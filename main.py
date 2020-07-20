import pandas as pd
from functions import adjust_person_name, adjust_phone

raw_contacts = pd.read_excel('raw_contacts.xlsx', headers=True, dtype={'name':str, 'phone':str})

raw_contacts['name'] = raw_contacts['name'].apply(adjust_person_name)
raw_contacts['phone'] = raw_contacts['phone'].apply(adjust_phone)

raw_contacts.to_excel('contacts.xlsx', header=True, index=False)