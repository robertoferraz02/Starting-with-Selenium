from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.wait = WebDriverWait(driver, 30)

driver.get('http://cesar.org.br')

firststep = driver.wait.until(EC. visibility_of_element_located((By.XPATH, '//*[@id="content"]/section[2]/div/div/div/div[4]/a/div/div/h3')))
firststep.click()

for handle in driver.window_handles:
    driver.switch_to.window(handle)

pesquisar = driver.find_element_by_css_selector('div#content nav > a > i').click()
escrever = driver.wait.until(EC.visibility_of_element_located((By.ID, 'search')))
escrever.send_keys('aulas')
ir = driver.find_element_by_css_selector('div#content input[type="submit"]:nth-child(2)').click()

sleep(10)

driver.quit()

print('TESTE REALIZADO COM SUCESSO')