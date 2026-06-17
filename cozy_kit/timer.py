# ============= cozy_kit/timer.py =============

# ============= IMPORTS =============

import threading
import time
import datetime as dt

from typing import Callable
from cozy_kit._internal import errors
from cozy_kit._internal.helpers.time_helpers import TimeHelpers

# ============= Timer CLASS =============


class Timer(TimeHelpers):
    """
    Provides countdown, pomodoro,
    and stopwatch timer utilities.
    Methods:
        countdown(count, time_type, show)
        start_pomodoro(work_time, break_time, long_break_time, show)
        pause_pomodoro()
        stop_pomodoro()
        resume_pomodoro()
        wait(count, time_type)
        start_stopwatch()
        end_stopwatch()
    """

    TIME_TYPES = {
        "min": 60,
        "sec": 1,
        "hour": 3600,
    }

    def __init__(self):
        self.paused = False
        self.running = True
        self.pomodoro_started = False

        super().__init__(
            time_types=self.TIME_TYPES,
            paused=self.paused,
            running=self.running,
            pomodoro_started=self.pomodoro_started,
        )

        self.start_time = None
        self._pomodoro_thread = None
        self.stopwatch_running = False

    def countdown(
        self,
        count: int,
        show: Callable[[str], None],
        time_type: str = "sec",
    ) -> None:
        """
        Starts a countdown timer.

        Parameters:
            count:
                Time amount.

            time_type:
                sec, min, or hour.

            show:
                Function used to display timer output.
        """

        self.running = True

        count = self._convert_type_to_seconds(count, time_type)

        self._format_time(
            count,
            show,
        )

        show("⏰ Time's up!")

        self._notify_user(
            title="Countdown",
            message="⏰ Time's up! Counter has ended",
        )

    # ============= POMODORO METHODS =============
    def start_pomodoro(
        self,
        work_time: int,
        break_time: int,
        long_break_time: int,
        show: Callable[[str], None],
        threaded: bool = False,
    ) -> None:
        self.pomodoro_started = True
        if threaded:
            self._pomodoro_thread = threading.Thread(
                target=self._pomodoro,
                args=(
                    work_time,
                    break_time,
                    long_break_time,
                    show,
                ),
                daemon=True,
            )

            self._pomodoro_thread.start()

        else:
            self._pomodoro(work_time, break_time, long_break_time, show)

    def pause_pomodoro(self) -> None:
        """
        Pauses the active pomodoro timer.
        """

        self.paused = True

    def stop_pomodoro(self) -> None:
        """
        Stops the active pomodoro timer.
        """

        self.running = False
        self.paused = False
        self.pomodoro_started = False

    def resume_pomodoro(self) -> None:
        """
        Resumes a paused pomodoro timer.
        """
        if not self.paused:
            raise errors.PomodoroNotPausedError(
                "You didn't pause the Pomodoro. "
                "Please pause it before you can resume it."
            )

        self.paused = False

    # ============= UTILITIES =============
    def wait(
        self,
        count: int,
        time_type: str,
    ) -> None:
        """
        Pauses execution for the specified duration.

        Parameters:
            count:
                Time amount.

            time_type:
                sec, min, or hour.
        """

        sleep_count = self._convert_type_to_seconds(count=count, time_type=time_type)

        time.sleep(sleep_count)

    @staticmethod
    def get_time() -> str:
        """
        Returns the current time.

        Returns:
            str:
                Current time formatted as HH:MM:SS p.
        """

        now = dt.datetime.now()

        return now.strftime("%I:%M %p")

    def start_stopwatch(self) -> None:
        """Starts the stopwatch."""

        self.stopwatch_running = True
        self.start_time = dt.datetime.now()

    def end_stopwatch(self) -> str:
        """
        Ends the stopwatch and returns the elapsed time as HH:MM:SS.
        """

        if not self.stopwatch_running:
            raise errors.StopWatchNotStartedError(
                "Stopwatch not started! " "Please run start_stopwatch() first."
            )

        end = dt.datetime.now()
        elapsed = end - self.start_time

        self.start_time = None
        self.stopwatch_running = False

        # Convert timedelta to HH:MM:SS string
        total_seconds = int(elapsed.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
