import re


def main_func(partner_data: dict):
    # функция для общей проверки информации
    if (check_name(partner_data['name']) and
        check_type(partner_data['type']) and
        check_director(partner_data['director']) and
        check_phone(partner_data['phone']) and
        check_mail(partner_data['mail']) and
        check_ur_addr(partner_data['ur_addr']) and
        check_inn(partner_data['inn']) and
        check_rate(partner_data['rate'])):
        return True
    return False

def check_name(name):
    if len(name) != 0:
        return True
    return False

def check_type(type):
    if type in ["ЗАО", "ООО", "ПАО", "ОАО"]:
        return True
    return False

def check_director(director):
    if len(director.split(" ")) == 3:
        return True
    return False

def check_phone(phone_number):
    try:
        regex = re.compile(r'[94][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9] [0-9][0-9]')
        if re.fullmatch(regex, phone_number):
            return True
        return False
    except Exception:
        return False

def check_mail(mail):
    if (len(mail) != 0 and
        len(mail.split("@")) == 2 and
        len(mail.split("@")[1].split(".")) == 2):
        return True
    return False

def check_ur_addr(ur_addr):
    if (len(ur_addr.split(", ")[0]) == 6 and ur_addr.split(", ")[0].isdigit()
        and len(ur_addr.split(", ")[1]) != 0):
        return True
    return False

def check_inn(inn: str):
    if len(inn) == 10 and inn.isdigit():
        return True
    return False

def check_rate(rate):
    if int(rate) in range(1, 11):
        return True
    return False