class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:

                return f'All right'

            else:
                return f'month is incorrect, try again!'
        else:
            return f'day is incorrect, try again!'

    def __str__(self):
        return f'Current date {Data.extract(self.day_month_year)}'


today = Data('11 - 1 - 2001')
print(today)
print(Data.valid(40, 11, 2022))
print(today.valid(81, 13, 2011))
print(Data.extract('13 - 2 - 1987'))
print(today.extract('21 - 7 - 2020'))
print(Data.valid(1, 11, 2000))
