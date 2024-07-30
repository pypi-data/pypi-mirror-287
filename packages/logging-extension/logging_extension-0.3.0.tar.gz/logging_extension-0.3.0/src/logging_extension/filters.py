import logging
import operator
from typing import Literal, get_args, Callable


class LevelFilter(logging.Filter):
    allowed_compare = Literal['lt', 'le', 'eq', 'ne', 'ge', 'gt']
    _level: int
    _compare: Callable

    def __init__(self, level: int | str, compare: allowed_compare | Callable[[int, int], bool], name: str = ''):
        super().__init__(name=name)
        self.set_level(level)
        self.set_compare(compare)

    def filter(self, record: logging.LogRecord) -> bool:
        return self.compare(record.levelno, self.level)

    @property
    def compare(self) -> Callable[[int, int], bool]:
        return self._compare

    @property
    def level(self) -> int:
        return self._level

    def set_compare(self, compare: allowed_compare | Callable[[int, int], bool]) -> None:
        if isinstance(compare, Callable):
            self._compare = compare
        elif compare in (comp_args := get_args(self.allowed_compare)):
            self._compare = getattr(operator, compare)
        else:
            raise ValueError(f'Argument {compare=} must be Callable or one of {comp_args} strings')

    def set_level(self, level: str | int) -> None:
        lvl = level if isinstance(level, int) else logging.getLevelName(level)
        if not isinstance(lvl, int):
            raise ValueError(f'Argument {level=} is not valid logging level string')
        self._level = lvl


class BelowLevelFilter(logging.Filter):
    def __init__(self, level: str | int, name: str = ''):
        super().__init__(name=name)
        self.level = level if isinstance(level, int) else logging.getLevelName(level)

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelno < self.level


