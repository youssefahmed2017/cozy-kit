import time
import datetime as dt

class InvalidTimeTypeError(Exception):
    pass

class Timer:
    TIME_TYPES = {
        'min':60,
        'sec':1,
        'hour':3600
                  }

    def __format_type(self, count, time_type):
        if time_type not in self.TIME_TYPES:
            raise InvalidTimeTypeError(f'"{time_type}" is not a valid time type. \nChoose: sec, min, or hour')

        count *= self.TIME_TYPES[time_type]

        return count

    def __format_time(self, count, show):

        for i in range(count, 0, -1):

            hours, remainder = divmod(i, 3600)

            mins, secs = divmod(remainder, 60)

            if hours > 0:

                show(
                    f"{hours:02}:{mins:02}:{secs:02}"
                )

            else:

                show(
                    f"{mins:02}:{secs:02}"
                )

            time.sleep(1)

    def countdown(self, count, time_type, show):
        count = self.__format_type(count, time_type)
        self.__format_time(count, show)

        show("⏰ Time's up!")
    #
    def pomodoro(self, work_time, break_time, long_break_time, show):
        """ Enter work, break, and long break as mins.
            and show is how you're gonna show it.
            Example:
                speak
                print
                label.config"""
        reps = 0
        work_time *= 60
        break_time *= 60
        long_break_time *= 60
        running = True
        while running:
            reps += 1
            if reps % 8 == 0:
                show("⏰ Long Break Time")
                self.__format_time(count=long_break_time, show=show)
            elif reps % 2 == 0:
                show("☕ Short Break Time")
                self.__format_time(count=break_time, show=show)
            else:
                show("💻 Work Time")
                self.__format_time(count=work_time, show=show)

    def wait(self, count, time_type):
        """time_type can either be 'min', 'sec' or 'hour'."""
        sleep_count = self.__format_type(count=count, time_type=time_type)

        time.sleep(sleep_count)

    def get_time(self):
        now = dt.datetime.now()
        return now.strftime("%H:%M:%S")

    def start_stopwatch(self):
        self.start_time = dt.datetime.now()

    def end_stopwatch(self):
        end = dt.datetime.now()

        elapsed = end - self.start_time

        return elapsed