# -*- coding: utf-8 -*-
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.CalcRating import CalcRating  # noqa: E402
from src.SecondQuartileRating import SecondQuartileRating  # noqa: E402
from src.TextDataReader import TextDataReader  # noqa: E402
from src.YAMLDataReader import YAMLDataReader  # noqa: E402


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p", dest="path", type=str, required=True, help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    reader = YAMLDataReader()
    students = reader.read("data/students.yaml")
    print(students)

    rating = CalcRating(students).calc()
    sq_rating = SecondQuartileRating()
    second_quartile_students = sq_rating.get_second_quartile_students(rating)

    print("Студенты второй квартиль рейтинга:")
    for name, rating in second_quartile_students:
        print(f"{name}: {rating:.2f}")


if __name__ == "__main__":
    main()
