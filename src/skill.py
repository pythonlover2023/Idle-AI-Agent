class Skill:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def improve(self, learning_rate):
        self.level += learning_rate
        print(f"Skill {self.name} improved to level {self.level:.2f}")