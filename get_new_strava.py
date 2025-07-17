import requests

# === CONFIGURATION INITIALISATION ===
CLIENT_ID = '168618'
CLIENT_SECRET = '077731df90902a8ee847a979c772b4b33796670b'
CODE = '365dac6c72b6ae01d79416e7296f3436f2bdc149'  # Le code copié depuis l'URL

# === ÉTAPE 1 : échange du code contre un token ===
def get_tokens_from_code(client_id, client_secret, code):
    response = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': 'authorization_code'
        }
    )

    if response.status_code != 200:
        print("❌ Erreur lors de l'échange du code :", response.text)
        return None

    tokens = response.json()
    print("✅ Jetons récupérés avec succès :")
    print("Access token :", tokens['access_token'])
    print("Refresh token :", tokens['refresh_token'])
    print("Expire à :", tokens['expires_at'])
    return tokens

# === ÉTAPE 2 : récupérer les dernières activités ===
def get_strava_activities(access_token, max_results=5):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(
        'https://www.strava.com/api/v3/athlete/activities',
        headers=headers,
        params={'per_page': max_results, 'page': 1}
    )

    if response.status_code != 200:
        print("❌ Erreur lors de la récupération des activités :", response.text)
        return []

    activities = response.json()
    print(f"\n📋 {len(activities)} activités récentes :\n")
    for a in activities:
        print(f"🔹 {a['start_date_local']} – {a['name']}")
        print(f"   🏃 Type       : {a['type']}")
        print(f"   📏 Distance   : {a['distance'] / 1000:.2f} km")
        print(f"   ⏱️ Durée      : {a['moving_time'] // 60} min")
        print(f"   ❤️ FC Moyenne : {a.get('average_heartrate', 'N/A')}")
        print("")
    return activities

# === MAIN ===
if __name__ == "__main__":
    tokens = get_tokens_from_code(CLIENT_ID, CLIENT_SECRET, CODE)
    if tokens:
        get_strava_activities(tokens['access_token'])