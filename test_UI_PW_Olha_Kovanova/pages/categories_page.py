import time

from playwright.sync_api import expect
from test_UI_PW_Olha_Kovanova.pages.base_page import BasePage
from test_UI_PW_Olha_Kovanova.pages.locators.categories_page_locators import *
import re


class CategoriesPage(BasePage):
    page_url = ''

    def wait_until_products_loaded(self):
        self.find(product_cards).first.wait_for(state="visible")

    def add_product_to_cart(self):
        # 1. Find product cart
        target_card = self.find(product_cards).filter(has_text="Customizable Desk")

        # Save the product name and clean it (delete extra space)
        product_name = target_card.locator(product_title_in_card).inner_text().strip()

        # 2. Hover and click on it
        target_card.hover()
        # use force=True, in case the button is over closed by another object
        target_card.locator(cart_btn).click(force=True)

        # 3. Check teh pop up
        cart_product_title_locator = self.find('strong.product-name').filter(has_text=re.compile(r"Customizable Desk"))

        expect(cart_product_title_locator, "Pop up with product wasn't pop up").to_be_visible(timeout=7000)

        # Check that product name is the same
        actual_text = cart_product_title_locator.inner_text()
        assert product_name in actual_text, f"Expected {product_name}, but in cart: {actual_text}"

    def proceed_to_checkout(self):
        self.find(proceed_to_checkout_btn).click()

    def select_legs(self):
        time.sleep(0.5)
        self.find(checkbox_custom_legs).first.click()

    def get_product_titles(self):
        return self.find(product_titles).all_inner_texts()

    def wait_until_products_count_is(self, count):
        expect(self.find(product_cards)).to_have_count(count)

    def get_first_product_title(self):
        return self.find(product_title_in_card).first.inner_text().strip()

    def get_first_product_price(self):
        price_text = self.find(product_price_in_card).first.inner_text()
        return float(price_text.replace("$", "").replace(",", ""))

    def get_first_product_data(self):
        return {
            "title": self.get_first_product_title(),
            "price": self.get_first_product_price()
        }

    def open_first_product(self):
        self.find(product_title_in_card).first.click()

    def should_have_single_product_with_title(self, expected_title: str):
        titles_locator = self.find(product_titles)
        expect(titles_locator).to_have_count(1)
        expect(titles_locator).to_have_text(expected_title)

    def should_have_cart_quantity(self, expected_quantity: int):
        locator = self.find(f"{cart_quantity_label}:visible").first

        expect(locator, f"Expected product quantity: {expected_quantity}").to_have_text(str(expected_quantity))

    def should_have_products_loaded(self):
        expect(self.find(product_cards).first, "Product list is empty").to_be_visible()

    def should_contain_product(self, expected_title: str):
        (expect(self.find(product_titles), f"Product name '{expected_title}' wasn't find in product list")
         .to_contain_text([expected_title]))
