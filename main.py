from LessonPlanner import utils


if __name__ == '__main__':
    lessons = utils.select_lessons(utils.get_all_lessons())
    programes = utils.make_all_possible_program(lessons)
    for program in programes:
        for k, v in program.days.items():
            print(k, v)
        print()
