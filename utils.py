import json
from LessonsProgrammer import models


PACKAGES = 'packages'
NAME = 'name'


def get_all_lessons():
    datas = json.load(open('/home/omid/PycharmProjects/myproject/LessonsProgrammer/Lessons.json', 'r'))
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


get_all_lessons()
