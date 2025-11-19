import jetFunctions as j
from time import sleep
from datetime import datetime

dt = datetime.now()
print("- Jet Lab")
print("- Date: ", dt)
with open(str(dt)+"_110мм.csv", "w") as file:
    file.write("- Jet Lab\n")
    file.write("- Date: "+ str(dt)+"\n")
    try:
        j.initSpiAdc()
        j.initStepMotorGpio()
        for i in range(600):
            sleep(0.1)
            mes = j.getAdc()
            print(mes)
            file.write(str(mes)+";"+str(i*2-600)+"\n")
            j.stepForward(2)

    finally:
        j.deinitSpiAdc()
        j.deinitStepMotorGpio()