from appium import webdriver
desired_cap = {
    "platformName": "Android",
    "deviceName": "6e1c6a6d",
    "appPackage": "com.instagram.android",
    "appActivity": "com.instagram.mainactivity.InstagramMainActivity"
}
# Creating a Smart Link for YouTube
webdriver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
webdriver.find_element_by_id("com.instagram.android:id/tab_avatar").click()
webdriver.find_element('By.XPATH,//android.widget.TextView[@text="Edit profile"]').click()
webdriver.find_element(
    'By.XPATH,//android.widget.LinearLayout[@content-desc="Links, 1"]/android.widget.LinearLayout[1]').click()
webdriver.find_element(
    'By.XPATH,//androidx.recyclerview.widget.RecyclerView[@resource-id="com.instagram.android:id/links_list"]/android.view.ViewGroup[1]').click()
webdriver.find_element(
    'By.XPATH,//android.widget.FrameLayout[@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.LinearLayout').click()
webdriver.find_element(
    'By.XPATH,(//android.view.ViewGroup[@resource-id="com.instagram.android:id/prism_form_field_container"])[1]/android.widget.EditText').send_keys(
    'CopiedText.click()')