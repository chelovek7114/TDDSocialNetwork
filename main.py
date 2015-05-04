__author__ = 'CHELOVEK7114'


class SocialNetwork:
    def __init__(self):
        self.cur_person = None
        self.persons = []

    def hello1(self):
        return 'Здравствуйте, вы зарегистрированы? (да, нет) ', lambda answer: self.hello2(answer)

    def hello2(self, answer):
        if answer == 'да':
            return 'Вход. Введите логин: ', lambda login: self.sign_in1(login)
        elif answer == 'нет':
            return 'Регистрация. Введите логин: ', lambda login: self.registration1(login)
        else:
            return 'Вы зарегистрированы? (да, нет) ', lambda answer1: self.hello2(answer1)

    def sign_in1(self, login):
        if login:
            return 'Вход. Введите пароль: ', lambda password: self.sign_in2(password, login)
        else:
            return 'Вход. Логин не может быть пустым. Повторите ввод: ', lambda login1: self.sign_in1(login1)

    def sign_in2(self, password, login):
        for person in self.persons:
            if person.login == login and person.password == password:
                self.cur_person = person
                return 'Вход выполнен успешно. Нажмите Enter для продолжения. ', lambda: self.main()
        return 'Неправильный логин или пароль. Нажмите Enter для продолжения. ', lambda: self.hello1()

    def registration1(self, login):
        if login:
            return 'Регистрация. Введите пароль: ', lambda password: self.registration2(password, login)
        else:
            return (
                'Регистрация. Логин не может быть пустым. Повторите ввод: ',
                lambda login1: self.registration1(login1),
            )

    def registration2(self, password, login):
        self.cur_person = Person(login, password)
        self.persons.append(self.cur_person)
        return 'Поздравляем, вы зарегистрированы! Нажмите Enter для продолжения. ', lambda: self.main()

    def main(self):
        return 'Здравствуйте, {0}. Что вы хотите? '.format(self.cur_person.login), None


class Person:
    def __init__(self, login, password):
        self.login = login
        self.password = password