import requests
import matplotlib.pyplot as plt

url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"


respond = requests.get(url)
result = respond.json()


earthquake = result["Infogempa"]["gempa"]

magnitude = []
location = []

for quake in earthquake:
    magnitude.append(float(earthquake["Magnitude"]))
    location.append(earthquake["Wilayah"])

plt.figure(figsize=(12, 6))

plt.bar(range(len(magnitude)), magnitude)

plt.title("Magnitude of Recent Earthquakes(M 5.0+)")
plt.xlabel("Earthquake Event")
plt.ylabel("Magnitude (SR)")

plt.xticks(
    range(len(location)),
    [f"EQ {i + 1}" for i in range(len(location))],
    rotation = 45,
    ha="right",

)

plt.tight_layout()

plt.savefig("earthquake_magnitude.png")
plt.show()