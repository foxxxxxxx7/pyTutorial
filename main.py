class Clock:
    def __init__(self, hour, minute):
        hr, min = divmod(minute, 60)
        self._hour = (hr + hour) % 24
        self._minute = min

    def __repr__(self):
        return f"Clock({self._hour}, {self._minute})"

    def __str__(self):
        return f"{self._hour:02}:{self._minute:02}"

    def __eq__(self, other):
        return self._hour == other._hour and self._minute == other._minute

    def __add__(self, minutes):
        hrs, mins = divmod(minutes, 60)
        return Clock(self._hour + hrs, self._minute + mins)

    def __sub__(self, minutes):
        hrs, mins = divmod(minutes, 60)
        return Clock(self._hour - hrs, self._minute - mins)