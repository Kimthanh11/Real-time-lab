from Detection import *
from scheduler import *

schedule = Scheduler()
schedule.SCH_Init()

task1 = Detection(0)
# task2 = Detection("http://172.16.134.187:4747/video")
# task1.initializeCam()
# task2.initializeCam()
schedule.SCH_Add_Task(task1.prediction, 1000, 1000)
# schedule.SCH_Add_Task(task2.prediction, 2000, 6000)


while True:
    schedule.SCH_Update()
    schedule.SCH_Dispatch_Tasks()
    