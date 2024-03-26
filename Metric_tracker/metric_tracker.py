import time
from selenium import webdriver
import collections
import csv

def writeToCSV(filename : str, metrics : dict):
    with open(file=filename, mode="w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=metrics[0].keys())

        writer.writeheader()

        for metric in metrics:
            writer.writerow(metric)


def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")

    metrics = []
    # Track presence time 
    SAMPLE_SIZE = 10
    count = 0
    start_time = time.time()
    while count < SAMPLE_SIZE:
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
    
        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")  
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")

        metrics.append({"TIMESTAMP (HH:MM:SS)": time.strftime("%H:%M:%S", time.localtime(current_time)),
                        "Presence time (Seconds)" : presence_time,
                        "Scrolling (Pixels)" : current_scroll/scroll_height})
    
        count += 1
        time.sleep(2) 

    driver.quit()
    print(metrics)
    writeToCSV("metrics.csv", metrics)

if  __name__ == "__main__":
    main()