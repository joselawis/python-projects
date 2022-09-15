import json
import urllib.request
from urllib.error import HTTPError


class CardPack(object):
    def __init__(self, data):
        self.name = data["name"]
        cards_data = data["cards"]
        self.cards = sorted(list(map(lambda card: Card(card), cards_data)))


class Card(object):
    def __init__(self, data):
        self.description = data["description"]

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.description == other.description
        return False

    def __hash__(self):
        return hash(self.description)

    def __lt__(self, other):
        return self.description < other.description


def get_duplicates(my_list):
    new_list = []
    dup_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
        else:
            dup_list.append(i)
    return dup_list


def print_descriptions(text, my_list):
    print(text, *map(lambda d: d.description, my_list), sep='\n- ')


def analyse_pack(card_pack):
    print(f"Name: {card_pack.name}")
    print(f"There are {len(card_pack.cards)} cards")

    # Obtaining unique card by using set()
    print(f"There are {len(set(card_pack.cards))} unique cards")
    # print_descriptions("Cards:", pack.cards)

    # Obtaining duplicated cards
    duplicates = sorted(set(get_duplicates(card_pack.cards)))
    print(f"There are {len(duplicates)} duplicates")
    if len(duplicates) == 0:
        print("- There is no duplicated cards")
    else:
        print_descriptions("Duplicated:", duplicates)


try:
    print("Hi! This is a free duplicated cards checker for Streamloots")
    user = input("What user do you want to check?: ")
    url = "https://api.streamloots.com/pages/%s/sets" % user

    # Send a request to url
    with urllib.request.urlopen(url) as response:
        json_data = json.loads(response.read())
        # Parse data to CardPack object
        card_packs = list(map(lambda data: CardPack(data), json_data["data"]))

        # Iterate the CardPack list
        for pack in card_packs:
            analyse_pack(pack)


except HTTPError:
    print("That user was not found :(")
