from unittest import TestCase
from main import SocialNetwork, Person

__author__ = 'CHELOVEK7114'


class TestSocialNetwork(TestCase):
    def test_hello1(self):
        sn = SocialNetwork()
        fact = sn.hello1()[0]
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
        fact = sn.sign_in1('Вася')[0]
        expected = 'Вход. Введите пароль: '
        self.assertEqual(fact, expected)
        fact = sn.sign_in1('')[0]
        expected = 'Вход. Логин не может быть пустым. Повторите ввод: '
        self.assertEqual(fact, expected)

    def test_sign_in2(self):
        sn = SocialNetwork()
        sn.persons.append(Person('Вася', 'пароль'))
        fact = sn.sign_in2('пароль', 'Вася')[0]
        expected = 'Вход выполнен успешно. Нажмите Enter для продолжения. '
        self.assertEqual(fact, expected)
        fact = sn.sign_in2('пароль', 'Петя')[0]
        expected = 'Неправильный логин или пароль. Нажмите Enter для продолжения. '
        self.assertEqual(fact, expected)

    def test_registration1(self):
        sn = SocialNetwork()
        fact = sn.registration1('Вася')[0]
        expected = 'Регистрация. Введите пароль: '
        self.assertEqual(fact, expected)
        fact = sn.registration1('')[0]
        expected = 'Регистрация. Логин не может быть пустым. Повторите ввод: '
        self.assertEqual(fact, expected)

    def test_registration2(self):
        sn = SocialNetwork()
        fact = sn.registration2('пароль', 'Вася')[0]
        expected = 'Поздравляем, вы зарегистрированы! Нажмите Enter для продолжения. '
        self.assertEqual(fact, expected)

    def test_main(self):
        sn = SocialNetwork()
        sn.cur_person = Person('Вася', 'пароль')
        fact = sn.main()[0]
        expected = 'Здравствуйте, Вася. Что вы хотите? '
        self.assertEqual(fact, expected)

    def test_registration_and_sign_in(self):
        sn = SocialNetwork()
        fact = sn.hello1()[1]('не знаю')[1]('нет')[1]('')[1]('Миша')[1]('пароль')[1]()
        expected = 'Здравствуйте, Миша. Что вы хотите? '
        self.assertEqual(fact[0], expected)
        fact = sn.hello1()[1]('да')[1]('Миша')[1]('пароль')[1]()
        expected = 'Здравствуйте, Миша. Что вы хотите? '
        self.assertEqual(fact[0], expected)
        fact = sn.hello1()[1]('да')[1]('Миша')[1]('неправильный пароль')[1]()
        expected = 'Здравствуйте, вы зарегистрированы? (да, нет) '
        self.assertEqual(fact[0], expected)
        fact = sn.hello1()[1]('да')[1]('Петя')[1]('пароль')[1]()
        expected = 'Здравствуйте, вы зарегистрированы? (да, нет) '
        self.assertEqual(fact[0], expected)