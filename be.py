import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=8,pin_e=22,pins_data=[38,24,23,18],numbering_mode=GPIO.BOARD,cols=16,rows=2,dotsize=8,auto_linebreaks=True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
GPIO.setup(35, GPIO.IN)         #Read output from PIR motion sensor
i=0
j=0
cnt=0
GPIO.output(3, 0) 
i=GPIO.input(11)
j=GPIO.input(35)

while True:
    i=GPIO.input(11)
    j=GPIO.input(35)
   
    if i==1:
        cnt=cnt+1
        print "led on"
        print "count",cnt
        GPIO.output(3, 1)
        while i==1: 
           i=GPIO.input(11)
           GPIO.output(3, 1)
        time.sleep(0.3)
        lcd.clear()
        s=str(cnt)
        lcd.write_string('count ')
        lcd.write_string(s)
        time.sleep(2)
       

        
    if j==1:
        if cnt>0:
            cnt=cnt-1
            print "Exited"
            print "count",cnt
            GPIO.output(3, 1)
            while j==1: 
               j=GPIO.input(35)
               GPIO.output(3, 1)    
            time.sleep(0.3)
            lcd.clear()
            s=str(cnt)
            lcd.write_string('count ')
            lcd.write_string(s)
            time.sleep(2)
           
            
          
        
    if cnt==0:  
        print "led off"
        GPIO.output(3, 0)
        lcd.clear()
        lcd.write_string('Light off ')
        time.sleep(0.3)
        lcd.clear()
    


