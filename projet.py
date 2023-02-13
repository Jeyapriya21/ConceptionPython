import datetime
import time
import threading


stop_thread = False
global_tank = []
machine = []

################################################################################

class my_task(threading.Thread):

    name = None
    period = None
    execution_time = None

    ############################################################################

    def __init__(self, name, period, execution_time, tank_write=False, stock_write=False):

        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.tank_write = tank_write
        self.stock_write = stock_write

        threading.Thread.__init__(self)

        ############################################################################
    # def run(self):

    #     global global_tank
    #     global machine

    #     while (not stop_thread):

    #         print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : Starting task")

    #         if (self.tank_write == True):

    #             global_tank.append(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : reading : " + datetime.datetime.now().strftime("%H:%M:%S"))

    #         else:
    #             while (len(global_tank) <= 50):
    #                 print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : " + global_tank[0])
    #                 del global_tank[0]

    #         time.sleep(self.execution_time)
    #         print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : waiting")
    #         time.sleep(self.period - self.execution_time)

# """"""""


def run(self):
    global global_tank
    global machine

    while (not stop_thread):
        print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : Starting task")

        if (self.tank_write == True):
            global_tank.append(datetime.datetime.now().strftime( "%H:%M:%S") + "\t" + self.name + " : reading : " + datetime.datetime.now().strftime("%H:%M:%S"))
            if (len(global_tank) >= 50):
                # pump have a low priority
                for i in range(len(machine)):
                  if (machine[i].name == 'Pump1' or machine[i].name == 'Pump2'):
                      machine[i].execution_time = self.execution_time

            if (len(global_tank) < 50):
                #wheels / 4 > motors
                if (len(global_tank) / 4 > len(machine)):
                  for i in range(len(machine)):
                    if (machine[i].name == 'Machine1'):
                        machine[i].execution_time = self.execution_time

               #wheels / 4 < motors
            elif (len(global_tank) / 4 < len(machine)):
                for i in range(len(machine)):
                    if (machine[i].name == 'Machine2'):
                        machine[i].execution_time = self.execution_time
        else:
          global_tank.append(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : blocked : " + datetime.datetime.now().strftime("%H:%M:%S"))

        # time.sleep(1)
        time.sleep(self.execution_time)
        print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : waiting")
        time.sleep(self.period - self.execution_time)


####################################################################################################
if __name__ == '__main__':

    task_list = []

    # Instanciation of task objects

    task_list.append(my_task(name="pump1", period=5, execution_time=2, tank_write=True))
    task_list.append(my_task(name="pump2", period=15, execution_time=3,  tank_write=True))
    task_list.append(my_task(name="machine1", period=5, execution_time=5, stock_write=True))
    task_list.append(my_task(name="machine2", period=5, execution_time=3, stock_write=True))

    for current_task in task_list:
        current_task.start()
