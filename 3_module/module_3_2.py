#!/usr/bin/env python3
# RFC 5322 regex
# "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
# Task regex
# 
import re
import traceback
email_regex = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+\.(ru|net|com)"

def debug_call(func):
    def wrapper(*args, **kwords):
        output = None
        try:
            output = func(*args, **kwords)
        except:
            traceback.print_exc()  
        return 
    return wrapper

@debug_call
def send_email(message: str, recipient: str,
               sender: str = 'university.help@gmail.com') -> None:
    '''Prototype function for sending email'''
    # Let's strip for user convenience 
    sender, recipient = sender.strip(), recipient.strip()
    if (not re.match(email_regex, recipient)): 
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        raise ValueError(f"(!) Malformed recipient email: {recipient}")
    if (not re.match(email_regex, sender)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        raise ValueError(f"(!) Malformed sender email: {sender}")
    if sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
        raise RuntimeError(f"(!) sender and recipient email's matches.")
    # SMTP logic goes hear
    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
