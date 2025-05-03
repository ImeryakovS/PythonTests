import random

rand = random.randint(1000, 9999)
credentials =   {
    'name' : f'Sergey{rand}',
    'email' : f'Sergey{rand}@test.ru',
    'login' : f'Sergey{rand}',
    'password' : 'password123'
}

existing_credentials = {
    'name' : 'SergeySergey',
    'email' : 'SergeySergey@test.ru',
    'login' : 'SergeySergey',
    'password' : 'test123'
}

low_access_credentials = {
    'name' : 'LowAccess',
    'email' : 'LowAccess@test.ru',
    'login' : 'LowAccess',
    'password' : 'test'
}

organizations_user = {
    'name' : 'Organization',
    'email' : 'Organization@test.ru',
    'login' : 'Organization',
    'password' : 'test'
}

change_password = {
    "password" : "testPassword"
}