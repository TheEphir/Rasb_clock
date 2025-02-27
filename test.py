from datetime import datetime
 
current_time = datetime.now().strftime("%H:%M:%S")

if int(current_time[:2]) > 15:
    print(True)
    
