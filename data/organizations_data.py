import random

rand = random.randint(1000,9999)
test_organizations_body = {
    'name' : f'testOrganization{rand}',
}

add_in_organizations_body = {
    'loginOrEmail' : 'Organization',
    'role' : 'Editor'
}