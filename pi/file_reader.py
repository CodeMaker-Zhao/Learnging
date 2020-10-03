import json

def get_stored_username():
    """如果有过去的用户名就直接获取"""
    try:
        with open('username.json') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """跟用户打招呼"""
    username = get_stored_username()
    if username:
        same = input('please input Y/N '+ username + 'is yours \n')
        if same == "Y" or same == "y":
            print('Welcome back '+ username)
        elif same == "N" or same == "n":
            username = get_new_username()
            print('We will remeber you when you come back '+ username+'!')
        else:
            greet_user() 
    else:
        username = get_new_username()
        print('We will remeber you when you come back '+ username+'!') 

def get_new_username():
    """设置用户名"""
    username = input('please input your name \n')
    with open('username.json', 'w') as f_obj:
        json.dump(username, f_obj)
    return username

greet_user()