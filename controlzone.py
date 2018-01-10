def main():
    SetSensor(IN_1, SENSOR_LIGHT)  #right
    SetSensorLight(IN_1)       
    SetSensor(IN_4, SENSOR_LIGHT) #left
    SetSensorLight(IN_4)       
    SetSensorLowspeed(IN_2)       

    left_mode = 1

    left_lock = 1

    lock_on = 0

    center_area = 1

    park = 1

    center_mode = 0


   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                #
   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Wait(2000) #2 Second Wait
    OnFwd (OUT_AC,100)

    Wait(1100) #3 Seconds Forwards
    OnFwd (OUT_A,50)
    OnRev (OUT_C,50)
    Wait(600) #Turn to face center)
    OnFwd (OUT_AC,0)
    Wait(2000) #2 Second Wait
    OnFwd (OUT_AC,100)

    Wait(300) #Turn to face center

    while(Sensor(IN_1)  <50 and Sensor(IN_4)  <50):
   
        OnFwd (OUT_AC,100)
    while(Sensor(IN_1)  <50 or Sensor(IN_4)  <50):

        if (Sensor(IN_1)  > 50 and Sensor(IN_4)  < 50):     #silver on right only
            OnRev(OUT_C,50) 
            OnRev(OUT_A,80)  
        elif (Sensor(IN_4)  > 50 and Sensor(IN_1)  < 50):     #silver on left only
            OnRev(OUT_C,80) 
            OnRev(OUT_A,50)  
        else:
            OnFwd (OUT_AC,100)

    if(SensorUS(IN_2)<20):
        center_mode = 1

        OnFwd (OUT_AC,100)
        Wait(300)
    else:
        OnRev (OUT_AC,100)
        Wait(500)
        OnRev(OUT_C,50) 
        OnFwd(OUT_A,50)  
        Wait(500)

        while(Sensor(IN_1)  <50 and Sensor(IN_4)  <50):   
            OnFwd (OUT_AC,100)

        if(Sensor(IN_4)  > 50):

            left_lock = 0

        else:

            left_lock = 1
        OnRev (OUT_AC,100)
        Wait(500)

   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   #   Phase 2   #
 
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
                           
    while(1):
        if(park==3):
            break
        elif(Sensor(IN_1)  <50 and Sensor(IN_4)  <50):      #move forwards if on black
            if(left_lock==1):
                OnFwd (OUT_A,60)
                OnFwd (OUT_C,30)
            else:
                OnFwd (OUT_A,30)
                OnFwd (OUT_C,60)
        elif (Sensor(IN_1)  > 75 and Sensor(IN_4)  > 75):     #silver
            if(center_mode == 1):
                while(1):
                    OnFwd (OUT_AC,60)
                    Wait(200)
                    if (SensorUS(IN_2)<25):
                        OnFwd (OUT_AC,60)
                    if (Sensor(IN_1)  < 50 and Sensor(IN_4)  < 50):
                        while(Sensor(IN_1)  < 75 or Sensor(IN_4)  < 75):
                            OnRev (OUT_AC,60)
                        Wait(400)    
                        park = 3
                        OnFwd (OUT_AC,0)
                        break
            else:
                while(1):
                    OnFwd (OUT_AC,60)
                    Wait(200)
                    while(1):
                        if (SensorUS(IN_2)<25):
                            OnFwd (OUT_AC,60)
                        if (Sensor(IN_1)  < 75 and Sensor(IN_4)  < 75):
                                OnRev (OUT_AC,60)
                                Wait(700)    
                                park = 3
                                OnFwd (OUT_AC,0)
                                break
            OnFwd (OUT_AC,30)
        elif (Sensor(IN_1)  > 75 and Sensor(IN_4)  < 50):     #silver on right  black on left
            OnRev(OUT_C,0) 
            OnRev(OUT_A,80)  
            left_mode=0
        elif (Sensor(IN_4)  > 75 and Sensor(IN_1)  < 50):     #silver on left black on right
            OnRev(OUT_C,80) 
            OnRev(OUT_A,0)  
            left_mode=1
        elif (Sensor(IN_1)  > 75 and Sensor(IN_4)  < 75):     #silver on right grey on left
            OnRev(OUT_C,0) 
            OnRev(OUT_A,80)  
            left_mode=0
        elif (Sensor(IN_4)  > 75 and Sensor(IN_1)  < 75):     #silver on left grey on right
            OnRev(OUT_C,80) 
            OnRev(OUT_A,0)  
            left_mode=1
        elif (Sensor(IN_1)  <50 and Sensor(IN_4)  > 50):     #black on right  grey  on left
            left_lock=0
        elif (Sensor(IN_4)  <  50 and Sensor(IN_1)  > 50):     #black on left grey on right
            left_lock=1
        else:                              #Light on Grey or Black, turn left (in)
            if(left_lock==0):
                OnFwd (OUT_A,60)
                OnFwd (OUT_C,30)
            else:
                OnFwd (OUT_A,30)
                OnFwd (OUT_C,60)