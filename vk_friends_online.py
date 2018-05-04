import vk


def get_api_session(login, password):
    app_id = 6469230
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    return vk.API(session, v='5.35')


def get_online_friends(api_session):
    friends_online_ids = api_session.friends.getOnline()
    friends = api_session.friends.get(fields='online')['items']
    friends_online = []
    for friend in friends:
        if friend['id'] in friends_online_ids:
            friends_online.append(friend)
    return friends_online


def output_friends_to_console(friends_online):
    print('Online now:')
    for friend_online in friends_online:
        print('{} {}'.format(
            friend_online['first_name'], friend_online['last_name']))


if __name__ == '__main__':
    login = input('Input e-mail or phone number: ')
    password = input('Imput your password: ')
    api_session = get_api_session(login, password)
    friends_online = get_online_friends(api_session)
    output_friends_to_console(friends_online)
