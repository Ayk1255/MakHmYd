def greet(name):
    return f"Привет, {name}! Это мой первый коммит из PyCharm."


if __name__ == "__main__":
    user_name = input("Введите ваше имя: ")
    print(greet(user_name))