# -*- coding: utf-8 -*-
from DataReader import DataReader
from Types import DataType
import yaml


class YAMLDataReader(DataReader):
    """
    Читает данные студентов из YAML-файла.
    Формат:
    - Иванов Иван Иванович:
        математика: 67
        литература: 100
        программирование: 91
    - Петров Петр Петрович:
        математика: 78
        химия: 87
        социология: 61
    """

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            raw_data = yaml.safe_load(file)

        students: DataType = {}
        for student_entry in raw_data:
            for name, subjects in student_entry.items():
                students[name] = [
                    (subj, score) for subj, score in subjects.items()
                ]

        return students
