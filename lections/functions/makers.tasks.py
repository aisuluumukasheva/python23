"task 5"
users = {
    'user1':123,
    'user2':345
}

def validate_password(func):
    def wrapper(username,password):
        try:
            if username not in users:
                raise KeyError
            elif users[username] != password:
                raise Exception("Password is invalid")
        except KeyError:
            print("Username is not defined ")
        except Exception as e:
            print(e)
        else:
            func(username,password)
    return wrapper

@validate_password
def login(username, password):
        print(f'Welcome, {username}')

login('user5', 123)

"==========task1================"
def call_function(func):
    def wrapper():
        print(f"Вызываю функцию {func.__name__}")
        func()
        print(f"Вызов функции {func.__name__} прошёл успешно")
    return wrapper


@call_function
def first():
    print("hello world")
    return "hello world"

first()
'==================Task 2=========='
def delay_time(seconds):
    def decorator(func):
        def wrapper():
            import time
            time.sleep(seconds)
            func()
        return wrapper
    return decorator

@delay_time(5)
def hello():
    print("Hello")

hello()