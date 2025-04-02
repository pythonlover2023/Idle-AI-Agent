from agent import Agent
from mentor_effect import MentorEffect
from event import Event
from resource_sharing import ResourceSharing

class GameLoop:
    def __init__(self, agents):
        self.agents = agents
        self.event = Event("Monster Invasion", strength=10)  # Startstärke
        self.steps_until_event = 5
        self.sharing = ResourceSharing(agents)

    def step(self):
        if self.steps_until_event > 0:
            self.steps_until_event -= 1
            if self.steps_until_event == 4:  # Warnung bei 4 Schritten
                self.event.start_warning()
            print(f"Steps until event: {self.steps_until_event}")
        elif self.steps_until_event == 0 and not self.event.active:
            self.event.trigger(self.agents)

        self.agents[1].perform_action("exploration")  # Nur Mentee arbeitet

if __name__ == "__main__":
    mentor = Agent("Mentor", coins=50)
    mentee = Agent("Mentee", coins=20)
    mentor.skills["exploration"].level = 5
    effect = MentorEffect(mentor, mentee)
    effect.apply("exploration")
    print(f"Mentor coins: {mentor.coins}, Mentee coins: {mentee.coins}")

    game = GameLoop([mentor, mentee])
    sharing = ResourceSharing([mentor, mentee])
    sharing.manual_share("Mentor", "Mentee", 20)  # Beispiel für manuelles Teilen

    for _ in range(6):  # 6 Schritte, um Event zu triggern
        game.step()