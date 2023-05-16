from task1 import *
from task2 import *
from scheduler import *

schedule = Scheduler()
schedule.SCH_Init()

task1 = Task1()
task2 = Task2()

schedule.SCH_Add_Task(task1.Task1_Run, 1000, 50000)
schedule.SCH_Add_Task(task2.Task2_Run, 2000, 60000)


while True:
    schedule.SCH_Update()
    schedule.SCH_Dispatch_Tasks()

