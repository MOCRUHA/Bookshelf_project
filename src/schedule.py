import os
import time

import schedule

#runs once a day the program main.py
def scan():
    print('Scanning...')
    os.exec('python3 main.py')

def once_a_day():
    schedule.every().day.at('05:00').do(scan)

    while True:
        schedule.run_pending()
        time.sleep(1)    

if __name__ == '__main__':
	once_a_day()
