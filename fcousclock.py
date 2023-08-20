import time
import os

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time Up!')

# 设定专注时长，例如25分钟
focus_time = 25 * 60

# 清除屏幕
os.system('cls' if os.name == 'nt' else 'clear')

print("Let's focus for 25 minutes. Don't look at the clock, just work.")
countdown(int(focus_time))
