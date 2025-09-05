import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)

#Первый тест
# http://testshop.qa-practice.com/
#
# откройте первый (Customizable Desk) товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Нажмите на кнопку Add to Cart
# В открывшемся попапе нажмите Continue shopping
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли


def test_add_product_to_cart(driver):
    driver.get('http://testshop.qa-practice.com/')
    product_element = driver.find_element(By.XPATH, "//img[@alt='Customizable Desk']")
    product_name = product_element.text

    # open product in new tab
    ActionChains(driver).key_down(Keys.CONTROL).click(product_element).key_up(Keys.CONTROL).perform()

    #switch to new tab
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # add product to cart
    add_to_cart_btn = driver.find_element(By.ID, "add_to_cart")
    add_to_cart_btn.click()

    #continue shopping

    # wait for the modal
    continue_shopping_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[span[normalize-space()='Continue Shopping']]"))
    )
    continue_shopping_btn.click()

    # close tab with product
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.refresh()

    #open cart from main tab
    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/shop/cart' and @aria-label='eCommerce cart']"))
    )
    cart_link.click()

    #check that the product in the cart
    cart_product_title_elem = driver.find_element(By.XPATH, "//h6[contains(@class,'fw-bold')]")
    cart_product_title = cart_product_title_elem.text
    print(cart_product_title)  # "Customizable Desk (Steel, White)"
    assert product_name in cart_product_title, f"Expected '{product_name}' to be in '{cart_product_title}'"


# Второй тест
# https://magento.softwaretestingboard.com/gear/bags.html Навести мышку на первый товар -> кликнуть внизу карточки товара
# на кнопку Add to compare -> Проверить, что товар появился слева на этой же странице в секции Compare Products

# 503 Service Unavailable





