from Detection import *
from scheduler import *
import time
schedule = Scheduler()
schedule.SCH_Init()

task1 = Detection(0, 0)
task2 = Detection("http://172.16.134.187:4747/video", 0)
# task1.initializeCam()
# task2.initializeCam()
schedule.SCH_Add_Task(task1.run, 0, 1000)
schedule.SCH_Add_Task(task2.run, 2000, 6000)


while True:
    schedule.SCH_Update()
    schedule.SCH_Dispatch_Tasks()
    time.sleep(0.1)

# print("Hello LAB2")
# import time
# from scheduler import *
# from task1 import *
# from task2 import *
# scheduler = Scheduler()
# scheduler.SCH_Init()

# task1 = Task1()
# task2 = Task2()

# scheduler.SCH_Add_Task(task1.Task1_Run, 1000,2000)
# scheduler.SCH_Add_Task(task2.Task2_Run, 2000,4000)

# while True:
#     scheduler.SCH_Update()
#     scheduler.SCH_Dispatch_Tasks()
#     time.sleep(1)