# ====================================================
class CozyKitError(Exception):
    pass


# =====================================================


class InvalidTimeTypeError(CozyKitError):
    pass


class InvalidShiftError(CozyKitError):
    pass


class InvalidTimeAmountError(CozyKitError):
    pass


class InvalidStoryError(CozyKitError):
    pass


class StopWatchNotStartedError(CozyKitError):
    pass


class DatabaseNotFoundError(CozyKitError):
    pass


class PomodoroNotStartedError(CozyKitError):
    pass


class PomodoroNotPausedError(CozyKitError):
    pass


class InvalidMotivationNameError(CozyKitError):
    pass


class InvalidMotivationContentError(CozyKitError):
    pass


class InvalidFunFactError(CozyKitError):
    pass


class TimerAlreadyRunningError(CozyKitError):
    pass


class EmptyTextError(CozyKitError):
    pass


class InvalidStyleError(CozyKitError):
    pass


class TimerAlreadyStartedError(CozyKitError):
    pass
