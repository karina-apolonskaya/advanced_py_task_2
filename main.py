import requests
import json
import hashlib

URL = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"

class FindLink:

    def __init__(self, URL):
        self.url = URL
        self.response = requests.get(URL)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.response.json()):
            raise StopIteration
        country_index = self.response.json()[self.index]
        country_name = country_index["name"]
        common_name = country_name["common"]
        wiki_address = f"https://en.wikipedia.org/wiki/{common_name}"
        wiki_address = wiki_address.replace(" ", "_")
        # final_address = common_name + ":" + " " + wiki_address
        return common_name, wiki_address

def get_hash(path):
    with open(path, encoding="utf-8") as iter_file:
        python_file = json.load(iter_file)
        for country in python_file:
            print(country + ":" + " " + python_file[country])
            hash_object = hashlib.md5(country.encode())
            yield hash_object.hexdigest()

if __name__ == "__main__":
    json_dict = dict()
    with open("countries.json", "w", encoding='utf-8') as f:
        for name, address in FindLink("https://raw.githubusercontent.com/mledoze/countries/master/countries.json"):
            json_dict[name] = address
        f.write(json.dumps(json_dict, ensure_ascii=False))
        print("Файл успешно записан!")
    for wiki_address in get_hash("countries.json"):
        print(wiki_address)





     