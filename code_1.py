def register():
    with open('logins.txt','w')as file :
        global add
        addlogin = input('Введите Логин :')
        addpass = input('Введите Пароль : ')
        file.write(addlogin + ' ' +addpass +'\n')
    with open('logins.txt', 'r') as file:
        add = file.readline()
        add = add.replace('\n' , '')
        add = add.split()
        print(add)
def login():
    logins = input('Введите Логин')
    passw = input('Введите Пароль')
    if logins == add[0] and passw == add[1]:
        print('Успешно')
    elif logins == add[0] and passw != add[1]:
        print('Не Верный Пароль')
    elif logins != add[0]:
        print('Не Верный Логин')
