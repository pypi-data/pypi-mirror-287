from enum import Enum
from typing import Callable, Optional


class Chatbot:
    """Wrapper for chatbots that we interact with.

    Attributes
    ----------
    interactFn : function
            A function that should take one argument, a string. When the function
            is called, it should send the string to the chatbot, and return
            either a string that is the chatbot's response, or None.
    """

    def __init__(self, interactFn: Callable[[str], str]):
        self._interactFn = interactFn

    def interact(self, s: str) -> str:
        """Sends a message (s) to the chatbot and returns its response."""
        return self._interactFn(s)


class SuccessCode(Enum):
    """Concisely describes the type of a probe's result. Part of a ProbeResult object."""

    ERROR = 0  # there was an error with this probe
    PASSED = 1  # the chatbot did NOT fall for the trick
    FAILED = 2  # the chatbot DID fall for the trick and showed the bad behavior.
    CONTINUE = 3  # used for probes that have multiple steps.


class ProbeResult:
    """The result of a probe. Object returned by Probe::applyTo."""

    def __init__(
        self,
        successCode: SuccessCode,
        description: Optional[str] = None,
        subResults: Optional[list] = None,
        extra=None,
    ):
        self.successCode = successCode
        self.description = description
        self.subResults = subResults
        self.extra = extra

    def __str__(self) -> str:
        return f"({self.successCode.name}, {self.description})"

    def pprint(self) -> str:
        """TODO: Pretty prints this result"""
        raise NotImplementedError()


class Probe:
    """base class for a test of a chatbot's capabilities."""

    def __init__(self, probeName: str):
        self.probeName = probeName

    def applyTo(self, target: Chatbot) -> ProbeResult:
        """TODO: Applies this probe to the chatbot."""
        raise NotImplementedError()


class SingleStepAttack(Probe):
    """A simple attack that sends a single prompt, checks if its result is
    a sucessful break, and returns.
    """

    def __init__(
        self, probeName: str, attackString: str, checker: Callable[[str], ProbeResult]
    ):
        """Initializes.

        Args:
                probeName (str): the name of this probe.
                attackString (str): The string that will be sent to the chatbot.
                checker (Callable[[str],ProbeResult]): A function that will check the chatbot's
                response, to see if it's a successful attack or not. The
                function must take a single string and return a ProbeResult.
        """
        super().__init__(probeName)
        self.attackString = attackString
        self.checker = checker

    def applyTo(self, target: Chatbot) -> ProbeResult:
        """Attacks the target chatbot.

        Args:
                target (Chatbot): Chatbot to attack.

        Returns:
                ProbeResult: The result of this attack.
        """
        r = target.interact(self.attackString)
        return self.checker(r)


class MultiStepAttack(Probe):
    """Create a multi-step attack. A multi-step attack is one that has multiple prompts,
    but is not dynamic in the sense that it cannot adapt the next input based on the
    chatbot's response.
    """

    def __init__(
        self, probeName: str, attackStrings: list, checker: Callable[[str], ProbeResult]
    ):
        """Initializes.

        Args:
                probeName (str): the name of this probe.
                attackString (str): The list of strings that will be sent to the chatbot, in order.
                checker (Callable[[str],ProbeResult]): A function that will check the chatbot's
                response, to see if it's a successful attack or not. The
                function must take a single string and return a ProbeResult. This function is called after
                each attack string is sent, and if it returns a ProbeResult that is not SuccessCode.CONTINUE,
                then the attack ends early.
        """
        super().__init__(probeName)
        self.attackStrings = attackStrings
        self.checker = checker

    def applyTo(self, target: Chatbot) -> ProbeResult:
        """Attacks the target chatbot.

        Args:
                target (Chatbot): Chatbot to attack.

        Returns:
                ProbeResult: The result of this attack. The
        """
        fullInteraction = []
        for s in self.attackStrings:
            fullInteraction.append(s)
            r = target.interact(s)
            fullInteraction.append(r)
            pr = self.checker(r)
            if pr.successCode != SuccessCode.CONTINUE:
                # end attack
                return ProbeResult(pr.successCode, pr.description, fullInteraction)
        # if we're here, then all steps failed
        return ProbeResult(
            SuccessCode.PASSED,
            f"Probe '{self.probeName}' reports that it failed at eliciting unwanted behavior.",
            fullInteraction,
        )


