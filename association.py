import elem as elem
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.maximize_window()

http1 = "www.abc.com"
http2 = "www.def.com"
username = "artur"
password = "qwerty123"

def log_in():
    try:
        driver.get(http1)
        time.sleep(1)
        click_xpath_element('//*[@id="loginMessageOkCancelButton"]')
        elem = driver.find_element_by_id("j_username")
        elem.clear()
        elem.send_keys(username)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_id("j_password")
        elem.clear()
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id('loginPanelSubmitButton')
        elem.click()
    except:
        print "Login"

def click_xpath_element(xpath):
    # And check what was found
    try:
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
        elem = driver.find_element_by_xpath(xpath)
        elem.click()
        time.sleep(1)
    except TimeoutException:
        pass

def main():
    suffix = "_loc"
    friendly_names1 = []
    friendly_names2 = []
    friendly_names3 = []
    friendly_names4 = []

    log_in()
    j = 11295    # starting ID of devices to association
    '''
###################################################################################################
    # association devices to groups loc_1 - loc_9
###################################################################################################
    for i in range(9, 10, 1):
        friendly_name = str(0) + str(0) + str(0) + str(i) + suffix
        friendly_names1.append(friendly_name)

    # go to static groups, find proper group and edit it
    for name in friendly_names1:
        driver.get(http2)
        elem = driver.find_element_by_xpath('//input[@placeholder="Search.."]')
        elem.click()
        elem.send_keys(name)
        elem.send_keys(Keys.RETURN)
        click_xpath_element('//*[@type="checkbox"]')
        time.sleep(1)
        click_xpath_element('//*[@id="gridComponent-grid-edit"]')

        # associate devices with defined ID
        for z in range(1, 6, 1):
            click_xpath_element('//*[@id="userdevicereslist-grid-associate_devices_id"]')
            time.sleep(1)
            elem = driver.find_element_by_xpath('//a[@class="add-on btn dropdown-toggle"]')
            elem.click()
            click_xpath_element('//ul[@class="dropdown-menu pull-right"]')
            click_xpath_element('//*[@id="id30b"]')
            click_xpath_element('//option[@value="criteria.startsWith"]')
            time.sleep(1)
            elem = driver.find_element_by_xpath('//input[@type="text"]')
            elem.click()
            elem.send_keys(j)
            j = j + 1
            time.sleep(1)
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            click_xpath_element('//*[@id="searchPanel-searchPanel-search"]')
            time.sleep(2)
            click_xpath_element('//input[@name="searchPanel:searchPanel-grid:grid:datatable:topToolbars:toolbars:1:headers:14:header:label:selected"]')
            time.sleep(2)
            click_xpath_element('//*[@id="searchPanel-grid-submit_id"]')
            time.sleep(1)

        # submit changes for a static group
        elem = driver.find_element_by_xpath('//*[@id="editor-submit"]')
        elem.click()
        time.sleep(1)
    
###################################################################################################
    # association devices to groups loc_10 - loc_99
###################################################################################################
    for n in range(31, 100, 1):
        friendly_name = str(0) + str(0) + str(n) + suffix
        friendly_names2.append(friendly_name)

    # go to static groups, find proper group and edit it
    for name in friendly_names2:
        driver.get(http2)
        elem = driver.find_element_by_xpath('//input[@placeholder="Search.."]')
        elem.click()
        elem.send_keys(name)
        elem.send_keys(Keys.RETURN)
        click_xpath_element('//*[@type="checkbox"]')
        click_xpath_element('//*[@id="gridComponent-grid-edit"]')
        time.sleep(1)

        # associate devices with defined ID
        for z in range(1, 6, 1):
            click_xpath_element('//*[@id="userdevicereslist-grid-associate_devices_id"]')
            time.sleep(1)
            elem = driver.find_element_by_xpath('//a[@class="add-on btn dropdown-toggle"]')
            elem.click()
            click_xpath_element('//ul[@class="dropdown-menu pull-right"]')
            click_xpath_element('//*[@id="id30b"]')
            click_xpath_element('//option[@value="criteria.startsWith"]')
            time.sleep(1)
            elem = driver.find_element_by_xpath('//input[@type="text"]')
            elem.click()
            elem.send_keys(j)
            j = j + 1
            time.sleep(1)
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            click_xpath_element('//*[@id="searchPanel-searchPanel-search"]')
            time.sleep(2)
            click_xpath_element('//input[@name="searchPanel:searchPanel-grid:grid:datatable:topToolbars:toolbars:1:headers:14:header:label:selected"]')
            time.sleep(2)
            click_xpath_element('//*[@id="searchPanel-grid-submit_id"]')
            time.sleep(1)

        # submit changes for a static group
        elem = driver.find_element_by_xpath('//*[@id="editor-submit"]')
        elem.click()
        time.sleep(1)
    
###################################################################################################
    # association devices to groups loc_100 - loc_999
###################################################################################################
    for m in range(881, 1000, 1):
        friendly_name = str(0) + str(m) + suffix
        friendly_names3.append(friendly_name)

    # go to static groups, find proper group and edit it
    for name in friendly_names3:
        driver.get(http2)
        elem = driver.find_element_by_xpath('//input[@placeholder="Search.."]')
        elem.click()
        elem.send_keys(name)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        click_xpath_element('//*[@type="checkbox"]')
        click_xpath_element('//*[@id="gridComponent-grid-edit"]')
        time.sleep(1)

        # associate devices with defined ID
        for z in range(1, 6, 1):
            click_xpath_element('//*[@id="userdevicereslist-grid-associate_devices_id"]')
            time.sleep(1)
            elem = driver.find_element_by_xpath('//a[@class="add-on btn dropdown-toggle"]')
            elem.click()
            click_xpath_element('//ul[@class="dropdown-menu pull-right"]')
            click_xpath_element('//*[@id="id30b"]')
            click_xpath_element('//option[@value="criteria.startsWith"]')
            time.sleep(1)
            elem = driver.find_element_by_xpath('//input[@type="text"]')
            time.sleep(1)
            elem.click()
            elem.send_keys(j)
            j = j + 1
            time.sleep(1)
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            click_xpath_element('//*[@id="searchPanel-searchPanel-search"]')
            time.sleep(2)
            click_xpath_element('//input[@name="searchPanel:searchPanel-grid:grid:datatable:topToolbars:toolbars:1:headers:14:header:label:selected"]')
            time.sleep(2)
            click_xpath_element('//*[@id="searchPanel-grid-submit_id"]')
            time.sleep(1)

        # submit changes for a static group
        elem = driver.find_element_by_xpath('//*[@id="editor-submit"]')
        elem.click()
        time.sleep(1)
    '''
