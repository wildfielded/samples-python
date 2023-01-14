#!/usr/bin/python3

from dataclasses import dataclass
from datetime import datetime
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        return []


''' =====----- MAIN -----===== '''
if __name__ == '__main__':
    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])
    for d in m.schedule():
        print(d)

#####=====----- THE END -----=====#########################################