from agent import Agent
from mentor_effect import MentorEffect

if __name__ == "__main__":
    mentor = Agent("Mentor", skill_level=5, coins=50)
    mentee = Agent("Mentee", skill_level=1)
    effect = MentorEffect(mentor, mentee)
    effect.apply()
    print(f"Mentor coins left: {mentor.coins}")