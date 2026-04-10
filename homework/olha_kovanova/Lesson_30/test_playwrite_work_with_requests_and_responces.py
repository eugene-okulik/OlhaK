# Задание
# Напишите тест, который заходит на страницу https://www.apple.com/shop/buy-iphone, кликает по iPhone 17 Pro & iPhone 17
# Pro Max, в открывшемся попапе проверяет заголовок.
#
# Но не всё так просто. ))) Перед открытием страницы включите отлавливание запроса в котором приходит информация о товарах
# и измените ответ так так, чтобы iPhone 17 Pro в попапе назывался "яблокофон 17 про"
#
# Попробуйте самостоятельно поискать сам запрос и где что нужно подменить в ответе на этот запрос. Вам в помощь всякие
# онлайн отображатели json, чтобы было проще разобраться в структуре ответа. Я обычно пользуюсь
# https://jsoneditoronline.org/
#
# Если совсем не получится разобраться, пишите мне в личку, подскажу.
#
# Ну и при проверке заголовка в попапе проверяйте, что заголовок = тому, на что вы заменили название телефона.

import re
import json
from playwright.sync_api import Page, Route, expect


def test_change_iphone_name(page: Page):
    def change_title(route: Route):
        # 1. Fetch response
        response = route.fetch()
        data = response.json()

        if 'body' in data and 'digitalMat' in data['body']:
            # Take 1st object (iPhone 17 Pro)
            target = data['body']['digitalMat'][0]
            new_name = "яблокофон 17 про"

            # Go to familyTypes where productname is placed
            if 'familyTypes' in target:
                for family in target['familyTypes']:
                    # Change productName
                    if 'productName' in family:
                        family['productName'] = new_name

        # 2. Change it back to string(json)
        new_body = json.dumps(data)

        # 3. Finish process with our data
        route.fulfill(response=response, body=new_body)

    # switch on waiter of corresponding response which we want to fetch and change with method change_title
    page.route(re.compile(r'.*/shop/api/digital-mat.*'), change_title)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role("heading", name="iPhone 17 Pro & iPhone 17 Pro Max").click()

    header_locator = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    header_locator.filter(has_text="яблокофон 17 про")
    expect(header_locator).to_be_visible()
