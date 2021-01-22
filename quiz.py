
AGREE_SCORE = 1
DISAGREE_SCORE = 1
PASSIVE_SCORE = 0

parties_scores = {
    "יהדות התורה": 0,
    "הליכוד": 0,
    "מרצ": 0,
    "ישראל ביתנו": 0,
    "הבית היהודי": 0,
    "הרשימה המשותפת": 0,
    "יש עתיד": 0,
    "שס": 0,
    "כחול לבן": 0,
    "העבודה": 0,
}


class VoteEnum:
    AGREE = 2,
    DISAGREE = 0,
    PASSIVE = 1


class Question:
    def __init__(self, content: str, parties: dict):
        self.content = content
        self.parties = parties

    def show_question(self, answer: str, scores: dict):
        if answer == 'y':
            self.yes(scores)
        elif answer == 'n':
            self.no(scores)
        elif answer == 'passive':
            self.passive(scores)

    def yes(self, scores):
        global parties_scores

        for party, opinion in self.parties.items():
            if opinion == VoteEnum.AGREE:
                scores[party] += AGREE_SCORE

    def no(self, scores):
        for party, opinion in self.parties.items():
            if opinion == VoteEnum.DISAGREE:
                scores[party] += DISAGREE_SCORE

    def passive(self, scores):
        for party, opinion in self.parties.items():
            if opinion == VoteEnum.PASSIVE:
                scores[party] += PASSIVE_SCORE
