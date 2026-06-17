# ============= cozy_kit/_internal/helpers/time_helpers.py =============

# ============= IMPORTS =============
from cozy_kit._internal import errors
import time
from typing import Callable
from plyer import notification


class TimeHelpers:
    def __init__(self, time_types: dict, paused, running, pomodoro_started) -> None:
        self.TIME_TYPES = time_types  # The time_types for _convert_type_to_seconds
        self.paused = paused
        self.running = running
        self.pomodoro_started = pomodoro_started

    def _convert_type_to_seconds(
        self,
        count: int,
        time_type: str,
    ) -> int:
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

    @staticmethod
    def _notify_user(
        message: str,
        title: str,
        duration: int = 3,
    ) -> None:
        notification.notify(
            title=title,
            message=message,
            timeout=duration,
        )

    def _format_time(
        self,
        count: int,
        show: Callable[[str], None],
    ) -> None:
        # Display time
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

    def _pomodoro(
        self,
        work_time: int,
        break_time: int,
        long_break_time: int,
        show: Callable[[str], None],
    ) -> None:
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

            # ============= CHECKS =============
            # Long Break
            if reps % 8 == 0:
                show("⏰ Long Break Time")

                self._notify_user(
                    title="Pomodoro Long Break Time ⏰",
                    message=(
                        "It's time for a long break. "
                        f"Enjoy {raw_long_break_time} "
                        "minutes of chilling!"
                    ),
                )

                self._format_time(
                    count=long_break_time,
                    show=show,
                )
            # Short Break
            elif reps % 2 == 0:
                show("☕ Short Break Time")

                self._notify_user(
                    title="Pomodoro Short Break Time ☕",
                    message=(
                        "It's time for a short break. "
                        "Have maybe some coffee and "
                        "enjoy your break!"
                    ),
                )

                self._format_time(
                    count=break_time,
                    show=show,
                )
            # Work
            else:
                show("💻 Work Time")

                self._notify_user(
                    title="Pomodoro Work Time 💻",
                    message="Let's get back to work.",
                )

                self._format_time(
                    count=work_time,
                    show=show,
                )
