import datetime
import time

def display_clock():
    while True:
    
        print("\033c", end="")
        
        # Odoo tsag
        current_time = datetime.datetime.now()
        
        # Tsagiin formatiig haruulah (HH:MM:SS)
        formatted_time = current_time.strftime("%H:%M:%S")
        
        # Tsagiig print hiih
        print("Current Time:", formatted_time)
        
        # 1 sekund huleeh
        time.sleep(1)

# Tsagiin programmig ehluuleh
display_clock()
