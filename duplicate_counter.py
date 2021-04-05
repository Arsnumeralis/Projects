user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenitcated(fn):
    def wrapper(user):
        if user.get('valid') == True:
            return fn(user)
        else:
            print('User not authorised.')
    return wrapper


@authenitcated
def message_friends(user):
    print('Message has been sent')

message_friends(user1)