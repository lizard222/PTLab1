# test/test_YAMLDataReader.py
import pytest

from src.Types import DataType
from src.YAMLDataReader import YAMLDataReader


@pytest.fixture()
def sample_data(tmp_path) -> tuple[str, DataType]:
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
    """
    data = {
        "Иванов Иван Иванович": [
            ("математика", 67),
            ("литература", 100),
            ("программирование", 91),
        ],
        "Петров Петр Петрович": [
            ("математика", 78),
            ("химия", 87),
            ("социология", 61),
        ],
        "Сидоров Сидор Сидорович": [
            ("математика", 90),
            ("литература", 85),
            ("физкультура", 95),
        ],
    }
    file = tmp_path / "students.yaml"
    file.write_text(content, encoding="utf-8")
    return str(file), data


def test_yaml_reader(sample_data):
    reader = YAMLDataReader()
    students = reader.read(sample_data[0])
    assert "Иванов Иван Иванович" in students
    assert isinstance(students["Петров Петр Петрович"], list)
    assert students == sample_data[1]
