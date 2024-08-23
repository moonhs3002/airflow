def get_sftp():
    print("sftp start")

def regist(name, sex, *args):
    print(f' name : {name}')
    print(f' sex  : {sex}')
    print(f' args : {args}')

def regist2(name, sex, *args, **kwargs):
    print(f'name : {name}')
    print(f'sex  : {sex}')
    print(f'args : {args}')
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    if email:
        print(email)
    if phone:
        print(phone)
