from fake_user_agent.main import user_agent
import mimesis
import string
import random


# create new person
def create_person(domen, current_proxy):
    ua = user_agent()

    new_person = mimesis.Person('en')

    first_name = new_person.first_name()
    last_name = new_person.last_name()

    password = ''.join(random.choice(string.hexdigits) for i in range(15))

    login = '{}{}'.format(first_name, ''.join(random.choice(string.hexdigits) for i in range(5)))

    login_inst = first_name + '_' + last_name + ''.join(random.choice(string.hexdigits) for i in range(5))

    birthday = (random.randint(1, 11), random.randint(1, 25), random.randint(20, 30))

    email = login + '@' + domen

    new_person_info = {
        'id': '-',
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'login': login,
        'ua': ua,
        'proxy': current_proxy,
        'login_inst': login_inst,
        'birthday': birthday,
        'is_inst_created': '0'
    }

    return new_person_info
