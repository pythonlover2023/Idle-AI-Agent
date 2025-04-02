from agent import Agent
from mentor_effect import MentorEffect

class GameLoop:
    def __init__(self, agents):
        self.agents = agents

    def step(self):
        # Nur der Mentee führt Aktionen aus, nicht der Mentor
        self.agents[1].perform_action("exploration")  # Index 1 = Mentee

if __name__ == "__main__":
    mentor = Agent("Mentor", coins=50)
    mentee = Agent("Mentee")
    mentor.skills["exploration"].level = 5  # Mentor startet bei Level 5
    effect = MentorEffect(mentor, mentee)
    effect.apply("exploration")
    print(f"Mentor coins left: {mentor.coins}")

    game = GameLoop([mentor, mentee])
    for _ in range(3):  # 3 Schritte als Beispiel
        game.step()