import unittest
from agent import Agent
from mentor_effect import MentorEffect

class TestMentorEffect(unittest.TestCase):
    def test_apply_boost(self):
        mentor = Agent("Mentor", skill_level=5, coins=50)
        mentee = Agent("Mentee", skill_level=1)
        effect = MentorEffect(mentor, mentee)
        effect.apply()
        self.assertEqual(mentee.learning_rate, 1.2)
        self.assertEqual(mentor.coins, 40)

if __name__ == "__main__":
    unittest.main()