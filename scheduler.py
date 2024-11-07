import schedule
import time
import subprocess

def job():
    """Job to run the main script."""
    print("Running the main script...")
    subprocess.run(['python', 'main.py', '1'])

schedule.every(50).seconds.do(job)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)
