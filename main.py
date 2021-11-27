#@mathew4STAR
#25-09-2021
#READ README.md for details

from selenium import webdriver as wd
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datascraper as ds
from datetime import datetime as dt 

startloc = input("Input where you want to go to: ")
endloc = input("Input your current location: ")
timee = input("When do you need to reach the location: ")
now = dt.now()

search_path = '/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]'
directions_path = '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button'
starting_point_path = '/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input'
details_path = '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[3]/div[4]/button/span'
locations_path = '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div/div/div[1]/div/div[2]/div[3]/div[1]/div[2]/div/div/div/div/div[1]/div[2]'
location_path_2 = '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div/div/div[1]/div/div[2]/div[3]/div[1]/div[2]/div'
first_add_path = '/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div'

opts = Options()
opts.add_argument('--headless')
driver = wd.Chrome("C:\\Program Files (x86)\\chromedriver.exe", chrome_options=opts)
driver.maximize_window()
driver.get("https://maps.google.com")
time.sleep(5)
search = driver.find_element_by_xpath(search_path)
search.send_keys(startloc)
time.sleep(2)
first_add = driver.find_element_by_xpath(first_add_path)
first_add.click()
time.sleep(4)
directions = driver.find_element_by_xpath(directions_path)
directions.click()
time.sleep(3)
starting_point = driver.find_element_by_xpath(starting_point_path)
starting_point.send_keys(endloc)
starting_point.send_keys(Keys.ENTER)
time.sleep(3)
details = driver.find_element_by_xpath(details_path)
details.click()
time.sleep(5)
location = driver.find_element_by_xpath(location_path_2)
data = location.text
#print(data)

data = data.split()

intersection = None
if ("Dorchester" in data) and ("Huron" in data):
    intersection = 1
elif ("Totten" in data) and ("Huron" in data):
    intersection = 2
elif ("Malden" in data) and ("Huron" in data):
    intersection = 3
else:
    print("Sorry, Data Unavailable")
    exit()

#print(intersection)

endhour = int(timee.split(":")[0])
endminute = int(timee.split(":")[1])
if endminute == 0:
    endminute = 50
    endhour = endhour - 1
else:
    endminute = endminute - 10
starthour = endhour - 1
if len(str(starthour)) == 1:
    starthour = "0" + str(starthour)
if len(str(endhour)) == 1:
    endhour = "0" + str(endhour)
finalstarttime = str(starthour) + ":00"
print("--------------------")
finalendtime = str(endhour)  + ":" + str(endminute)
print("Time from:" + finalstarttime)
print("To:" + finalendtime)

year = now.year
month = now.month
day = now.day

date1 = str(month) + "/" + str(day - 1) + "/" + str(year)
date2 = str(month) + "/" + str(day - 2) + "/" + str(year)
date3 = str(month) + "/" + str(day - 3) + "/" + str(year)

data1 = ds.data(date1, finalstarttime, finalendtime, intersection)
data2 = ds.data(date2, finalstarttime, finalendtime, intersection)
data3 = ds.data(date3, finalstarttime, finalendtime, intersection)

runner1 = 0
runner2 = 0
runner3 = 0
quan = []
quann = []
quannn = []
timestamps = []
timestampss = []
timestampsss = []
data1 = data1.split()
data2 = data2.split()
data3 = data3.split()

ts = '"timeStamp":'
qty = '"qty":'
for i in data1:
    runner1 += 1
    if i == ts:
        timestamps.append(data1[runner1])

    if i == qty:
        qty = data1[runner1]
        qty = qty.strip(",")
        #print(qty)
        quan.append(qty)

for i in data2:
    runner2 += 1
    if i == ts:
        timestampss.append(data2[runner2])

    if i == qty:
        qty = data2[runner2]
        qty = qty.strip(",")
        #print(qty)
        quann.append(qty)

for i in data3:
    runner3 += 1
    if i == ts:
        timestampsss.append(data3[runner3])

    if i == qty:
        qty = data3[runner3]
        qty = qty.strip(",")
        #print(qty)
        quannn.append(qty)


one = max(quan)
two = max(quann)
three = max(quannn)
finalval = [one, two, three]
final = max(finalval)
finalindex = finalval.index(final)
if finalindex == 0:
    index = quan.index(one)
    timey = timestamps[index]
if finalindex == 1:
    index = quann.index(two)
    timey = timestampss[index]
if finalindex == 2:
    index = quannn.index(three)
    timey = timestampsss[index]
timey = timey.split("T")
timey = timey[1]
print("The best time to leave is", timey)
input("press enter to close")