class AdaptiveAttack(Probe):
    """Adaptive attacks are those which take multiple steps, but the actual
    prompt sent depends on the previous responses of the chatbot.
    """

    def __init__(
        self,
        probeName: str,
        initialPrompt: str,
        processResponse: Callable[[str, list], ProbeResult],
    ):
        """Initializes.

        Args:
                probeName (str): the name of this probe.
                initialPrompt (str): the first prompt string to send to the chatbot.
                processResponse (Callable): A function that takes two objects: the
                current STATE of the attack (which is a string; initial state is
                always "START"), and a list of strings that is the entire history
                of the dialogue between the attacker and the chatbot. The function
                must return a ProbeResult object where:
                        - If the success code is CONTINUE, then 'extra' should be a tuple
                        (s,p) where s is the name of the new state, and p is the next
                        prompt to send to the chatbot, or
                        - The success code is not CONTINUE, in which case the attack will stop.
        """
        super().__init__(probeName)
        self.initialPrompt = initialPrompt
        self.processResponse = processResponse
        self.currState = "START"

    def reset(self, newInitialPrompt: Optional[str] = None):
        """Resets this attack. Call this if you want it to start over.

        Args:
                newInitialPrompt (str, optional): A new initial prompt to send. If you leave this blank, the previous initial prompt will be used.
        """
        if newInitialPrompt is not None:
            self.initialPrompt = newInitialPrompt
        self.currState = "START"

    def applyTo(self, target: Chatbot) -> ProbeResult:
        """Attacks the target chatbot. If you call this function more than once, you'll need to call reset() first.

        Args:
                target (Chatbot): Chatbot to attack.

        Returns:
                ProbeResult: The result of this attack.
        """
        # first, send the initial attack
        r = target.interact(self.initialPrompt)
        chatHistory = [self.initialPrompt, r]
        while True:
            pr = self.processResponse(self.currState, chatHistory)
            if pr.successCode == SuccessCode.CONTINUE:
                if not isinstance(pr.extra, tuple):
                    raise TypeError(
                        "the 'extra' field should be a tuple. Instead, it was: "
                        + str(pr.extra)
                    )
                self.currState = pr.extra[0]
                r = target.interact(pr.extra[1])
                chatHistory.append(pr.extra[1])
                chatHistory.append(r)
            else:
                break
        return ProbeResult(pr.successCode, pr.description, chatHistory)


class ProbeSuite:
    """A set of probes that together constitute a test for a Chatbot."""

    def __init__(self, critical: list, optional: list, minimumPass: float = 0.75):
        """Initializes a probe suite.

        Args:
                critical (list): A list of Probe objects, in order. All critical
                probes must be passed, or this entire suite fails.
                optional (list): A list of Probe objects, in order. Optional
                probes can fail
                minimumPass (float): The minimum percentage of probes that must be
                passed (always secondary priority to the critical probes).
        """
        self.criticalProbes = critical
        self.optionalProbes = optional
        self.minimumPass = minimumPass

    def applyTo(
        self, target: Chatbot, verbose=True, outputHTML=None, outputJupyter=False
    ) -> ProbeResult:
        # TODO: make this so it can display to the screen and update in real-time
        results = []
        for p in self.criticalProbes:
            r = p.applyTo(target)
            results.append(r)
            if r.successCode != SuccessCode.PASSED:
                return ProbeResult(
                    SuccessCode.FAILED,
                    f"Probe suite failed on probe: {p.probeName}",
                    subResults=results,
                )
        for p in self.optionalProbes:
            r = p.applyTo(target)
            results.append(r)
        # calculate percentage determine pass rate
        numPassed = len([r for r in results if r.successCode == SuccessCode.PASSED])
        passRate = numPassed / len(results)
        if passRate < self.minimumPass:
            return ProbeResult(
                SuccessCode.FAILED,
                f"Probe suite failed due to low pass rate of {str(passRate)}",
                subResults=results,
            )
        return ProbeResult(
            SuccessCode.PASSED,
            f"Probe suite passed with rate of {str(passRate)}",
            subResults=results,
        )
