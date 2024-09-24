import schedule
import time
import os

def run_url():
    os.system('curl https://jetx.rf.gd/testclc.php')

schedule.every(10).seconds.do(run_url)

while True:
    schedule.run_pending()
    time.sleep(1)
