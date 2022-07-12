"""
Сериализация JSON

Прочитайле data в строку
Создайте файл - data_file.json и запишите в него data
"""
data = {
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
import json

print("Cериализация JSON")
print (json.dumps(data))

out_file = open("data_file.json", "w")

json.dump(data, out_file, indent = 6)
out_file.close()


