class User:
    def __init__(self, user_name, user_pass):
        self.user_name = user_name
        self.user_pass = user_pass


    def checkeng_user_name(function):
        def wrapper(self, *args, **kwargs):
            if len(self.user_name) < 6 or len(self.user_pass) < 3:
                raise ValueError('имя пользовотеля должно быть не менее 6 символов, и пороль не менее 3 символов')
            return function(self, *args, **kwargs)
        return wrapper

    def email(function):
        def wrapper(self, *args, **kwargs):
            if '@' not in self.user_name:
                raise ValueError('нет символа @')
            return function(self, *args, **kwargs)
        return wrapper

    @email
    @checkeng_user_name
    def user_reg(self):
        print('пользователь зарегестрирован')


    # @checkeng_user_name
    # def ололо(self):
    #     print("эЭ")


user = User('sdffffd', '456524443')
user.user_reg()
