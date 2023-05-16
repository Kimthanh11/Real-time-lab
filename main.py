from task1 import *
from task2 import *
from scheduler import *

schedule = Scheduler()
Scheduler.SCH_Init()

task1 = Task1()
task2 = Task2()

task1.Task1_Run()
task2.Task2_Run()