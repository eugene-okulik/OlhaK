from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.implicitly_wait(6)
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    # sleep(3)

# Задание
# Часть 1
# Напишите программку, которая заходит на вот эту страницу: https://www.qa-practice.com/elements/input/simple, вводит
# какой-то текст в поле, делает submit , а после этого находит элемент, в котором отображается тот текст, который был
# введен и рапечатывает этот текст.


def test_input_text_to_text_field(driver):
    input_data = 'newtext'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data
    print(result_text.text)

# Часть 2
# Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form и полностью заполнит форму
# (кроме загрузки файла) и нажмет Submit.
#
# Небольшая особенность
# Страничка эта немного кривая, иногда реклама перекрывает элементы и по ним невозможно кликнуть (но сейчас, смотрю,
# вообще реклама пропала). Если бы это было приложение, которое мы тестируем, это был бы баг. Но работаем с тем, что есть.
# И для нас это даже плюс, нужно найти как выкрутиться. Обойти это можно уменьшив размер экрана браузера - тогда элементы
# перераспределяются и становятся доступны. Но если реклама так и не появится, то ничего на странице не мешает.
#
# После отправки вам будет отображено окошко с тем что вы ввели. Получите со страницы содержимое этого окошка и
# распечатайте (выведите на экран).


def test_fillin_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')

    # Уменьшаем размер окна браузера
    driver.set_window_size(1024, 768)
    # Максимально увеличиваем экран
    driver.maximize_window()

    # Заполняем текстовые поля
    driver.find_element(By.ID, 'firstName').send_keys('Olha')
    driver.find_element(By.ID, 'lastName').send_keys('Kovanova')
    driver.find_element(By.ID, 'userEmail').send_keys('olalaqa@gmail.com')

    # Выбираем пол
    driver.find_element(By.XPATH, '//label[text()="Female"]').click()

    # Заполняем номер телефона
    driver.find_element(By.ID, 'userNumber').send_keys('0636271677')

    # Работаем с выбором даты
    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()
    driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day--005').click()  # Выбираем 5-е число

    # Заполняем предметы
    subjects = driver.find_element(By.ID, 'subjectsInput')
    subjects.send_keys('Math')
    subjects.send_keys(Keys.ENTER)

    # Выбираем хобби
    driver.find_element(By.XPATH, '//label[text()="Music"]').click()

    # Заполняем адрес
    driver.find_element(By.ID, 'currentAddress').send_keys('Svetlaya 13m')

    # Выбираем штат и город
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Скроллим вниз
    state = driver.find_element(By.ID, 'state')
    state.click()
    driver.find_element(By.XPATH, '//div[text()="NCR"]').click()
    city = driver.find_element(By.ID, 'city')
    city.click()
    driver.find_element(By.XPATH, '//div[text()="Delhi"]').click()

    # Отправляем форму
    submit_btn = driver.find_element(By.ID, 'submit')
    driver.execute_script("arguments[0].click();", submit_btn)  # Используем JavaScript для клика

    # Получаем текст из модального окна
    modal_content = driver.find_element(By.CLASS_NAME, 'modal-content')
    print(modal_content.text)


# Часть 3
# № 1
# Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/select/single_select, выбирает
# какой-нибудь вариант из Choose language, кликает Submit и проверяет, что в окошке с результатом отображается тот
# вариант, который был выбран.

def test_select_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    # Select a language from the dropdown
    dropdown = driver.find_element(By.ID, 'id_choose_language')
    dropdown.click()
    option = driver.find_element(By.CSS_SELECTOR, 'select#id_choose_language option[value="1"]')
    option.click()
    selected_option = option.text

    # Submit the form
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()

    # Verify the selected option is displayed in the result window
    result_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'result-text'))
    )
    assert result_text.text == selected_option
    print(result_text.text)


# № 2
# Напишите тест, который зайдет на страницу https://the-internet.herokuapp.com/dynamic_loading/2, нажмет Start, и
# проверит, что на странице появляется текст "Hello World!"

def test_waite_until_text(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    expected_text = 'Hello World!'

    # Wait until the Start button is clickable and then click it
    start_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#start button'))
    )
    start_btn.click()

    # Wait until the text "Hello World!" is visible in the element and retrieve the element
    result_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'finish'))
    )

    # Verify the text
    assert result_element.text == expected_text
    print(result_element.text)

