class Event:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength  # Skaliert z. B. mit Team-Ressourcen
        self.active = False
        self.warning_steps = 5  # Vorbereitungsphase

    def start_warning(self):
        self.active = False
        print(f"Warning: {self.name} approaches in {self.warning_steps} steps!")

    def trigger(self, agents):
        self.active = True
        print(f"Event {self.name} triggered! Strength: {self.strength}")
        for agent in agents:
            if agent.coins > 0:  # Nur Agenten mit Ressourcen betroffen
                loss = min(agent.coins, self.strength)
                agent.coins -= loss
                print(f"{agent.name} loses {loss} coins to {self.name}.")