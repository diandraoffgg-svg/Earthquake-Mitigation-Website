import requests

url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"

respond = requests.get(url)
result = respond.json()

eq_list = [result["Infogempa"]["gempa"]]

print("===EARTHQUAKE REPORT===")

count = 0
biggest_mag = 0
biggest_place = None

for idx, quake in enumerate(eq_list, 1):
    count += 1

    tanggal = quake["Tanggal"]
    waktu = quake["Jam"]
    lokasi = quake["Wilayah"]
    magnitude = float(quake["Magnitude"])
    depth = quake["Kedalaman"]

    print(f"\n#{idx}")
    print(f"Time        : {tanggal}, {waktu}")
    print(f"Location    : {lokasi}")
    print(f"Magnitude   : {magnitude}")
    print(f"Depth       : {depth}")

    if magnitude > biggest_mag:
        biggest_mag = magnitude
        biggest_place = lokasi

print("\nEarthquakes in total: ", count)
print("Strogest quake: ", biggest_mag, "at", biggest_place)

print("\nQuakes above magnitude 5: ")
found = False 
for quake in eq_list:
    if float(quake["Magnitude"])>5:
        print(f"-quake{['Wilayah']} (M{quake['Magnitude']})")
        fount = True

if not found:
    print("None this time")