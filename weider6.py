#!/usr/bin/env python3

from datetime import timedelta
import os
import sys
import time
from typing import NamedTuple

SERIES_COUNT = 3
BREAK_TIME = timedelta(seconds=1.5)
REP_TICKS = 3
REP_TICK_TIME = timedelta(seconds=1)


def say(text, duration=None):
    start = time.time()
    if os.system('say {}'.format(text)):
        raise KeyboardInterrupt()
    elapsed = time.time() - start
    if duration and duration > elapsed:
        time.sleep(duration - elapsed)


class Exercise(NamedTuple):
    name: str
    double_count: bool
    immediate: bool = False

    def do(self, reps_count):
        say(self.name)
        if self.double_count:
            reps_count *= 2
        for rep in range(1, reps_count + 1):
            if self.immediate:
                say(rep, duration=REP_TICK_TIME.total_seconds())
            else:
                for _ in range(REP_TICKS):
                    say(rep, duration=REP_TICK_TIME.total_seconds())
                time.sleep(BREAK_TIME.total_seconds())
        time.sleep(BREAK_TIME.total_seconds())


EXERCISES = [
    Exercise('seperate legs no holding', True),
    Exercise('legs together no holding', False),
    Exercise('seperate legs holding', True),
    Exercise('legs together holding', False),
    Exercise('bicycle', True, immediate=True),
    Exercise('straight legs', False),
]


def main():
    try:
        for c in range(5, 0, -1):
            say(c)
        reps = int(sys.argv[1])
        for serie in range(1, SERIES_COUNT + 1):
            say('series {}'.format(serie))
            for exercise in EXERCISES:
                exercise.do(reps)
        say('well done you fat bastards')
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
