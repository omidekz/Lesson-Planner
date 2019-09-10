from LessonPlanner import models
from LessonPlanner.utils import make_lesson_from_json


def get_day(val):
    _days_ = {
        "0": "شنبه",
        "1": "یکشنبه",
        "2": "دوشنبه",
        "3": "سه شنبه",
        "4": "چهارشنبه",
        "5": "پنجشنبه",
    }
    return _days_[val]


def make_dict_lesson() -> dict:
    name = input("name: ")
    code = "222" + input("code: ")
    packages = int(input("n of packages: "))
    lesson = {
        "name": name,
        "code": code,
        "packages": []
    }
    for i in range(packages):
        p_code = i + 1
        days = input("days: ").split()
        days = [get_day(i) for i in days]
        times = list(map(lambda x: x.split("-"), input("times: ").split()))
        while len(times) * 2 == len(days):
            times.append(times[0])
        try:
            exd, exm = input("exam date[day month]: ").split()
            ext = input("exam time[10:00-12:00]: ").split("-")
        except:
            d = lesson["packages"][-1]
            exd, exm, ext = d['exam_day'], d['exam_month'], d['exam_time']
        lesson["packages"].append({
            "code": p_code,
            "days": days,
            "times": times,
            "exam_month": exm,
            "exam_day": exd,
            "exam_time": ext
        })
    return lesson


def make_json_lesson():
    return str(make_dict_lesson()).replace("'", '"')
