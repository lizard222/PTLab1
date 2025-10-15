# -*- coding: utf-8 -*-
from typing import List, Tuple


class SecondQuartileRating:
    """
    Рассчитывает рейтинг студентов и выбирает студентов,
    чей рейтинг попадает во вторую квартиль.
    """

    def get_second_quartile_students(
        self, rating: dict[str, float]
    ) -> List[Tuple[str, float]]:
        ratings_sorted = sorted(rating.items(), key=lambda x: x[1])
        n = len(ratings_sorted)
        q1 = n // 4
        q2 = n // 2
        # вторая квартиль: от q1 до q2 (25%-50%)
        return ratings_sorted[q1:q2]
