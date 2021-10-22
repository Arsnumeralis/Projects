import requests
import sys
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError(f'Error fecting: {resp.status_code}, check the api and try again')
    return resp

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

pwned_api_check(sys.argv[1])

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Your password "{password}" has been found {count} time(s). You should probably change it.')
        else: print(f'{password} has not yet been found')
    return 'done'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))