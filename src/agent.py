class Agent:
    def __init__(self, name, skill_level=1, learning_rate=1.0, coins=100):
        self.name = name
        self.skill_level = skill_level
        self.learning_rate = learning_rate
        self.coins = coins
        self.boost_actions_left = 0

    def receive_boost(self):
        self.learning_rate *= 1.2  # +20% Boost
        self.boost_actions_left = 10
        print(f"{self.name} received a learning boost! New learning rate: {self.learning_rate}")

    def perform_action(self):
        if self.boost_actions_left > 0:
            self.boost_actions_left -= 1
            if self.boost_actions_left == 0:
                self.learning_rate /= 1.2  # Boost endet
                print(f"{self.name}'s boost has ended. Learning rate back to {self.learning_rate}")