__author__ = 'CHELOVEK7114'


class SocialNetwork:
    def __init__(self):
        self.cur_person = None
        self.persons = []

    def run(self):
        question = self.hello1()
        answer = None
        while answer != '!':
            answer = input(question[0])
            question = question[1](answer)

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
                return 'Вход выполнен успешно. Нажмите Enter для продолжения. ', lambda param: self.main1()
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
        return 'Поздравляем, вы зарегистрированы! Нажмите Enter для продолжения. ', lambda param: self.main1()

    def main1(self):
        return '{0}, что вы хотите? '.format(self.cur_person.login), lambda request: self.main2(request)

    def main2(self, request):
        if request == 'выход':
            return self.hello1()
        elif request == 'друзья':
            return self.show_friends()
        elif request[:len('добавить')] == 'добавить' and len(request.split()) == 2:
            return self.add_friend(request.split()[1])
        elif request[:len('удалить')] == 'удалить' and len(request.split()) == 2:
            return self.remove_friend(request.split()[1])
        elif request[:len('отправить')] == 'отправить' and len(request.split()) == 2:
            return self.send_message1(request.split()[1])
        elif request == 'сообщения':
            return self.show_messages()
        return 'Неправильный запрос, повторите ввод: ', lambda request1: self.main2(request1)

    def add_friend(self, friend_login):
        for person in self.persons:
            if person.login == friend_login:
                if person in self.cur_person.friends:
                    return (
                        '{0} уже итак у вас в друзьях. Нажмите Enter для продолжения. '.format(friend_login),
                        lambda param: self.main1()
                    )
                else:
                    self.cur_person.friends.append(person)
                    return (
                        '{0} добавлен в друзья. Нажмите Enter для продолжения. '.format(friend_login),
                        lambda param: self.main1()
                    )
        return 'Такого пользователя нет. Нажмите Enter для продолжения. ', lambda param: self.main1()

    def show_friends(self):
        answer = 'Ваши друзья: '
        for person in self.cur_person.friends:
            answer += person.login + ', '
        if self.cur_person.friends:
            answer = answer[:-2]
        return answer + '. Нажмите Enter для продолжения. ', lambda param: self.main1()

    def remove_friend(self, friend_login):
        for friend in self.cur_person.friends:
            if friend.login == friend_login:
                self.cur_person.friends.remove(friend)
                return (
                    '{0} удалён из ваших друзей. Нажмите Enter для продолжения. '.format(friend_login),
                    lambda param: self.main1()
                )
        return 'Такого друга у вас итак нет. Нажмите Enter для продолжения. ', lambda param: self.main1()

    def send_message1(self, friend_login):
        for friend in self.cur_person.friends:
            if friend.login == friend_login and self.cur_person in friend.friends:
                return 'Введите сообщение: ', lambda message: self.send_message2(message, friend)
        return (
            'Такого друга у вас нет или Вас нет у него в друзьях. Нажмите Enter для продолжения. ',
            lambda param: self.main1()
        )

    def send_message2(self, message, friend):
        friend.messages.append((self.cur_person, message))
        return 'Сообщение успешно отправлено. Нажмите Enter для продолжения. ', lambda param: self.main1()

    def show_messages(self):
        answer = 'Ваши сообщения:\n'
        for sender, message in self.cur_person.messages:
            answer += sender.login + ': ' + message + '\n'
        return answer + 'Нажмите Enter для продолжения. ', lambda param: self.main1()


class Person:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.friends = []
        self.messages = []

SocialNetwork().run()