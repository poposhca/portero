import RPi.GPIO as GPIO
import time

class KeyBoardReader:
    
    def __init__(self):
            GPIO.setmode(GPIO.BOARD)
            self.MATRIX= [[1,2,3,'A'],
                     [4,5,6,'B'],
                     [7,8,9,'C'],
                 ['*',0,'#','D']]
            self.ROW = [7,11,13,15]
            self.COL = [12,16,18]

            for j in range(3):
                GPIO.setup(self.COL[j],GPIO.OUT)
                GPIO.output(self.COL[j],1)
            for i in range(4):
                GPIO.setup(self.ROW[i],GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def raedInput(self):
            try:
                while(True):
                    for j in range(3):
                        GPIO.output(self.COL[j],0)
                        for i in range(4):
                            if GPIO.input(self.ROW[i])==0:
                                return self.MATRIX[i][j]
                                time.sleep(0.2)
                                while(GPIO.input(self.ROW[i])==0):
                                    pass
                        GPIO.output(self.COL[j],1)
            except KeyboardInterrupt:
                GPIO.cleanup()

     
