from LessonPlanner import utils

print(utils.get_all_lessons(path='../Lessons.json'))
lessons = utils.select_lessons(utils.get_all_lessons('../Lessons.json'))
progs = utils.make_all_possible_program(lessons)
for prog in progs:
    for k, v in prog.days.items():
        print(k, v)
    print()
