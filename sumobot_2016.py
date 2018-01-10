def Reverse_Conditional():
    i=0
    for i in range(0,10000): #Reverse while checking back light
        lightB=Sensor(IN_2) #update back sensor

        if ((lightB > 45) or(Sensor(IN_3))): #stop if back sensor hits white!
            break


    

def main():
    
    LEFT_LIGHT = IN_1
    RIGHT_LIGHT = IN_4

    BACK_LIGHT = IN_2

    BACK_TOUCH = IN_3
    
    LIGHT_VALUE = 45

    LEFT_MOTOR = OUT_A
    RIGHT_MOTOR = OUT_C
    
    SetSensor(LEFT_LIGHT, SENSOR_LIGHT)
    SetSensor(RIGHT_LIGHT, SENSOR_LIGHT)
    SetSensor(BACK_LIGHT, SENSOR_LIGHT)
    SetSensor(BACK_TOUCH, SENSOR_TOUCH)
    

    SetSensorTouch(BACK_TOUCH)
    SetSensorLight(LEFT_LIGHT)
    SetSensorLight(RIGHT_LIGHT)
    SetSensorLight(BACK_LIGHT)
    
    leftwhite = False
    rightwhite = False
    backwhite = False
    i=0

    
    PlayTone(440.00,150)
    Wait(300)
    PlayTone(349.23,150)
    Wait(300)
    PlayTone(329.63,300)
    Wait(450)
    PlayTone(329.63,75)
    Wait(150)
    PlayTone(349.23,75)
    Wait(150)
    PlayTone(329.63,75)
    Wait(150)
    PlayTone(349.23,75)
    Wait(150)
    PlayTone(329.63,75)
    Wait(150)
    PlayTone(349.23,75)
    Wait(150)
    PlayTone(329.63,75)
    Wait(150)
    PlayTone(349.23,75)
    Wait(150)
    PlayTone(440.00,150)
    Wait(300)

    while(1):
            lightL=Sensor(LEFT_LIGHT)
            lightR=Sensor(RIGHT_LIGHT)    
            lightB=Sensor(BACK_LIGHT)    
            touch=Sensor(BACK_TOUCH)    
            
            if(lightL > LIGHT_VALUE):
                leftwhite = True
            else:
                leftwhite = False
                
            if(lightR > LIGHT_VALUE):
                rightwhite = True
            else:
                rightwhite = False
                
            if(lightB > LIGHT_VALUE):
                backwhite = True
            else:
                backwhite = False

            if(backwhite):
                #This code is the safety net from the touch sensor. has priority, so won't fall over the edge
                OnRev(OUT_AC, 100)

                while(1):
                    #continue updating light sensors while reversing
                    lightL=Sensor(LEFT_LIGHT)
                    lightR=Sensor(RIGHT_LIGHT)

                    if (lightL > LIGHT_VALUE or lightR > LIGHT_VALUE): 
                        break
                        #stop if light sensors hit white!
                        #will run proper procedure next iteration of main while loop
            elif(touch):
                OnRev(OUT_AC, -100)
            elif(leftwhite and not(rightwhite)):
                OnRev(OUT_AC, -100)
                
                Reverse_Conditional()
                
                if (not(Sensor(BACK_TOUCH))): #stop if back sensor hits white!
                    OnRev(OUT_A, 100) #Stationary turn to the right
                    OnRev(OUT_C, -100)
                    Wait(500)

            elif(not(leftwhite) and rightwhite):
                OnRev(OUT_AC, -100)
                
                Reverse_Conditional()
                
                
                if (not(Sensor(BACK_TOUCH))): #stop if back sensor hits white!
                    OnRev(OUT_A, -100) #Stationary turn to the left
                    OnRev(OUT_C, 100)
                    Wait(500)

            else:
                OnRev(OUT_AC, 100)