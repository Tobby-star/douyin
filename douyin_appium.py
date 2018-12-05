import time
import random
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC


def main():
    # 设置驱动配置
    server = 'http://localhost:4723/wd/hub'
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'STF_AL00',
        'appPackage': 'com.ss.android.ugc.aweme',
        'appActivity': '.main.MainActivity',
        # 关闭手机软键盘
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    driver = webdriver.Remote(server, desired_caps)
    wait = WebDriverWait(driver, 60)
    # 同意用户隐私协议,点击
    button_1 = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/q6')))
    button_1.click()
    # 禁止电话权限,点击
    button_2 = wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_deny_button')))
    button_2.click()
    # 禁止位置权限,点击
    button_3 = wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_deny_button')))
    button_3.click()
    time.sleep(2)
    # 向上滑动,进入抖音视频播放页面
    TouchAction(driver).press(x=515, y=1200).move_to(x=515, y=1000).release().perform()
    # 这里需要设置一个较长时间的延迟,因为抖音有引导操作和提示,需等待片刻
    time.sleep(20)
    # 点击抖音"喜欢"处,以此进入登录界面
    TouchAction(driver).press(x=950, y=800).release().perform()
    # 点击密码登录
    button_4 = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/afg')))
    button_4.click()
    # 输入账号
    button_5 = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/ab_')))
    button_5.send_keys('你的账号')
    # 输入密码
    button_6 = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/aes')))
    button_6.send_keys('你的密码')
    time.sleep(2)
    # 因为会跳出软键盘,会遮挡登录按钮,需点击软键盘取消
    TouchAction(driver).press(x=980, y=1850).release().perform()
    time.sleep(2)
    # 点击登录按钮
    button_7 = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/abb')))
    button_7.click()
    time.sleep(2)
    # 登录成功,进入抖音视频界面,点击下方标题栏 "我"
    TouchAction(driver).press(x=990, y=1850).release().perform()
    # 进入个人主页,点击关注处
    button_8 = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/a_7')))
    button_8.click()
    # 进入关注栏,点击第二个关注
    button_9 = wait.until(EC.presence_of_element_located((By.XPATH, '	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]')))
    button_9.click()
    # 进入UP主主页,点击第一个视频
    button_10 = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/aqm')))
    button_10.click()
    # 不断下滑页面,直到底部
    while True:
        TouchAction(driver).press(x=515, y=1247).move_to(x=515, y=1026).release().perform()
        time.sleep(float(random.randint(5, 10)))


if __name__ == '__main__':
    main()
