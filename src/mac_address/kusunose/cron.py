import subprocess
import schedule
import time
from estimation import main 

def job():
    main()

schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)