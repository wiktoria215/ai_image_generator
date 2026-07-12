import requests

# Używamy działającej bramki i najnowszego modelu graficznego FLUX
API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
MOJ_TOKEN = "TUTAJ_WPISZ_SWOJ_TOKEN"

naglowki = {"Authorization": f"Bearer {MOJ_TOKEN}"}
moj_opis = "A gold ring with a blue topaz, surrounded by a gold cluster design, 4k resolution"
paczka_z_danymi = {"inputs": moj_opis}

print("Wysyłam prośbę do chmury (poczekaj chwilę)...")

odpowiedz = requests.post(API_URL, headers=naglowki, json=paczka_z_danymi)

if odpowiedz.status_code != 200:
    print(f"\nSerwer odrzucił żądanie. Kod błędu: {odpowiedz.status_code}")
    print("Szczegóły:", odpowiedz.text)
else:
    with open("wynik.png", "wb") as plik:
        plik.write(odpowiedz.content)
    print("Gotowe! Obraz został pomyślnie wygenerowany.")