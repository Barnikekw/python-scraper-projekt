import requests
import json

def get_random_fact():
    # Ingyenes, nyilvános API, ami hasznos/érdekes tényeket ad vissza angolul
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    
    print("Kapcsolódás a külső API-hoz...")
    
    try:
        response = requests.get(url)
        
        # Ellenőrizzük, hogy a kérés sikeres volt-e (200 OK kód)
        if response.status_code == 200:
            data = response.json()
            fact_text = data.get("text", "Nincs adat")
            
            print(f"\nSikeres lekérdezés! Íme a mai tény:\n-> {fact_text}\n")
            
            # Elmentjük helyben egy fájlba is
            save_to_file(fact_text)
        else:
            print(f"Hiba történt a szerver oldalon. Státuszkód: {response.status_code}")
            
    except Exception as e:
        print("Hálózati hiba lépett fel:", e)

def save_to_file(text):
    with open("eredmenyek.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")
    print("Az adat sikeresen elmentve az 'eredmenyek.txt' fájlba!")

if __name__ == "__main__":
    get_random_fact()