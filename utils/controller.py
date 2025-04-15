def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowosci {user["location"]} opublikował {user["posts"]} postów')


def add_user(users_data: list) -> None:
    new_name: str = input('podaj imie nowego znajomego: ')
    new_location: str = input('podaj lokalizacje: ')
    new_posts: str = input('podaj liczbe postów: ')
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts}),
