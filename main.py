from geocoder import get_ll_span
from mapapi_PG import show_map


def main():
    if toponym := input("Введите адрес для поиска:").strip():
        if ll_spn := get_ll_span(toponym):
            show_map(f"ll={ll_spn[0]}&spn={ll_spn[1]}", "map", f"pt={ll_spn[0]},pm2rdm")


if __name__ == "__main__":
    main()
