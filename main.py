def greet(name):
    return f"Привет, {name}! Это мой первый коммит из PyCharm."

def sum(a:int,b:int):
    return a+b


if __name__ == "__main__":
    user_name = input("Введите ваше имя: ")
    print(greet(user_name))
    a = input("Первое число")
    b = input("Второе число")
    print(sum(a,b))