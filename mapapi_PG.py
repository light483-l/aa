import pygame
import requests
import os


def show_map(ll_spn, map_type="map", add_params=None):
    map_url = "https://static-maps.yandex.ru/1.x/"

    params = {
        "l": map_type,
        "size": "650,450"
    }
    
    params.update(dict(param.split('=') for param in ll_spn.split('&')))

    if add_params:
        params.update(dict(param.split('=') for param in add_params.split('&')))

    try:
        response = requests.get(map_url, params=params)
        response.raise_for_status()

        map_file = "map.png"
        with open(map_file, "wb") as f:
            f.write(response.content)

        pygame.init()
        screen = pygame.display.set_mode((650, 450))
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
        os.remove(map_file)

    except Exception as e:
        print(f"Ошибка при работе с картой: {e}")
