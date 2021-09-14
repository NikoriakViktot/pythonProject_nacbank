from selenium import webdriver
import time
from nbu_parcer.parcer_settings import g_url_to_parse
from nbu_parcer.parcer_settings import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select



# url = 'http://hydro.meteo.gov.ua/'
url = g_url_to_parse
driver.get(url=url)

time.sleep(1)
email_input = driver.find_element_by_name("username")
email_input.send_keys("onm85259@zwoho.com")
time.sleep(1)
pasword_input = driver.find_element_by_name("password")
pasword_input.send_keys("OpwP$h^U8t0#")
time.sleep(0.5)
kabinet_buton = driver.find_element_by_name("login").click()
time.sleep(0.5)
driver.refresh()
time.sleep(1)
cooins = driver.get("https://coins.bank.gov.ua")
# shop = driver.get('https://coins.bank.gov.ua/shop')

novi_produktu = driver.find_element_by_id('front-latest')
contener_ptoduct = novi_produktu.find_element_by_xpath('//*[@id="front-latest"]/div[2]')
ul = contener_ptoduct.find_element_by_tag_name('ul')
li = ul.find_elements_by_tag_name('li')
a_link = [a.find_elements_by_tag_name('a') for a in li]
text_a = a_link[0]
print(a_link)
text_a[]
a_link_1 = [a.find_element_by_partial_link_text('Георгій Береговий у футлярі') for a in text_a[3]]



# try:
#     li_1 = li[0].find_element_by_partial_link_text('Георгій Береговий у футлярі').click()
# except Exception as ex:
#     print(ex)
# try:
#     li_1 = li[3].find_element_by_partial_link_text('Георгій Береговий у футлярі').click()
# except Exception as ex:
#     print(ex)


# vubir_kat = Select(driver.find_element_by_name("orderby"))
# vubir_kat.select_by_value('date')
# zwit = driver.find_element_by_name('paged')
# zwit.submit()
# time.sleep(1)
# # wait = WebDriverWait(driver, 10)
# # element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
# # try:
# id_element = driver.find_elements_by_xpath("site-content")
#
# # vsi_tovaru =driver.find_elements_by_xpath("//*[@id="'site-content'"]/div[2]")
# ul_tovar = driver.find_elements_by_xpath('//*[@id="site-content"]/div[2]')
# sp = []
# for iter_tr in ul_tovar:
#     sp.append(iter_tr.find_elements_by_tag_name('li'))
#
# print(sp)
# # except:
#     driver.refresh()
time.sleep(1)
# url_tovar = sp
# print(url_tovar)

# 'Пам`ятна банкнота номіналом 500 гривень зразка 2015 року до 30-річчя незалежності України').click(
# b = li.find_element_by_partial_link_text('Георгій Береговий у футлярі').click()
# poshyk = driver.find_element_by_partial_link_text('Чорнобиль. Відродження. Кінь Пржевальського з нейзильберу у сувенірній упаковці')
# poshyk.click()


kyputu_button = driver.find_element_by_name("add-to-cart").click()
time.sleep(5)
cart = driver.get('https://coins.bank.gov.ua/cart')
time.sleep(5)
scrinshot = driver.get_screenshot_as_png()
oformutb_zamovlenya = driver.get('https://coins.bank.gov.ua/checkout')
# nova_poshta = driver.find_element_by_css_selector('.shipping_methods li')
nova_poshta = driver.find_element_by_id('shipping_method_0_nova_poshta_shipping_method')
nova_poshta.submit()
galochka = driver.find_element_by_id("terms")
# galochka.find_elements_by_class_name("woocommerce-form__label woocommerce-form__label-for-checkbox checkbox")
galochka.submit()

portmone = driver.find_element_by_css_selector('.pg-payment-method__str-card')
namber_car = portmone.find_element_by_class_name('pg-group-input pg-payment-method__str-card__number')
namber_car.send_keys('5685 8564 5666 5555')
time.sleep(1)
rik_cart = portmone.find_element_by_class_name('pg-group-input pg-payment-method__str-card__exp')
rik_cart.send_keys('1212')
time.sleep(1)
id_cart = portmone.find_element_by_class_name("pg-group-input pg-payment-method__str-card__cvv")
id_cart.send_keys('123')
time.sleep(1)
email_cart = portmone.find_element_by_class_name("pg-group-input")
email_cart.send_keys('nikoriakviktor@gmail.com')
time.sleep(1)
oplata = portmone.find_element_by_class_name('pg-group-btn').click()
# kyputu_button.submit()
# from bs4 import BeautifulSoup
# soup_monet = BeautifulSoup(cooins, 'html.parser')
# # url_monet = soup_monet.find_all('a href')
# print(soup_monet)




# vubir_posta = driver.find_element_by_xpath(_class="table_form")


