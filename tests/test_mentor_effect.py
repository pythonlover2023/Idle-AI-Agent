import unittest
from agent import Agent
from mentor_effect import MentorEffect

class TestMentorEffect(unittest.TestCase):
    def test_apply_boost(self):
        mentor = Agent("Mentor", coins=50)
        mentor.skills["exploration"].level = 5
        mentee = Agent("Mentee")
        effect = MentorEffect(mentor, mentee)
        effect.apply("exploration")
        self.assertEqual(mentee.learning_rate, 1.2)
        self.assertEqual(mentor.coins, 40)

if __name__ == "__main__":
    unittest.main()