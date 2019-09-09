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
    new_lesson = []
    code = input('lesson code[-1 for finish]:')
    while code != '-1':
        res = get(lessons, code)
        if res and not get(new_lesson, code):
            new_lesson.append(res)
            print('added')
        elif get(new_lesson, code):
            print('it been added')
        else:
            print('not found this {} code'.format(code))
        code = input('lesson code[-1 for finish]:')
    return new_lesson


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
        result.append(models.Program(program.copy()))
    else:
        for package in lessons[index].packages:
            program.append((lessons[index].name, package))
            make_all_possible_program(lessons, index + 1, program, result)
            program.pop()
