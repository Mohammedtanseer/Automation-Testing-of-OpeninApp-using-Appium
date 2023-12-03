from appium import webdriver
import time

# Set up desired capabilities for Appium
desired_cap = {
    "platformName": "Android",
    "deviceName": "6e1c6a6d",
    "appPackage": "com.openinapp",
    "appActivity": "com.openinapp.ui.landing.LandingActivityV2"
}
webdriver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# Smart Link Generator
webdriver.find_element_by_id("com.openinapp:id/btnCreateSmartLink").click()
webdriver.find_element_by_id("com.openinapp:id/et_feed_link").send_keys('https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydmabk-21&ref=pd_sl_7lvdlypdab_e&adgrpid=58666170373&hvpone=&hvptwo=&hvadid=678717150657&hvpos=&hvnetw=g&hvrand=726431556467216006&hvqmt=e&hvdev=m&hvdvcmdl=&hvlocint=&hvlocphy=9062036&hvtargid=kwd-10573980&hydadcr=28228_2379650&gclid=Cj0KCQiAyKurBhD5ARIsALamXaHDOGAmahmJGf1P23KDASIXkEJKqzfLVyIcPrrkwQaxArRXnwdngX0aAlHUEALw_wcB')
webdriver.find_element_by_id("com.openinapp:id/ll_btn_generate_link").click()
webdriver.find_element_by_id("com.openinapp:id/ll_copy_smart_link").click()
