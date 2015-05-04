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
                return 'Вход выполнен успешно. Нажмите Enter для продолжения. ', lambda param: self.main()
        return 'Неправильный логин или пароль. Нажмите Enter для продолжения. ', lambda param: self.hello1()

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
        return 'Поздравляем, вы зарегистрированы! Нажмите Enter для продолжения. ', lambda param: self.main()

    def main(self):
        return '{0}, что вы хотите? '.format(self.cur_person.login), None

    def add_friend(self, friend_login):
        for person in self.persons:
            if person.login == friend_login:
                if person in self.cur_person.friends:
                    return (
                        '{0} уже итак у вас в друзьях. Нажмите Enter для продолжения. '.format(friend_login),
                        lambda param: self.main()
                    )
                else:
                    self.cur_person.friends.append(person)
                    return (
                        '{0} добавлен в друзья. Нажмите Enter для продолжения. '.format(friend_login),
                        lambda param: self.main()
                    )
        return 'Такого пользователя нет. Нажмите Enter для продолжения. ', lambda param: self.main()

    def show_friends(self):
        answer = 'Ваши друзья: '
        for person in self.cur_person.friends:
            answer += person.login + ', '
        if self.cur_person.friends:
            answer = answer[:-2]
        return answer + '. Нажмите Enter для продолжения. ', lambda param: self.main()

    def remove_friend(self, friend_login):
        for friend in self.cur_person.friends:
            if friend.login == friend_login:
                self.cur_person.friends.remove(friend)
                return 'Вася удалён из ваших друзей. Нажмите Enter для продолжения. ', lambda param: self.main()
        return 'Такого друга у вас итак нет. Нажмите Enter для продолжения. ', lambda param: self.main()


class Person:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.friends = []