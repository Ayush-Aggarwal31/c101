num=int(input("Enter a number of seconds tocountdown from : "))
import time
from playsound import playsound
def countdown(num):
    while(num>0):
        mins=int(num/60)
        secs=int(num%60)
        if(mins<=9):
            timer=f'0{mins}:{secs}'
            if(secs<=9):
                timer=f'0{mins}:0{secs}'
        elif(secs>9 and mins>9):
            timer=f'{mins}:{secs}'
        elif(mins<=9):
            timer=f'0{mins}:{secs}'
        elif(secs<=9 or mins<=9):
            timer=f'0{mins}:0{secs}'
        print(timer)
        time.sleep(1)
        num-=1
    print("Time's Up!")
    playsound('C:/Users/ayush/OneDrive/Desktop/Python/c101/buzzer.wav')
countdown(num)
