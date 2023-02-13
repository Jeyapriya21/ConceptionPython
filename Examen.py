import datetime
import threading
import time
stop_thread = False 
global_fifo_tank1 = []
global_fifo_pump1 = []
global_fifo_pump2 = []
list_pump1 = []
list_pump2 = []

class my_task(threading.Thread):
   name = None
   period = None
   execution_time = None
   ###########################################################
   def __int__(self,name, period, execution_time,tank_write=False):
       self.name = name
       self.period = period
       self.execution_time = execution_time
       self.tank_write = tank_write 

       threading.Thread.__int__(self)
    ##################################################################
   def run(self):
        while len(global_fifo_tank1) <= 50:
            if len(list_pump1) <= 10: 
                print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + "pump 1")
                list_pump1.append(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + "pump 1")
                global_fifo_tank1.append(list_pump1)
            else:
               if len(list_pump2) <= 20:
                   print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + "pump 2")
                   list_pump2.append(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + "pump 2")
                   global_fifo_tank1.append(list_pump2)
            if len(global_fifo_tank1) >= 5 and len(global_fifo_pump2) <=4 * len(global_fifo_pump1):
                   print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + "machine 2, fabrication de rou")
                   global_fifo_pump2.append(datetime.datetime.now().strftime("%H:%M:/S") + "\t" + "fabrication de rou")
                   print(global_fifo_pump2)
                   print("stock de rou", len(global_fifo_pump2))

            elif len(global_fifo_tank1) >= 25 and len(global_fifo_pump2) >=4 * len(global_fifo_pump1):
                print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + "machine 2, fabrication de moteur")
                global_fifo_pump1.append(datetime.datetime.now().strftime("%H:%M:/S") + "\t" + "moteur")
                print(global_fifo_pump1)
                print("stock de moteur", len(global_fifo_pump1))

            time.sleep(self.execution_time)
            print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + "stopping task")
            time.sleep(self.period - self.execution_time)

if __name__== '__main__' :
    task_list=[]
    task_list.append(my_task(name="pump1",period=5, execution_time=2,tank_write=True))
    task_list.append(my_task(name="pump2",period=15, execution_time=3, tank_write=True))
    task_list.append(my_task(name="machine1", period=5, execution_time=5))
    task_list.append(my_task(name="machine2", period=5, execution_time=3))

    for current_task in task_list:
        print("*****", current_task, "*****")
        current_task.start()



                





