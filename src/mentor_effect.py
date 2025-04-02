class MentorEffect:
    def __init__(self, mentor, mentee):
        self.mentor = mentor
        self.mentee = mentee

    def apply(self):
        if self.mentor.skill_level >= 5 and self.mentor.coins >= 10:
            self.mentor.coins -= 10
            self.mentee.receive_boost()
            print(f"{self.mentor.name} mentors {self.mentee.name} for 10 coins.")
        else:
            print("Mentor effect not applicable: Skill level < 5 or not enough coins.")