__author__ = 'CHELOVEK7114'


class SocialNetwork:
    def __init__(self):
        pass

    def hello1(self, answer):
        return 'Здравствуйте, вы зарегистрированы? (да, нет) ', None

    def hello2(self, answer):
        if answer == 'да':
            return 'Вход. Введите логин: ', None
        elif answer == 'нет':
            return 'Регистрация. Введите логин: ', None
        else:
            return 'Вы зарегистрированы? (да, нет) ', None

    def sign_in(self, answer):
        if answer:
            return 'Вход. Введите пароль: ', None
        else:
            return 'Вход. Логин не может быть пустым. Повторите ввод: ', None

    def sign_in2(self, answer, login):
        if login == 'Вася':
            return 'Здравствуйте, {0}. Что вы хотите? '.format(login), None
        else:
            return 'Неправильный логин или пароль. Нажмите Enter для продолжения. ', None

    def registration(self, answer):
        if answer:
            return 'Регистрация. Введите пароль: ', None
        else:
            return 'Регистрация. Логин не может быть пустым. Повторите ввод: ', None

    def registration2(self, answer, login):
        return 'Поздравляем, вы зарегистрированы! Нажмите Enter для продолжения. ', None

# self.cur_person = None

#     def sign_in(self):
#         answer = input('Вы зарегистрированы? (да/нет/выход): ')
#         while not (answer in ('да', 'нет', 'выход')):
#             answer = input('Вы зарегистрированы? Введите "да", "нет" или "выход": ')
#         if answer == 'выход':
#             return
#         if answer == 'да':
#             name = input('Введите ваш логин: ')
#             password = input('Введите ваш пароль: ')
#             self.cur_person = None
#             for person in self.persons:
#                 if name == person.name and password == person.password:
#                     self.cur_person = person
#                     break
#             if self.cur_person:
#                 self.menu()
#             else:
#                 print('Неправильно введён логин или пароль')
#                 self.sign_in()
#         else:
#             name = input('Введите логин: ')
#             while name == '':
#                 name = input('Логин не может быть пустым. Повторите ввод: ')
#             password = input('Введите пароль: ')
#             while password == '':
#                 password = input('Логин не может быть пустым. Повторите ввод: ')
#             self.cur_person = Person(name, password)
#             self.persons.append(self.cur_person)
#             self.menu()
#
#     def menu(self):
#         print('Hello ' + self.cur_person.name + '!!!')
#
#
# class Person:
#     def __init__(self, name, password):
#         self.password = password


#         self.name = name
