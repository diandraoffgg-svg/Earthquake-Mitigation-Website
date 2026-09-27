import requests

url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"

respond = requests.get(url)
result = respond.json()

earthquake = result["Infogempa"]["gempa"]

print("===LATEST EARTHQUAKE INFORMATION===")
print(f"Time        :{earthquake['Tanggal']}, {earthquake['Jam']}")
print(f"Locati0n    :{earthquake['Wilayah']}")
print(f"Magnitude   :{earthquake['Magnitude']}")
print(f"Depth       :{earthquake['Kedalaman']}")
print(f"Coordinate  :{earthquake['Lintang']}, {earthquake['Bujur']}")