import unittest
from datetime import datetime

from main import str_to_datetime, coincidence_exist, count_office_coincidences, get_pairs_of_employees
from models import Schedule, Employee


class Test(unittest.TestCase):

    def test_str_to_datetime(self):
        self.assertEqual(str_to_datetime("10:15"), datetime.strptime("10:15", "%H:%M"))
        self.assertEqual(str_to_datetime("13:50"), datetime.strptime("13:50", "%H:%M"))

    def test_count_office_coincidences(self):
        self.assertEqual(
            count_office_coincidences(
                Employee(
                    name="JULIO",
                    weekly_schedule=[
                        Schedule(
                            "MO",
                            datetime.strptime("10:00", "%H:%M"),
                            datetime.strptime("11:00", "%H:%M")
                        ), Schedule(
                            "TH",
                            datetime.strptime("15:00", "%H:%M"),
                            datetime.strptime("18:45", "%H:%M")
                        )
                    ]
                ), Employee(
                    name="MARIO",
                    weekly_schedule=[
                        Schedule(
                            "MO",
                            datetime.strptime("9:15", "%H:%M"),
                            datetime.strptime("11:30", "%H:%M")
                        ), Schedule(
                            "SU",
                            datetime.strptime("10:00", "%H:%M"),
                            datetime.strptime("10:45", "%H:%M")
                        )
                    ]
                )
            ), ('JULIO-MARIO', 1))

        self.assertEqual(
            count_office_coincidences(
                Employee(
                    name="JULIO",
                    weekly_schedule=[
                        Schedule(
                            "MO",
                            datetime.strptime("10:00", "%H:%M"),
                            datetime.strptime("11:00", "%H:%M")
                        ), Schedule(
                            "TH",
                            datetime.strptime("15:00", "%H:%M"),
                            datetime.strptime("18:45", "%H:%M")
                        )
                    ]
                ), Employee(
                    name="RENE",
                    weekly_schedule=[
                        Schedule(
                            "TH",
                            datetime.strptime("9:15", "%H:%M"),
                            datetime.strptime("11:30", "%H:%M")
                        ), Schedule(
                            "SU",
                            datetime.strptime("10:00", "%H:%M"),
                            datetime.strptime("10:45", "%H:%M")
                        )
                    ]
                )
            ), ('JULIO-RENE', 0))

    def test_get_pairs_of_employees(self):
        self.assertEqual(
            get_pairs_of_employees([
                Employee(
                    name="SANDRA",
                    weekly_schedule=[
                        Schedule(
                            "MO",
                            datetime.strptime("10:00", "%H:%M"),
                            datetime.strptime("11:00", "%H:%M")
                        ), Schedule(
                            "TH",
                            datetime.strptime("15:00", "%H:%M"),
                            datetime.strptime("18:45", "%H:%M")
                        )
                    ]
                ), Employee(
                    name="MARIO",
                    weekly_schedule=[
                        Schedule(
                            "MO",
                            datetime.strptime("9:15", "%H:%M"),
                            datetime.strptime("11:30", "%H:%M")
                        ), Schedule(
                            "SU",
                            datetime.strptime("10:00", "%H:%M"),
                            datetime.strptime("10:45", "%H:%M")
                        )
                    ]
                ),
                Employee(
                    name="JULIO",
                    weekly_schedule=[
                        Schedule(
                            "MO",
                            datetime.strptime("10:00", "%H:%M"),
                            datetime.strptime("11:00", "%H:%M")
                        ), Schedule(
                            "TH",
                            datetime.strptime("15:00", "%H:%M"),
                            datetime.strptime("18:45", "%H:%M")
                        )
                    ]
                ), Employee(
                    name="RENE",
                    weekly_schedule=[
                        Schedule(
                            "TH",
                            datetime.strptime("9:15", "%H:%M"),
                            datetime.strptime("11:30", "%H:%M")
                        ), Schedule(
                            "SU",
                            datetime.strptime("10:00", "%H:%M"),
                            datetime.strptime("10:45", "%H:%M")
                        )
                    ]
                )
            ]), {
                'SANDRA-MARIO': 1,
                'SANDRA-JULIO': 2,
                'SANDRA-RENE': 0,
                'MARIO-JULIO': 1,
                'MARIO-RENE': 1,
                'JULIO-RENE': 0
            })

    def test_coincidence_exist(self):
        self.assertEqual(
            coincidence_exist(
                Schedule(
                    "MO",
                    datetime.strptime("10:15", "%H:%M"),
                    datetime.strptime("10:30", "%H:%M")
                ), Schedule(
                    "MO",
                    datetime.strptime("10:00", "%H:%M"),
                    datetime.strptime("10:45", "%H:%M")
                )
            ), True)

        self.assertEqual(
            coincidence_exist(
                Schedule(
                    "MO",
                    datetime.strptime("09:10", "%H:%M"),
                    datetime.strptime("10:00", "%H:%M")
                ), Schedule(
                    "MO",
                    datetime.strptime("10:00", "%H:%M"),
                    datetime.strptime("10:45", "%H:%M")
                )
            ), False)

        self.assertEqual(
            coincidence_exist(
                Schedule(
                    "TH",
                    datetime.strptime("09:10", "%H:%M"),
                    datetime.strptime("19:00", "%H:%M")
                ), Schedule(
                    "WE",
                    datetime.strptime("10:00", "%H:%M"),
                    datetime.strptime("18:45", "%H:%M")
                )
            ), False)


if __name__ == '__main__':
    unittest.main()
