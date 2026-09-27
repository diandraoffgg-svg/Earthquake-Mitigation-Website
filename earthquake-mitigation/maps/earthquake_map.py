import requests
import folium

url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"

respond = requests.get(url)
result = respond.json()

earthquake = result["Infogempa"]["gempa"]

CARTO_KEY = "cb1_4053_1_f2127fc7af4fb2374f576f08"

peta = folium.Map(
        location=[-2,108],
        zoom_start=5,


        tiles=f"https://basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}.png?key=cb1_4053_1_f2127fc7af4fb2374f576f08",

        attr='@ <a href= "https://www.openstreetmap.org/copyright"</a> contributors, @ <a href="https://carto.com/attribution/">CARTO</a>'
)

lintang = earthquake["Lintang"]
bujur = earthquake["Bujur"]

lintang = float(lintang.replace(" LS", "").replace(" LU", ""))
bujur = float(bujur.replace(" BT", "").replace(" BB", ""))

if "LS"  in earthquake["Lintang"] :
    lintang = -lintang
if "BB" in earthquake["Bujur"] :
    bujur = -bujur

info_gempa = f"""
<b> Informasi Gempa</b><br>
Tanggal: {earthquake["Tanggal"]}</br>
Waktu: {earthquake["Jam"]}</br>
Lokasi: {earthquake["Wilayah"]}</br>
Magnitude: {earthquake["Magnitude"]}</br>
Kedalaman: {earthquake["Kedalaman"]}</br>
Koordinat: {earthquake["Lintang"]},{earthquake["Bujur"]}

"""

folium.Marker(
location=[lintang, bujur],
popup=info_gempa,
tooltip=earthquake["Wilayah"],
    icon=folium.Icon(
        color="red",
        icon="map-marker",
        prefix= "fa"
    )

).add_to(peta)

peta.save("earthquake_map.html")
print("Peta berhasil dibuat")
print("File: earthquake_map.html")