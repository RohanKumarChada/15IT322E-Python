import RPi.GPIO as GPIO
import time

GPIO.setwarnings( False)
GPIO.setmode( GPIO.BCM)

TRIGGER=23
ECHO=24

motor1_input1=21
motor1_input2=20
motor2_input1=10
motor2_input2=9

GPIO.setup( TRIGGER, GPIO.OUT)
GPIO.setup( ECHO, GPIO.IN) 

GPIO.setup( motor1_input1, GPIO.OUT)
GPIO.setup( motor1_input2, GPIO.OUT)
GPIO.setup( motor2_input1, GPIO.OUT)
GPIO.setup( motor2_input2, GPIO.OUT)

def stop() :
  GPIO.output( motor1_input1, 0)
  GPIO.output( motor1_input2, 0)
  GPIO.output( motor2_input1, 0)
  GPIO.output( motor2_input2, 0)
  print ”stopping”

def forward() :
  GPIO.output( motor1_input1, 1)
  GPIO.output( motor1_input2, 0)
  GPIO.output( motor2_input1, 1)
  GPIO.output( motor2_input2, 0)
  print ”going forward”

def back() :
  GPIO.output( motor1_input1, 0)
  GPIO.output( motor1_input2, 1)
  GPIO.output( motor2_input1, 0)
  GPIO.output( motor2_input2, 1)
  print “going backward”

def right() :
  GPIO.output( motor1_input1, 1)
  GPIO.output( motor1_input2, 0)
  GPIO.output( motor2_input1, 0)
  GPIO.output( motor2_input2, 0)
  print “turning right”

def left() :
  GPIO.output( motor1_input1, 0)
  GPIO.output( motor1_input2, 0) 
  GPIO.output( motor2_input1, 1)
  GPIO.output( motor2_input2, 0)
  print “turning left”

def distance() :
  GPIO.output( TRIGGER, True) 
  time.sleep(0.00001)
  GPIO.output( TRIGGER, False) 
  
  StartTime = time.time()
  StopTime = time.time()
  
  while GPIO.input(ECHO)==0 :
      StartTime = time.time()
   
  while GPIO.input(ECHO)==1 :
      StopTime = time.time()

  TimeElapsed = StopTime – StartTime
  
  distance = (TimeElapsed * 34300)/2
  return distance  
  
#------------------------------------------------------------------
If__name__ == ‘__main__’ :

  try:
      count=0
      while True :
            dist= distance()
            print(“Distance = %.1f cm” %dist)
            time.sleep(0.5)

            if dist > 10 :
                forward()
            else :
	        count=count+1
                stop()
                time.sleep(1)
                back()
                time.sleep(1.5)
                if (count%3==1):
                    right()
                else :
                    left()
                time.sleep(1.5)
                stop()
                time.sleep(1)

  
  except KeyboardInterrupt :
       stop() 
       print(“User Interrupt”)
       GPIO.cleanup()
