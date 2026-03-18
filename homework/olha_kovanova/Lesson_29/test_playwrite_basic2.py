from playwright.sync_api import Page, Dialog, expect, BrowserContext


# Задание 1
# Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/alert/confirm, кликает на кнопку, чтобы
# появился алерт, жмет Ok и проверяет, что на страние в секции "You selected" написано "Ok"
def test_accept_alert(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', accept_alert)
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    click_btn = page.get_by_role("link", name="Click")
    click_btn.click()

    result_text = page.locator('#result-text')
    expect(page.locator("#result")).to_be_visible()
    expect(result_text).to_have_text('Ok')

# Задание 2
# Напишите тест, который зайдет на страницу https://www.qa-practice.com/elements/new_tab/button, нажмет на кнопку Click,
# в открывшемся табе проверит, что в результате написано "I am a new page in a new tab" и проверит, что на изначальной
# вкладке кнопка Click - активна (enabled)


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_btn = page.get_by_role("link", name="Click")
    click_btn.click()

    with context.expect_page() as new_page_event:
        click_btn.click()
    new_page = new_page_event.value

    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()

    expect(click_btn).to_be_enabled()

# Задание 3
# Напишите тест, который зайдет на страницу https://demoqa.com/dynamic-properties, нажмет на кнопку Color change только
# после того как она станет красной.


def test_change_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_change_btn = page.locator('#colorChange')
    visible_after_btn = page.locator('#visibleAfter')

    expect(visible_after_btn).to_be_visible(timeout=10000)
    expect(color_change_btn).to_have_css("color", "rgb(220, 53, 69)")

    color_change_btn.click()
