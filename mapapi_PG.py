import pygame
import requests
import os


def show_map(ll_spn, map_type="map", add_params=None):
    """Отображение карты с помощью pygame"""
    map_url = "https://static-maps.yandex.ru/1.x/"

    # Базовые параметры
    params = {
        "l": map_type,
        "size": "650,450"
    }

    # Добавляем координаты и масштаб
    params.update(dict(param.split('=') for param in ll_spn.split('&')))

    # Добавляем дополнительные параметры (метку)
    if add_params:
        params.update(dict(param.split('=') for param in add_params.split('&')))

    try:
        response = requests.get(map_url, params=params)
        response.raise_for_status()

        # Сохраняем временный файл карты
        map_file = "map.png"
        with open(map_file, "wb") as f:
            f.write(response.content)

        # Инициализация pygame
        pygame.init()
        screen = pygame.display.set_mode((650, 450))
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()

        # Ожидание закрытия окна
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
        os.remove(map_file)

    except Exception as e:
        print(f"Ошибка при работе с картой: {e}")