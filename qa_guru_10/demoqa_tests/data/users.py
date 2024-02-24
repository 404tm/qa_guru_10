import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    gender: str
    # user_number: int
    # date_birth: str
    # hobby: str
    currentAddress: str
    # state: str
    # city: str


guest = User(full_name='Olga', email='404tm@example.com', gender='Female', currentAddress='Moscowskaya Street 18')

#guest_info = User(user_number='1234567891', date_birth={'1999', 'May', '11'}, hobby='Reading', address='Moscowskaya Street 18', state='NCR', city='Delhi')

