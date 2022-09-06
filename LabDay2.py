def valid_email(email):
    if email.count('@') != 1:
        return False

    recipient_name = email.split('@')[0]
    domain_name = email.split('@')[-1]

    if len(recipient_name) > 64:
        return False

    if domain_name.count('.') != 1 or len(domain_name) > 253:
        return False

    before_dot = domain_name.split('.')[0]
    after_dot = domain_name.split('.')[-1]

    if not before_dot.isalpha():
        return False
    if (not after_dot.isalpha()) or len(after_dot) < 2 or len(after_dot) > 3:
        return False

    return True


def valid_web_url(link):
    if link.count('://') != 1:
        return False

    scheme_name = link.split('://')[0]

    if scheme_name not in ('http', 'https', 'ftp', 'mailto'):
        return False

    return True


def valid_date(date):
    day = int(date.split('/')[0])
    month = date.split('/')[1]

    if int(month) > 12 or (month in ('04', '06', '09', '11') and day > 30) \
            or (month in ('01', '03', '05', '07', '08', '10', '12') and day > 31) \
            or (month == '02' and day > 29):
        return False

    return True


def valid_credit_card_number(num):
    if not num.isnumeric() or len(num) != 16:
        return False
    return True


def valid_mobile_phone_number(num):
    if len(num) == 9:
        if not num.startswith('0') or not num.isnumeric():
            return False
    if len(num) == 12:
        if not num.startswith('+374') or not num[1:].isnumeric():
            return False

    return True


choose = input('choose one of (Email / Website URL / Date / Credit Card Number / Mobile Phone Number): ')

if choose == 'Email':
    input_email = input('enter your email: ')
    print(valid_email(input_email))

if choose == 'Website URL':
    input_url = input('enter your URL: ')
    print(valid_web_url(input_url))

if choose == 'Date':
    input_date = input('enter your Date (DD/MM/YY): ')
    print(valid_date(input_date))

if choose == 'Credit Card Number':
    input_credit_card_number = input('enter your Credit Card Number: ')
    print(valid_credit_card_number(input_credit_card_number))

if choose == 'Mobile Phone Number':
    input_mobile_phone_number = input('enter your Mobile Phone Number: ')
    print(valid_mobile_phone_number(input_mobile_phone_number))
