from getpass import getpass

from owl import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

def generate_pw_hash(password, file):
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        with open(file, 'w') as pwfile:
            pwfile.write(pw_hash)

if __name__ == '__main__':
    with app.app_context():
        file = input('Enter password file name (default: .pw): ')
        if not file:
            file = '.pw'
        password = getpass('Enter new password: ')
        confirm = getpass('Confirm password: ')
        if password != confirm:
            print('Abort! Password mismatch.')
            exit()
        generate_pw_hash(password, file)
        print('Success! New password file created: {}'.format(file))
        if file != '.pw':
            print('Don\'t forgot change password file name in `config.py`.')