class ResourceSharing:
    def __init__(self, agents):
        self.agents = agents

    def auto_share(self):
        total_coins = sum(agent.coins for agent in self.agents)
        share = total_coins * 0.2 / len(self.agents)  # 20% gleichmäßig
        transfer_loss = share * 0.05  # 5% Verlust
        for agent in self.agents:
            agent.coins = share * 0.95  # 95% nach Verlust
        print(f"Resources auto-shared: {share:.2f} coins per agent (5% loss).")

    def manual_share(self, giver_name, receiver_name, amount):
        giver = next(a for a in self.agents if a.name == giver_name)
        receiver = next(a for a in self.agents if a.name == receiver_name)
        if giver.coins >= amount:
            loss = amount * 0.05  # 5% Verlust
            giver.coins -= amount
            receiver.coins += (amount - loss)
            print(f"{giver_name} gave {amount} coins to {receiver_name} (-{loss:.2f} loss).")
        else:
            print(f"{giver_name} doesn’t have enough coins.")