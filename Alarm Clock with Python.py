from datetime import datetime   
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break
                    
""" For this task, I will be using the DateTime module in Python to create an alarm clock and the sound library in Python to play the alarm sound.
The DateTime module comes preinstalled in the Python programming language so you can easily import it in your program. 
The playsound library can be easily installed by using a pip command; pip install playsound.The user input should be in a format of hours: minutes: and then seconds.
You will start listening to the song as you will reach the time that has been set. 
To test your code set the time 2 or 3 minutes later from the time you are giving the user input. """
