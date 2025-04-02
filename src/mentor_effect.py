class MentorEffect:
    def __init__(self, mentor, mentee):
        self.mentor = mentor
        self.mentee = mentee

    def apply(self, skill_name):
        if skill_name in self.mentor.skills and self.mentor.skills[skill_name].level >= 5:
            if self.mentor.coins >= 10:
                self.mentor.coins -= 10
                self.mentee.receive_boost(skill_name)
                print(f"{self.mentor.name} mentors {self.mentee.name} for {skill_name} (10 coins).")
            else:
                print("Not enough coins for mentor effect.")
        else:
            print(f"Mentor effect not applicable: {skill_name} level < 5.")