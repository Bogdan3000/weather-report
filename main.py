import requests
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel

API_KEY = "03cbef3df8394785a10140200251603"
LOCATION = "Stiklestad"
URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}&aqi=no"

response = requests.get(URL)
data = response.json()

location = data["location"]
current = data["current"]
condition = current["condition"]

console = Console()

table = Table(title=f"☁️ Været i {location['name']}, {location['country']}", box=box.ROUNDED, expand=True)

table.add_column("🌟 Parameter", style="cyan bold", no_wrap=True)
table.add_column("🔎 Verdi", style="magenta")

table.add_row("🌡 Temperatur", f"{current['temp_c']} °C")
table.add_row("🤒 Føles som", f"{current['feelslike_c']} °C")
table.add_row("💨 Vind", f"{current['wind_kph']} km/t {current['wind_dir']}")
table.add_row("💧 Fuktighet", f"{current['humidity']} %")
table.add_row("☁️ Skydekke", f"{current['cloud']} %")
table.add_row("🔭 Sikt", f"{current['vis_km']} km")
table.add_row("🌞 UV-indeks", str(current['uv']))
table.add_row("🕓 Lokal tid", location["localtime"])
table.add_row("📋 Tilstand", condition["text"])

icon_url = "https:" + condition["icon"]

console.print(Panel.fit(f"[bold green]🌤 {condition['text']}[/bold green]\n\n[link={icon_url}]🖼 Klikk her for værikon[/link]", title="Værbeskrivelse", border_style="bright_blue"))
console.print(table)
