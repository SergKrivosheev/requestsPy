import requests
from pprint import pprint


def heroes_intelligence():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    all_heroes = response.json()
    heroes_to_find = ['Hulk', 'Captain America', 'Thanos']
    smartest_hero = ''
    intel_ = 0
    for hero in heroes_to_find:
        for hero_ in all_heroes:
            if hero_['name'] == hero:
                if hero_['powerstats']['intelligence'] > intel_:
                    intel_ = hero_['powerstats']['intelligence']
                    smartest_hero = hero_['name']
    pprint(f'The smartest hero is {smartest_hero} and his/her intelligence is {intel_}')

if __name__ == '__main__':
    heroes_intelligence()