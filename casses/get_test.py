# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.AuthPage import AuthPage
from pages.IdPage import Main_page


class GetTest(unittest.TestCase):

    def runTest(self):
        """
        Тут описываются тест кейсы
        :return:
        """
        # Главная страница
        self.test_change_personal_info()
        print("Done 1")
        self.test_go_to_all_settings()
        print("Done 2")
        self.test_equality_names()
        print("Done 3")
        self.test_click_add_reserve_email()
        print("Done 4")
        print("Done main page tests")
        #Pop Up
        self.test_check_empty_email()
        print("Done 5")
        self.test_check_incorrect_email()
        print("Done 6")
        self.test_check_correct_email()
        print("Done 7")

        self.clear_email_after_tests()
        print("Done Pop Up tests")



    def setUp(self) -> None:
        browser = 'CHROME'
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        LOGIN = os.environ['LOGIN']
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)
        id_page = Main_page(self.driver)
        id_page.open()
        self.main_page = Main_page(self.driver)

    def go_to_main(self):
        self.main_page.open(self.main_page.BASE_URL)

    def clear_email_after_tests(self):
        self.main_page.clear_reserve_email()


    def tearDown(self) -> None:
        self.driver.quit()

    def test_change_personal_info(self):
        ok = self.main_page.click_change_personal_info()
        self.assertTrue(ok)
        self.go_to_main()

    def test_go_to_all_settings(self):
        ok = self.main_page.click_get_all_settings()
        self.assertTrue(ok)
        self.go_to_main()

    def test_equality_names(self):
        self.assertEqual(self.main_page.get_name_surname_from_left_bar(), self.main_page.get_name_surname_from_card())

    def test_click_add_reserve_email(self):
        ok = self.main_page.click_add_reserve_email()
        self.assertTrue(ok)

    def test_check_empty_email(self):
        res = self.main_page.add_email("")
        self.assertEqual(res, "Укажите почту")

    def test_check_incorrect_email(self):
        res = self.main_page.add_email("asd")
        self.assertEqual(res, "Неправильная почта. Укажите другую.")

    def test_check_correct_email(self):
        header=self.main_page.add_email("correct@yandex.ru")
        self.assertEqual(header, "Резервная почта добавлена")

