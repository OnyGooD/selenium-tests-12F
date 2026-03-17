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

def second_room(driver):
    driver.implicitly_wait(5)
    gen_table_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button[1]')
    while(True):
        try:
            gen_table_btn.click()
        except:
            break
    
    text_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button')
    text_btn.click()

def third_room(driver):
    driver.implicitly_wait(5)
    
    number_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/input')
    tipp_btn = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/button')
    for i in range(0, 100): 
            number_input.send_keys(i)
            tipp_btn.click()
            number_input.clear()
            result_h2 = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/h2').get_attribute('textContent')
            if '✅' in result_h2.get_attribute("textContent"):
                break
            number_input.clear()
                
    tovabb_btn = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/a')
    tovabb_btn.click()