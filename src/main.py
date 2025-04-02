from agent import Agent
from mentor_effect import MentorEffect

class GameLoop:
    def __init__(self, agents):
        self.agents = agents

    def step(self):
        for agent in self.agents:
            agent.perform_action("exploration")

if __name__ == "__main__":
    mentor = Agent("Mentor", coins=50)
    mentee = Agent("Mentee")
    mentor.skills["exploration"].level = 5  # Mentor hat Level 5
    effect = MentorEffect(mentor, mentee)
    effect.apply("exploration")
    print(f"Mentor coins left: {mentor.coins}")

    game = GameLoop([mentor, mentee])
    for _ in range(3):
        game.step()