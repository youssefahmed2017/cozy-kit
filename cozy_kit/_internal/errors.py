# ============= cozy_kit/_internal/errors.py =============


# ============= MAIN ERROR =============
class CozyKitError(Exception):
    pass


# ============= Timer ERRORS =============


class InvalidTimeAmountError(CozyKitError):
    pass


class StopWatchNotStartedError(CozyKitError):
    pass


class InvalidTimeTypeError(CozyKitError):
    pass


class PomodoroNotStartedError(CozyKitError):
    pass


class PomodoroNotPausedError(CozyKitError):
    pass


# ============= TextEditor ERRORS =============


class InvalidShiftError(CozyKitError):
    pass


class EmptyTextError(CozyKitError):
    pass


# ============= TextCustomizations ERRORS =============


class InvalidStyleError(CozyKitError):
    pass


# ============= Greeting ERRORS =============


class InvalidStoryError(CozyKitError):
    pass


class InvalidMotivationError(CozyKitError):
    pass


class InvalidFunFactError(CozyKitError):
    pass


# ============= JSON ERRORS =============


class DatabaseNotFoundError(CozyKitError):
    pass


# ============= SMTPMailer ERRORS =============


class UnfilledPasswordAndEmailError(CozyKitError):
    pass


class NoRecipientError(CozyKitError):
    pass


class AttachmentNotFoundError(CozyKitError):
    pass
