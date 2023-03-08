import csv
import secrets
import names
from random_address import real_random_address_by_state
from datetime import datetime
from random import randint
from faker import Faker
import os
fake = Faker()


def generate_csv_file(columns, range_from, range_to,
                      column_separator, string_character, title, rows):
    date = datetime.now().strftime("%Y_%m_%d__%H_%M")
    data_scheme_folder = ''.join(("media/Sets/", title))
    if not os.path.exists(data_scheme_folder):
        os.makedirs(data_scheme_folder)
    with open(f'{data_scheme_folder}/{date}.csv', 'w') as file:
        writer = csv.writer(file, delimiter=column_separator,
                            quotechar=string_character,
                            quoting=csv.QUOTE_ALL)
        writer.writerow(columns)

        for row in range(rows):
            new_row = []
            for x, column in enumerate(columns):
                match column:
                    case 'integer':
                        new_row.append(randint(range_from[x], range_to[x]))
                    case 'full_name':
                        new_row.append(names.get_full_name())
                    case 'email':
                        new_row.append(f"{secrets.token_hex(8)}@gmail.com")
                    case 'address':
                        address = real_random_address_by_state('CA')
                        new_row.append(address['city'] + ' ' + address['address1'])
                    case 'job':
                        new_row.append('job')
                    case 'domain_name':
                        new_row.append('domain_name')
                    case 'phon_number':
                        new_row.append(randint(100000000, 999999999))
                    case 'company_name':
                        new_row.append('company_name')
                    case 'text':
                        new_row.append('text')
                    case 'date':
                        new_row.append(fake.date_between(start_date='today', end_date='+30y'))

            writer.writerow(new_row)
    return f'Sets/{title}/{date}.csv'
