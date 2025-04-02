class Agent:
    def __init__(self, name, coins=100):
        self.name = name
        self.coins = coins
        self.skills = {"exploration": Skill("Exploration"), "combat": Skill("Combat")}
        self.learning_rate = 1.0
        self.boost_actions_left = 0

    def receive_boost(self, skill_name):
        self.learning_rate *= 1.2  # Platz für boost_modifier später
        self.boost_actions_left = 10
        print(f"{self.name} received a boost for {skill_name}! New learning rate: {self.learning_rate}")

    def perform_action(self, skill_name):
        if skill_name in self.skills:
            self.skills[skill_name].improve(self.learning_rate)
        if self.boost_actions_left > 0:
            self.boost_actions_left -= 1
            if self.boost_actions_left == 0:
                self.learning_rate /= 1.2
                print(f"{self.name}'s boost has ended. Learning rate back to {self.learning_rate}")