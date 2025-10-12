# test/test_SecondQuartileRating.py
import pytest
from YAMLDataReader import YAMLDataReader
from SecondQuartileRating import SecondQuartileRating


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


def test_yaml_reader(sample_data):
    reader = YAMLDataReader()
    students = reader.read(sample_data)
    assert "Иванов Иван Иванович" in students
    assert isinstance(students["Петров Петр Петрович"], list)
