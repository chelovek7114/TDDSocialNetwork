from unittest import TestCase
from main import SocialNetwork

__author__ = 'CHELOVEK7114'


class TestSocialNetwork(TestCase):
    def test_hello(self):
        sn = SocialNetwork()
        fact = sn.hello1('')[0]
        expected = 'Здравствуйте, вы зарегистрированы? (да, нет) '
        self.assertEqual(fact, expected)

    def test_hello2(self):
        sn = SocialNetwork()
        fact = sn.hello2('да')[0]
        expected = 'Вход. Введите логин: '
        self.assertEqual(fact, expected)
        fact = sn.hello2('нет')[0]
        expected = 'Регистрация. Введите логин: '
        self.assertEqual(fact, expected)
        fact = sn.hello2('не знаю')[0]
        expected = 'Вы зарегистрированы? (да, нет) '
        self.assertEqual(fact, expected)

    def test_sign_in(self):
        sn = SocialNetwork()
        fact = sn.sign_in('Вася')[0]
        expected = 'Вход. Введите пароль: '
        self.assertEqual(fact, expected)
        fact = sn.sign_in('')[0]
        expected = 'Вход. Логин не может быть пустым. Повторите ввод: '
        self.assertEqual(fact, expected)

    def test_sign_in2(self):
        sn = SocialNetwork()
        fact = sn.sign_in2('пароль', 'Вася')[0]
        expected = 'Здравствуйте, Вася. Что вы хотите? '
        self.assertEqual(fact, expected)
        fact = sn.sign_in2('пароль', 'Петя')[0]
        expected = 'Неправильный логин или пароль. Нажмите Enter для продолжения. '
        self.assertEqual(fact, expected)

    def test_registration(self):
        sn = SocialNetwork()
        fact = sn.registration('Вася')[0]
        expected = 'Регистрация. Введите пароль: '
        self.assertEqual(fact, expected)
        fact = sn.registration('')[0]
        expected = 'Регистрация. Логин не может быть пустым. Повторите ввод: '
        self.assertEqual(fact, expected)

    def test_registration2(self):
        sn = SocialNetwork()
        fact = sn.registration2('пароль', 'Вася')[0]
        expected = 'Поздравляем, вы зарегистрированы! Нажмите Enter для продолжения. '
        self.assertEqual(fact, expected)