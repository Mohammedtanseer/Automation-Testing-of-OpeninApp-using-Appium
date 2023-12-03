from appium import webdriver
import time
desired_cap = {
    "platformName": "Android",
    "deviceName": "6e1c6a6d",
    "appPackage": "com.instagram.android",
    "appActivity": "com.instagram.mainactivity.InstagramMainActivity"
}
webdriver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
webdriver.find_element_by_id('com.instagram.android:id/tab_avatar').click()
start_time = time.time()
webdriver.find_element_by_id('com.instagram.android:id/text_1').click()
webdriver.find_element_by_id('android:id/button1').click()
end_time = time.time()
redirection_time = end_time - start_time
print(f"Redirection Time: {redirection_time} seconds")