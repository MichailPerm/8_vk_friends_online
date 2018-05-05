import sys, vk, getpass


def get_api_session(login, password, app_id=6469230, version='5.35'):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    return vk.API(session, v=version)


def get_online_friends(api_session):
    friends_online_ids = api_session.friends.getOnline()
    return api_session.users.get(user_ids=friends_online_ids)


def output_friends_to_console(friends_online):
    print('Online now:')
    for friend_online in friends_online:
        print('{} {}'.format(
            friend_online['first_name'], friend_online['last_name']))


if __name__ == '__main__':
    login = input('Input e-mail or phone number: ')
    password = getpass.getpass(prompt='Input your password: ')
    try:
        api_session = get_api_session(login, password)
    except vk.exceptions.VkAuthError:
        sys.exit('You\'ve entered uncorrect login or password')
    friends_online = get_online_friends(api_session)
    output_friends_to_console(friends_online)
