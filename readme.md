# Lesson Planner
- this repo make a list of possible Lesson-Plan by brute-force algorithm

## Structure:
* ### all [models](models/models.py):
    - Time: 
        - start
        - end
        - time can be checked for `conflict() -> bool`
    - Day:
        - name
        - time
    - Package:
        - days
        - code
    - Lesson:
        - packages
        - code
        - name
    - Program:
        - packages
        - day -> for getting plane
* ### Lessons.json
     - this file representation of the lessons database 
     - Time     json: `[str, str]` ex: `{["08:00", "10:00"]}`
     - Package  json: `{"code": int, "days": [], "times":[], "exam_month": str, "exam_day": str, "exam_time": []}` -> times is a nested list, each list for specific day
     - Lesson   json: `{"name": str, "code": str, "packages": []}` -> packages is a list of above format
* ### brief description of structure:
    - each lesson has name and code, and some packages
     ex: mathematical with code=12 present in 2 groups:
     <br>group 1: Sunday an Monday in 08:00 o'clock until 10:00 o'clock
     <br>group 2: Saturday and Wednesday at the same time
     <br> so we have [Lesson](models/models.py) and each lesson has some [Package](models/models.py).
     <br> each package held in certain days. So we have [Day](models/models.py), and each day has a name and time.<br>
     **pay attention...** a said time, So we have [Time](models/models.py) model that each time has an start and end.
     <br>times maybe have a conflict so a good plan has no conflict