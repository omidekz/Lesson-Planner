import json
from LessonPlanner import models
from typing import List, Tuple, Dict

PACKAGES = 'packages'
NAME = 'name'
ListLesson = List[models.Lesson]
ListProgram = List[Tuple[str, models.Program]]


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
    lesson: Dict[str: str, str: List] = {
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
        except Exception:
            d: Dict = lesson["packages"][-1]
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


def make_json_lesson() -> str:
    return str(make_dict_lesson()).replace("'", '"')


def make_lesson_from_json(data: dict) -> models.Lesson:
    name = data[NAME]
    code = data[models.Lesson.CODE]
    lesson = models.Lesson(name, code)
    packages = data[PACKAGES]
    for package in packages:
        p_code = package[models.Lesson.CODE]
        days = package[models.Lesson.DAYS]
        times = package[models.Lesson.TIMES]
        ext = package[models.Lesson.EXAM_TIME]
        exm = package[models.Lesson.EXAM_MONTH]
        exd = package[models.Lesson.EXAM_DAY_DATE]
        lesson.addpackage(code=p_code,
                          times=times,
                          days=days,
                          exam_time=ext,
                          exam_day=exd,
                          exam_month=exm)
    return lesson


def get_all_lessons(path='Lessons.json') -> ListLesson:
    datas = json.load(open(path, 'r'))
    lessons: ListLesson = []
    for data in datas:
        lesson = make_lesson_from_json(data)
        lessons.append(lesson)
    return lessons


def select_lessons(lessons: ListLesson) -> ListLesson:
    for ind, lesson in enumerate(lessons):
        print('{})'.format(ind), lesson.name)
    code = list(map(int, input('enter lesson numbers separate by space 1 3 2 5 : ').split()))
    lessons = [lessons[i] for i in code]
    while input('do want to create some lesson[y/n]? : ').lower()[0] == 'y':
        lessons.append(make_lesson_from_json(make_dict_lesson()))
    return lessons


def get(lessons: ListLesson, code):
    for i in lessons:
        if i.code == int(code):
            return i
    return None


def make_all_possible_program(lessons: ListLesson, index: int = -1, program=None, result=None):
    if index == -1:
        res = []
        make_all_possible_program(lessons, 0, [], res)
        return res
    elif index == len(lessons):
        prog = models.Program(program.copy())
        if isok(prog):
            result.append(prog)
    else:
        for package in lessons[index].packages:
            program.append(package)
            make_all_possible_program(lessons, index + 1, program, result)
            program.pop()


def isok(prog: models.Program):
    for day_name, times in prog.days.items():
        times.sort(key=lambda x: x[1], reverse=False)
        for i in range(len(times) - 1):
            if times[i][1].conflict(times[i + 1][1]):
                return False
    for i in range(len(prog.packages)):
        for j in range(i + 1, len(prog.packages)):
            if prog.packages[i].exam_day[0] == -1 or prog.packages[i].exam_day[0] == '-1':
                continue
            if prog.packages[i].exam_day[0] == prog.packages[j].exam_day[0] and \
                    prog.packages[i].exam_day[1] == prog.packages[j].exam_day[1] and \
                    prog.packages[i].exam_day[2].conflict(prog.packages[j].exam_day[2]):
                return False

    return True
