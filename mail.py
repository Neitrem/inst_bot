import email
import imaplib
import time
from db_manager import get_person

# getting instagram code
def get_code(mail_address, password):
    mail = imaplib.IMAP4_SSL('imap.rambler.ru')

    mail.login(mail_address, password)

    loop = 0

    while True:
        mail.list()

        mail.select('inbox')

        result, data = mail.search(None, "ALL")

        ids = data[0]

        id_list = ids.split()

        for i in id_list:
            result, data = mail.fetch(i, "(RFC822)")
            message = data[0][1].decode('utf-8')
            message_str = email.message_from_string(message)

            from_ = message_str['From']
            subj = message_str['Subject']

            if("Instagram" in from_):
                code = str(subj).split()[0]
                print(code)
                return code, True

        time.sleep(10)
        loop += 1

        if(loop ==30):
            code = None
            return code, False


# sending some amount of messages etch other
def messaging(id_1, id_2):
    person_1 = get_person(id_1)
    person_2 = get_person(id_2)

    email_1 = person_1['email']
    pass_1 = person_1['password']

    email_2 = person_2['email']
    pass_2 = person_2['password']






