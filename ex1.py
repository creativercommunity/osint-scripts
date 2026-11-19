import requests

def check_github(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Пользователь найден: {data.get('name', 'Без имени')}")
            print(f"   Репозиториев: {data.get('public_repos', 0)}")
            print(f"   Ссылка: {data.get('html_url')}")
        elif response.status_code == 404:
            print(f"❌ Пользователь '{username}' не найден на GitHub")
        else:
            print(f"⚠️ Странный ответ: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка сети: {e}")


check_github("torvalds")
check_github("random_xxx_123")