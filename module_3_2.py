def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    name_end = (".com",".ru",".net")
    if recipient.endswith(name_end) and "@" in recipient and sender.endswith(name_end) and "@" in sender:
        if sender != 'university.help@gmail.com' and recipient != sender:
           print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
        elif recipient == sender:
           print("Нельзя отправить письмо самому себе!")
        else:
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.uk', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
