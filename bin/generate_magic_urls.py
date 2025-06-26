import json
import urllib.parse

with open("bayernatlas/items.json", "r", encoding="utf-8") as f:
    items = f.read()
    items = json.loads(items)
    items = items["items"][0]["items"]

for item in items:
    name = item["name"]
    url_template = urllib.parse.quote_plus(item["url"], safe="")
    min_zoom = item["minZoom"]
    max_zoom = item["maxZoom"]

    magic_url = f"http://osmand.net/add-tile-source?name={name}&min_zoom={min_zoom}&max_zoom={max_zoom}&url_template={url_template}"
    html = f"""<a href="{magic_url}">{name}</a>"""
    print(html)
