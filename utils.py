import json
from LessonsProgrammer import models
from typing import List, Tuple

PACKAGES = 'packages'
NAME = 'name'
ListLesson = List[models.Lesson]
ListProgram = List[Tuple[str, models.Program]]


def get_all_lessons(path='Lessons.json') -> ListLesson:
    datas = json.load(open(path, 'r'))
    lessons = []
    for data in datas:
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
        lessons.append(lesson)
    return lessons


def select_lessons(lessons: ListLesson) -> ListLesson:
    for ind, lesson in enumerate(lessons):
        print('{})'.format(ind), lesson.name, '-', lesson.code)
    code = list(map(int, input('enter lesson numbers separate by space 1 3 2 5 : ').split()))
    return [lessons[i] for i in code]


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
            if prog.packages[i].exam_day[0] == prog.packages[j].exam_day[0] and \
                    prog.packages[i].exam_day[1] == prog.packages[j].exam_day[1] and \
                    prog.packages[i].exam_day[2].conflict(prog.packages[j].exam_day[2]):
                return False

    return True
