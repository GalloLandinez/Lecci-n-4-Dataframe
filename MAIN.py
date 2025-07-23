import pandas as pd 
import pywhatkit as pyw 
import time 
from datetime import datetime 
now = datetime.now() 
future_minute = now.minute + 2 
future_hour = now.hour 
phone=pd.read_excel("DATOS_CEL.xlsx") 
waiting_time_to_send = 30 

    

close_tab = True 
waiting_time_to_close = 2 
 
for i in range(len(phone)): 
    telefono=f"+57{phone.loc[i,"NUMBERS"].astype(str)}" 
     
    nombre=phone.loc[i,"NAME"] 
    
    msmchat=f"cod {nombre} Buen día, este es un mensaje de prueba de Python" #mensaje que llega al whatsapp
    time_hour = future_hour 
    time_minute = future_minute 
    pyw.sendwhatmsg(telefono, msmchat, time_hour, time_minute, waiting_time_to_send,  
                    close_tab) 
 
    time.sleep(20) 
         
    # Actualizar hora para el próximo mensaje (+1 minuto) 
    future_minute += 1 
    if future_minute >= 60: 
            future_minute = 0 
            future_hour += 1 

           