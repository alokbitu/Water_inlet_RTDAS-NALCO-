import time
import numpy as np

# temp_discharge = 0

def dis_cal():
       filename2 = 'total_discharge.txt'
       total_discharge = np.loadtxt(filename2, delimiter=',', dtype=float)
       temp_discharge = total_discharge
       while True:
        #timenow = time.localtime()
        filename = 'current_discharge.txt'
        discharge = np.loadtxt(filename, delimiter=',', dtype=float)
        #print(discharge)
        current_discharge = discharge/60
        #print("current discharge is:" + str(current_discharge))
        total_discharge = temp_discharge + current_discharge
        if total_discharge > 99999999:
          total_discharge = 0
          temp_discharge = total_discharge
        else:
         pass
        print("Total discharge is:" + str(total_discharge))
        temp_discharge = total_discharge
        #print(temp_discharge)

        file2 = open("total_discharge.txt", "w+")
        file2.write(str(round(total_discharge,2)))
        file2.close()

        time.sleep(60)

def main():
 dis_cal()

main()

