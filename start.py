import time
import csv
import psutil
from pygetwindow import getActiveWindow
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_active_window_process():
    active_window = getActiveWindow()
    if active_window is not None:
        pid = active_window._hWnd
        process = psutil.Process(pid)
        return process
    return None

def get_active_webpage_url(process):
    if process.name().lower() in ['chrome.exe', 'firefox.exe', 'msedge.exe']:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.switch_to.window(driver.window_handles[-1])
        url = driver.current_url
        driver.quit()
        return url
    return None

def write_to_csv(timestamp, application, webpage):
    with open('activity_log.csv', 'a', newline='') as csvfile:
        fieldnames = ['timestamp', 'application', 'webpage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'timestamp': timestamp, 'application': application, 'webpage': webpage})


start_time = time.time()

while time.time() - start_time < 300:
    process = get_active_window_process()
    if process:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        application = process.name()
        print(f"{timestamp}: Active application: {application}")
        url = get_active_webpage_url(process)
        if url:
            print(f"{timestamp}: Active webpage: {url}")
        else:
            url = "N/A"
        write_to_csv(timestamp, application, url)
    time.sleep(5)