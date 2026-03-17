from selenium.webdriver.common.by import By

def first_room(driver):

    username_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/input[1]')
    username_input.send_keys('admin')

    password_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/input[2]')
    passwrod_p = driver.find_element(By.CSS_SELECTOR, '#root > main > div.flip-card > div > div.flip-card-back > p:nth-child(3)')
    pwd = passwrod_p.get_attribute('textContent')
    password_input.send_keys(pwd)

    login_btn = driver.find_element(By.TAG_NAME, 'button')
    login_btn.click()

    print('Első szoba kész!')