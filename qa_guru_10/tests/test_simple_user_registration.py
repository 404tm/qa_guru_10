from demoqa_tests.application import app
from demoqa_tests.data import users

def test_registers_user():
    app.simple_registration.open()

    app.simple_registration.register(users.guest)


    #app.profile.should_have_data(users.admin)
