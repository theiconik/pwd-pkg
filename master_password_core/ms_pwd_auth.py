import bcrypt, stdiomask
from db_ms_pwd_fetch import db_ms_pwd

# password = b"SuperSercet34"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# print(hashed)


def auth(username):
    user_input = stdiomask.getpass(prompt='Enter master password: ',
                                   mask='*').encode("utf-8")
    # print(user_input)
    hashed = db_ms_pwd(username).encode('utf-8')

    if bcrypt.checkpw(user_input, hashed):
        return 1
    else:
        return 0


# print(auth())
