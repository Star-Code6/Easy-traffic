from selenium import webdriver as wd
import time
from selenium.webdriver.chrome.options import Options


traffic_path  = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div/span[1]'
tryit_path =  '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[2]/div[1]/div[2]/button'
date_path = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/input'
intersection_path = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/select'
option_1_path = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/select/option[2]'
option_2_path = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/select/option[3]'
option_3_path = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/select/option[4]'
start_time_path = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/input'
end_time_path = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/input'
execute_path = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[3]/button'
data_path = '/html/body/div/div/div[2]/div[3]/section/div/span[2]/div/div/span/div/div[2]/div/div[4]/div[2]/div/div/table/tbody/tr/td[2]/div[1]/div/pre'


opts = Options()
opts.add_argument('--headless')

def data(d, stime, etime, inter):
    driver = wd.Chrome("C:\\Program Files (x86)\\chromedriver.exe", chrome_options= opts)
    driver.maximize_window()
    driver.get("https://opendata.citywindsor.ca/swagger/index.html")
    time.sleep(4)
    traffic = driver.find_element_by_xpath(traffic_path)
    traffic.click()
    time.sleep(2)
    tryit = driver.find_element_by_xpath(tryit_path)
    tryit.click()
    date = driver.find_element_by_xpath(date_path)
    date.send_keys(d)
    intersection = driver.find_element_by_xpath(intersection_path)
    intersection.click()
    if inter == 1:
        option_path = option_1_path
    if inter == 2:
        option_path = option_2_path
    if inter == 3:
        option_path = option_3_path
    option = driver.find_element_by_xpath(option_path)
    option.click()
    start_time = driver.find_element_by_xpath(start_time_path)
    start_time.send_keys(stime)
    end_time = driver.find_element_by_xpath(end_time_path)
    end_time.send_keys(etime)
    execute = driver.find_element_by_xpath(execute_path)
    execute.click()
    time.sleep(5)
    data = driver.find_element_by_xpath(data_path)
    final_data = data.text
    return final_data
if __name__ == "__main__":
    print("Running program with sample data")
    samp_data = ["1/1/2021", "13:00", "14:00", 1]
    data(samp_data[0], samp_data[1], samp_data[2], samp_data[3])
