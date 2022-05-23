import bcrypt
import hmac
import hashlib
import base64

from PyQt5.QtSql import QSqlQuery


def encode_string(string):
    return string.encode('utf-8')


def check_password(password, hash_password):
    salt = "146585145368132386173505678016728509634"
    h = hmac.new(encode_string(salt), encode_string(password), hashlib.sha512)
    h = base64.b64encode(h.digest())
    return bcrypt.checkpw(h, encode_string(hash_password))


def check_cookie():
    def decorator(function):
        def wrapper(self, *args, **kwargs):
            print(self.username)
            print(self.password)
            query = QSqlQuery()
            query.prepare("SELECT password FROM users WHERE username = :username")
            query.bindValue(":username", self.username)
            query.exec()
            if query.next():
                hash_password = query.value(0)
                if check_password(self.password, hash_password):
                    return function(self, *args, **kwargs)
                else:
                    print("Error")
            else:
                print("Error")
        return wrapper
    return decorator
