def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowosci {user["location"]} opublikował {user["posts"]} postów')


def add_user(users_data: list) -> None:
    new_name: str = input('podaj imie nowego znajomego: ')
    new_location: str = input('podaj lokalizacje: ')
    new_posts: str = input('podaj liczbe postów: ')
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts}),


def remove_user(users_data: list) -> None:
    user_name: str = input('podaj znajomego do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)


def update_user(users_data: list) -> None:
    user_name: str = input('podaj imię uzytkownika do aktualizacji: ')
    for user in users_data:
        if user['name'] == user_name:
            user['name'] = input('podaj nowe imie uzytkownika: ')
            user['location'] = input('podaj nową lokalizacje: ')
            user['posts'] = input('podaj liczbe postów: ')