###################################################################################################
    # association devices to groups loc_1000 - loc_1260
###################################################################################################
    for p in range(1240, 1261, 1):
        friendly_name = str(p) + suffix
        friendly_names4.append(friendly_name)

    # go to static groups, find proper group and edit it
    for name in friendly_names4:
        driver.get(http2)
        elem = driver.find_element_by_xpath('//input[@placeholder="Search.."]')
        elem.click()
        elem.send_keys(name)
        elem.send_keys(Keys.RETURN)
        click_xpath_element('//*[@type="checkbox"]')
        click_xpath_element('//*[@id="gridComponent-grid-edit"]')
        time.sleep(1)

        # associate devices with defined ID
        for z in range(1, 6, 1):
            click_xpath_element('//*[@id="userdevicereslist-grid-associate_devices_id"]')
            time.sleep(1)
            elem = driver.find_element_by_xpath('//a[@class="add-on btn dropdown-toggle"]')
            elem.click()
            click_xpath_element('//ul[@class="dropdown-menu pull-right"]')
            click_xpath_element('//*[@id="id30b"]')
            click_xpath_element('//option[@value="criteria.startsWith"]')
            time.sleep(1)
            elem = driver.find_element_by_xpath('//input[@type="text"]')
            elem.click()
            elem.send_keys(j)
            j = j + 1
            time.sleep(1)
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            click_xpath_element('//*[@id="searchPanel-searchPanel-search"]')
            time.sleep(2)
            click_xpath_element('//input[@name="searchPanel:searchPanel-grid:grid:datatable:topToolbars:toolbars:1:headers:14:header:label:selected"]')
            time.sleep(2)
            click_xpath_element('//*[@id="searchPanel-grid-submit_id"]')
            time.sleep(1)

        # submit changes for a static group
        elem = driver.find_element_by_xpath('//*[@id="editor-submit"]')
        elem.click()
        time.sleep(1)

if __name__ == '__main__':
    main()
