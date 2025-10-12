# test/test_SecondQuartileRating.py# test/test_SecondQuartileRating.py
import pytest
from src.YAMLDataReader import YAMLDataReader
from src.SecondQuartileRating import SecondQuartileRating
from src.CalcRating import CalcRating

@pytest.fixture()
def sample_data(tmp_path):
    content = """
- Иванов Иван Иванович:
    математика: 67
    литература: 100
    программирование: 91
- Петров Петр Петрович:
    математика: 78
    химия: 87
    социология: 61
- Сидоров Сидор Сидорович:
    математика: 90
    литература: 85
    физкультура: 95
- Кузнецов Кузьма Кузьмич:
    математика: 70
    литература: 75
    программирование: 80
"""
    file = tmp_path / "students.yaml"
    file.write_text(content, encoding='utf-8')
    return str(file)

def test_second_quartile(sample_data):
    reader = YAMLDataReader()
    students = reader.read(sample_data)
    rating = CalcRating(students).calc()
    sq_rating = SecondQuartileRating()
    sq_students = sq_rating.get_second_quartile_students(rating)
    # Проверяем, что возвращается список кортежей
    assert all(isinstance(x, tuple) for x in sq_students)
