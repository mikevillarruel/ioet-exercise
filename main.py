from datetime import datetime, timedelta
from typing import Dict, List, Tuple

from models import Employee, Schedule


def read_file(path: str) -> List[str]:
    with open(path, "r") as file:
        return [item.strip() for item in file.readlines()]


def extract_data(file_data: List[str]) -> List[Employee]:
    employees: List[Employee] = []

    for fd in file_data:
        name, schedule_data = fd.split('=')
        daily_schedules = schedule_data.split(',')

        weekly_schedule: List[Schedule] = []

        for ds in daily_schedules:
            day: str = ds[0:2]
            time_interval: str = ds[2:].split('-')

            entry_time, departure_time = [str_to_datetime(item) for item in time_interval]

            weekly_schedule.append(Schedule(day, entry_time, departure_time))

        employees.append(Employee(name, weekly_schedule))

    return employees


def str_to_datetime(time_string: str) -> datetime:
    return datetime.strptime(time_string, "%H:%M")


def get_pairs_of_employees(employees: List[Employee]) -> Dict[str, int]:
    pairs: Dict[str, int] = {}
    for index, employee1 in enumerate(employees[0:-1]):
        for employee2 in employees[index + 1:]:
            pair_name, value = count_office_coincidences(employee1, employee2)
            pairs[pair_name] = value
    return pairs


def count_office_coincidences(employee1: Employee, employee2: Employee) -> Tuple[str, int]:
    pair_name: str = f"{employee1.name}-{employee2.name}"
    coincidences: int = 0

    for dailyScheduleEmp1 in employee1.weekly_schedule:
        for dailyScheduleEmp2 in employee2.weekly_schedule:

            if dailyScheduleEmp1.day == dailyScheduleEmp2.day:
                if coincidence_exist(dailyScheduleEmp1, dailyScheduleEmp2):
                    coincidences += 1

    return pair_name, coincidences


def coincidence_exist(schedule1: Schedule, schedule2: Schedule) -> bool:
    if schedule1.day != schedule2.day:
        return False
    max_entry: datetime = max(schedule1.entry_time, schedule2.entry_time)
    min_departure: datetime = min(schedule1.departure_time, schedule2.departure_time)
    delta: timedelta = (min_departure - max_entry)
    if delta.total_seconds() > 0:
        return True
    else:
        return False


def print_pairs(pairs: Dict[str, int]):
    for pair, quantity in pairs.items():
        print(pair + ": " + str(quantity))


def main():
    file_data: List[str] = read_file("schedules.txt")
    employees_schedule: List[Employee] = extract_data(file_data)
    pairs: Dict[str, int] = get_pairs_of_employees(employees_schedule)
    print_pairs(pairs)


if __name__ == '__main__':
    main()
