from calendar import month_name
from project.month_mapper import month_mapper


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(x) for x in date.split(".")]
        # str_month = cls.get_month_str(month)
        str_month = month_name[month]
        # str_month = month_mapper[month]
        return cls(name, id, year, str_month, age_restriction)

    # @staticmethod
    # def get_month_str(mon):
    #     months = {
    #         "01": "January",
    #         "02": "February",
    #         "03": "March",
    #         "04": "April",
    #         "05": "May",
    #         "06": "June",
    #         "07": "July",
    #         "08": "August",
    #         "09": "September",
    #         "10": "October",
    #         "11": "November",
    #         "12": "December"
    #     }
    #     if mon in months:
    #         return months[mon]

    def __repr__(self):
        rented_status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented_status}"