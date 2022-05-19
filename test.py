import json
with open("bib_find/bibles/EntireBible-DR.json", 'r', encoding="UTF-8") as f:
    bible = json.load(f)

print(bible["Luke"]["1"])