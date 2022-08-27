import requests

class TheSmartestHero:

    def get_all_heroes (self):
        url = f"https://akabab.github.io/superhero-api/api//all.json"
        response = requests.get(url)
        self.resp_json = response.json()
        return self.resp_json

    def get_hero_intelligence(self, hero_name):
        self.hero_dict = {hero_name : 0}
        for hero_description in self.resp_json:
            if hero_description['name'] == hero_name:
                self.hero_dict[hero_name] = hero_description['id']
                return self.hero_dict


if __name__ == '__main__':
    hulk = TheSmartestHero()
    hulk.get_all_heroes()
    hulk.get_hero_intelligence('Hulk')

    captain_america = TheSmartestHero()
    captain_america.get_all_heroes()
    captain_america.get_hero_intelligence('Captain America')

    thanos = TheSmartestHero()
    thanos.get_all_heroes()
    thanos.get_hero_intelligence('Thanos')


def hero_comparison(first_dict, second_dict, third_dict):
    sum_dict = {**first_dict, **second_dict, **third_dict}
    intelligence_level = 0
    name_of_most_intelligence = ''
    for k, v in sum_dict.items():
        if v > intelligence_level:
            intelligence_level = v
            name_of_most_intelligence = k
    print(f'Самый умный супергерой {name_of_most_intelligence} с интеллектом {intelligence_level}')


hero_comparison(hulk.get_hero_intelligence('Hulk'), captain_america.get_hero_intelligence('Captain America'), thanos.get_hero_intelligence('Thanos'))




