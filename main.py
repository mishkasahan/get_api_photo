import os
import requests


def get_foto(teg):
    url = (f"https://api.pexels.com/v1/search?query={teg}&per_page=1")
    api_key = 'MeRXswhRL3hDsIgmTM4LEwT9wpyF5TFhsjMZQuLMyvMSt6bs03IYzbqV'
    try:
        response = requests.get(url, headers={'Authorization': api_key})
        if response.status_code == 200:
            resp = response.json()
            url_photo = resp["photos"][0]["src"]["original"]
            respons = requests.get(url_photo)

            if not os.path.exists('downloaded_photos'):
                os.makedirs('downloaded_photos')

            with open(f'downloaded_photos/{teg}_photo.jpg', 'wb') as file:
                file.write(respons.content)

        else:
            print(f"Помилка отримання відповіді. Код помилки - {response.status_code}")

    except Exception as e:
        print(f"Виникла помилка: {e}")


get_foto("cat")
