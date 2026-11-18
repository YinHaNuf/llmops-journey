class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def upgrade(self, bonus):
        self.score+=bonus
        if self.score>=100:
            self.score=100



