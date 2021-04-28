from typing import List, Tuple, Union
from math import floor


class Number(int):
    def __str__(self):
        return f"{self:02}"



class Date:
    date_attrs = ('day', 'month', 'year')

    def __init__(self, date: str, /):
        fragments = date.split('-')

        if not self.validate(*fragments):
            raise ValueError(f"{date} invalid date format")

        self.day, self.month, self.year = self.transform(fragments)

    def __iter__(self):
        for attr in self.date_attrs:
            yield self.__getattribute__(attr)

    @classmethod
    def transform(cls, date: Union[List[str], Tuple[str]]) -> List[Number]:
        """ Приведение свалидированных элементов date к типу Number
        :param date: итерируемый объект с набором данных, готовых к преобразованию к типу Number
        :return:
        """
        return [Number(i) for i in date]

    @staticmethod
    def validate(*date: Union[List[str], Tuple[str]]) -> bool:
        """ Валидация входных данных на формат и контент
        входные данные представляют дату в виде кортежа
        (dd, mm, yyyy).
        День считается валидным, если лежит в диапазоне 1 - 31.
        Месяц считается валидным, если лежит в диапазоне 1 - 12.
        Год считается валидным начиная с 1970
        :param date: кортеж с 3 элементами в парядке dd, mm, yyyy
        :return: True - если проверка на формат и контент пройдены, иначе - False
        """
        try:
            day, month, year = [int(x) for x in date]
        except TypeError:  # исключение как при распаковке. так и при приведениее
            return False

        bis_sextus = bool(not (year % 400 and year % 4) and year % 100)
        end_mon_day = 28 + (month + floor(month / 8)) % 2 + 2 % month + 2 * floor(1 / month)
        end_mon_day += bis_sextus if month == 2 else 0

        return all([1 <= day <= end_mon_day, 1 <= month <= 12, year >= 1970])

    def __str__(self):
        return f"Date is '{'-'.join([str(s) for s in self])}'"


if __name__ == '__main__':
    for date in ('01-12-2011', '01-12-1969', '29-02-2020', '29-02-2021'):
        try:
            print(Date(date))
        except ValueError as e:
            print(e)