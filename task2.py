"""Module 5/Task 2"""

from re import compile
from typing import Callable, List, Iterator


PATTERN = compile(r"\d+[.,]?\d+")


def generator_numbers_with_findall(text: str) -> List[float]:
    """Parse number from the text with regex[findall]"""

    get_numbers_as_list = [float(number) for number in PATTERN.findall(text)]

    return get_numbers_as_list


def generator_numbers_with_finditer(text: str) -> Iterator[float]:
    """Parse number from the text with regex[finditer]"""

    parsed_numbers_iter = PATTERN.finditer(text)

    for number_match in parsed_numbers_iter:
        number = float(number_match.group())
        yield number


def sum_profit(text: str, func: Callable) -> int:
    """Count a sum"""
    profit = func(text)
    return sum(profit)


if __name__ == "__main__":

    TEXT = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,"
            " доповнений додатковими надходженнями 27.45 і 324.00 доларів.")

    total_income = sum_profit(TEXT, generator_numbers_with_findall)
    print(f"Загальний дохід: {total_income}")

    total_income = sum_profit(TEXT, generator_numbers_with_finditer)
    print(f"Загальний дохід: {total_income}")
