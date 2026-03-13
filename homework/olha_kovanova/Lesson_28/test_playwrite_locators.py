# Задание 1
# get_by_role
# Напишите тест, который заходит на страницу https://the-internet.herokuapp.com/, кликает по ссылке Form Authentication,
# заполняет логин и пароль, кликает кнопку Login
#
# Все элементы должны быть найдены с помощью локатора get_by_role
#
# Задание 2
# Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form и полностью заполнит форму
# (кроме загрузки файла) и нажмет Submit.
# Какие локаторы использовать - выбирайте сами.
import time

from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('Olha')
    page.get_by_role('textbox', name='password').fill('Test')
    page.get_by_role('button', name='Login').click()


def test_fill_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_placeholder('First Name').fill('Olga')
    page.get_by_placeholder('Last Name').fill('Zayka')
    page.get_by_placeholder('name@example.com').fill('olhaz@gmail.com')
    page.get_by_role('radio', name='Female').click()
    page.get_by_placeholder('Mobile Number').fill('0654875687')
    page.locator("#dateOfBirthInput").fill("13 Mar 2024")
    page.get_by_role('checkbox', name='Sports').click()
    page.get_by_placeholder('Current Address').fill('Svetlaya17n')
    page.locator("#react-select-3-input").fill("NCR")
    page.keyboard.press("Enter")
    page.locator("#react-select-4-input").fill("Delhi")
    page.keyboard.press("Enter")
    page.locator("#subjectsInput").fill("Math")
    page.keyboard.press("Enter")
    page.get_by_role('button', name='Submit').click()
