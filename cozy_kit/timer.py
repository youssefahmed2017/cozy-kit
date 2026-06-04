import threading
import time
import datetime as dt

from typing import Callable
from plyer import notification
from . import errors


class Timer:
    """
    Provides countdown, pomodoro,
    and stopwatch timer utilities.
    """

    TIME_TYPES = {
        "min": 60,
        "sec": 1,
        "hour": 3600,
    }

    def __init__(self):
        self.paused = False
        self.running = True
        self.start_time = None
        self.pomodoro_started = False
        self.stopwatch_running = False

    def __convert_type_to_seconds(
        self,
        count: int,
        time_type: str,
    ) -> int:
        """
        Converts a time amount into seconds.

        Parameters:
            count:
                Time amount.

            time_type:
                sec, min, or hour.

        Returns:
            int:
                Time converted to seconds.
        """

        if time_type not in self.TIME_TYPES:
            raise errors.InvalidTimeTypeError(
                f'{time_type}" is not a valid time type. ' "Choose: sec, min, or hour"
            )

        if count <= 0:
            raise errors.InvalidTimeAmountError(
                f'{count}" is an invalid amount. ' f"{count} must be greater than 0"
            )

        count *= self.TIME_TYPES[time_type]

        return count

    def __notify_user(
        self,
        message: str,
        title: str,
        duration: int = 3,
    ) -> None:
        notification.notify(
            title=title,
            message=message,
            timeout=duration,
        )

    def __format_time(
        self,
        count: int,
        show: Callable[[str], None],
    ) -> None:
        """
        Formats and displays a live countdown timer.

        Parameters:
            count:
                Countdown duration in seconds.

            show:
                Function used to display timer output.
        """

        if self.pomodoro_started:
            raise errors.TimerAlreadyStartedError(
                "You have already "
                "started the timer."
                "Please stop it "
                "before you can run it again."
            )

        for i in range(count, 0, -1):
            while self.paused:
                time.sleep(0.1)

            if not self.running:
                break

            hours, remainder = divmod(i, 3600)
            mins, secs = divmod(remainder, 60)

            if hours > 0:
                show(f"{hours:02}:{mins:02}:{secs:02}")
            else:
                show(f"{mins:02}:{secs:02}")

            time.sleep(1)

    def countdown(
        self,
        count: int,
        time_type: str,
        show: Callable[[str], None],
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

        count = self.__convert_type_to_seconds(count, time_type)

        self.__format_time(
            count,
            show,
        )

        show("⏰ Time's up!")

        self.__notify_user(
            title="Countdown",
            message="⏰ Time's up! Counter has ended",
        )

    def __pomodoro(
        self,
        work_time: int,
        break_time: int,
        long_break_time: int,
        show: Callable[[str], None],
    ) -> None:
        """
        Starts a fully implemented pomodoro timer
        with work, short break, and long break sessions.

        Parameters:
            work_time:
                Work session duration in minutes.

            break_time:
                Short break duration in minutes.

            long_break_time:
                Long break duration in minutes.

            show:
                Function used to display timer output.
        """

        reps = 0

        self.running = True

        raw_long_break_time = long_break_time

        work_time *= 60
        break_time *= 60
        long_break_time *= 60

        while self.running:
            if not self.running:
                show("00:00")
                break

            reps += 1

            if reps % 8 == 0:
                show("⏰ Long Break Time")

                self.__notify_user(
                    title="Pomodoro Long Break Time ⏰",
                    message=(
                        "It's time for a long break. "
                        f"Enjoy {raw_long_break_time} "
                        "minutes of chilling."
                    ),
                )

                self.__format_time(
                    count=long_break_time,
                    show=show,
                )

            elif reps % 2 == 0:
                show("☕ Short Break Time")

                self.__notify_user(
                    title="Pomodoro Short Break Time ☕",
                    message=(
                        "It's time for a short break. "
                        "Have maybe some coffee and "
                        "continue your work."
                    ),
                )

                self.__format_time(
                    count=break_time,
                    show=show,
                )

            else:
                show("💻 Work Time")

                self.__notify_user(
                    title="Pomodoro Work Time 💻",
                    message="Let's get back to work.",
                )

                self.__format_time(
                    count=work_time,
                    show=show,
                )

    def start_pomodoro(
        self,
        work_time: int,
        break_time: int,
        long_break_time: int,
        show: Callable[[str], None],
    ) -> None:
        self.pomodoro_started = True

        self._pomodoro_thread = threading.Thread(
            target=self.__pomodoro,
            args=(
                work_time,
                break_time,
                long_break_time,
                show,
            ),
            daemon=True,
        )

        self._pomodoro_thread.start()

    def pause_pomodoro(self) -> None:
        """
        Pauses the active pomodoro timer.
        """

        if not self.pomodoro_started:
            raise errors.PomodoroNotStartedError(
                "You didn't start the Pomodoro. "
                "Please start before you can pause it."
            )

        self.paused = True

    def stop_pomodoro(self) -> None:
        """
        Stops the active pomodoro timer.
        """

        if not self.pomodoro_started:
            raise errors.PomodoroNotStartedError(
                "You didn't start the Pomodoro. "
                "Please run pomodoro() before you can stop it."
            )

        self.running = False
        self.paused = False
        self.pomodoro_started = False

    def resume_pomodoro(self) -> None:
        """
        Resumes a paused pomodoro timer.
        """

        if not self.pomodoro_started:
            raise errors.PomodoroNotStartedError(
                "You didn't start the Pomodoro. "
                "Please run pomodoro() before you can "
                "pause it, then resume it."
            )

        if not self.paused:
            raise errors.PomodoroNotPausedError(
                "You didn't pause the Pomodoro. "
                "Please pause it before you can resume it."
            )

        self.paused = False

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

        sleep_count = self.__convert_type_to_seconds(count=count, time_type=time_type)

        time.sleep(sleep_count)

    def get_time(self) -> str:
        """
        Returns the current time.

        Returns:
            str:
                Current time formatted as HH:MM:SS.
        """

        now = dt.datetime.now()

        return now.strftime("%H:%M:%S")

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
