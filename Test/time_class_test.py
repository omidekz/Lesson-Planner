from LessonPlanner import models

ftime = models.Time('10:00',
                    '12:00')
stime = models.Time('8:0', '24:9')

print(stime.conflict(ftime))

ttime = models.Time('6:00', '7:59')
print(ttime.conflict(stime))

print(ftime, stime)
