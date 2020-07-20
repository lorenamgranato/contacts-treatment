import re

def adjust_person_name(raw_name):
    name = re.sub(r"[0-9-]+", "", raw_name)

    position = name.find('(')
    if name[position + 1] == ')': name = name[:position] + name[position + 2:]
    
    name = name.strip().title()
    return name


def adjust_phone(raw_phone):
    phone = re.sub('[^0-9]', '', raw_phone)
    
    if len(phone) > 11 and phone[0:2] == '55':
        phone = phone[2:]

    while (phone[0] == '0') and (len(phone) >= 2):
        phone = phone[1:]

    if (len(phone) == 10) and phone[2] in ['7', '8', '9']:
        phone = phone[:2] + '9' + phone[2:]
    
    return int(phone)