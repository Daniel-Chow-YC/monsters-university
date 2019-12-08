class Monster():

    def __init__(self, name):
        self.name = name
        self.skills = []

    def sleep(self):
        return 'zzzzzzzz...'

    def eat(self, food):
        return f"Nom, nom {food} is good!"

    def scare_attack(self):
        return "RAAAHHHH (╯°□°)╯"

    def add_skill(self, list_of_skills):
        self.skills.extend(list_of_skills)

# example_monster = Monster('Jim')
# example_monster.add_skill(['scary', 'angry'])
# print(example_monster.skills)