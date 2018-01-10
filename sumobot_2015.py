#Edgar: Anton and Evan
def main():
    Wait(2000)
    #Light Back
    
    SetSensorLowspeed(IN_1)    #Touch Back
    SetSensor(IN_2, SENSOR_LIGHT)    #Light Back
    
    SetSensor(IN_3, SENSOR_TOUCH)    #Touch Front
    SetSensor(IN_4, SENSOR_LIGHT)    #Light Front
    
    SetSensorLight(IN_2)              
    SetSensorLight(IN_4)     
    
    OnRev(OUT_B ,100)
    OnFwd(OUT_C ,100)
    Wait(1250)
    
    i=0
    while(1):           
    
          
        distanceB=SensorUS(IN_1)
        lightB=Sensor(IN_2)
        touchF=Sensor(IN_3)     
        lightF=Sensor(IN_4)    
        
        
        if (lightF>60):     #Front Light
            #Move Backwards
            OnRev(OUT_A,100)
            OnFwd(OUT_BC,100)
            
            for i in range(0,1450):
                lightB=Sensor(IN_2)
                touchF=Sensor(IN_3)     
                lightF=Sensor(IN_4)    
            
                if(touchF == 1 or lightB > 50): 
                    break #Don't Die
                if (i == 200): #Turn
                    OnRev(OUT_B ,100)
                    OnFwd(OUT_C ,100)
        
        elif (lightB>60):     #Back Light
            #Move Forwards
            OnFwd(OUT_A,100)
            OnRev(OUT_BC,100)
            
            while(1):#for i in range(0,3000): 
                lightB=Sensor(IN_2)
                touchF=Sensor(IN_3)     
                lightF=Sensor(IN_4)    
                if(touchF == 1 or lightF > 50):
                    break #Don't Die
        elif (touchF==1 ): #Push enemies forwards
            OnFwd(OUT_A,100)
            OnRev(OUT_BC,100)
        elif (distanceB<10): #Push enemies backwards
            OnRev(OUT_A,100)
            OnFwd(OUT_BC,100)
        else:
            OnFwd(OUT_A,50) #Turn JFF
            OnRev(OUT_B,50)
            OnFwd(OUT_C ,50)#always rev