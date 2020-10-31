import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_add_to_basket_button_present(browser):
    browser.get(link)
    add_to_basket_button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(10)
    assert bool(add_to_basket_button) == True, 'Нет кнопки "Добавить в корзину"'
