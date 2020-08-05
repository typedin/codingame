from src.sign import Sign


class Spock(Sign):

    def identifier(self):
        return "S"

    def stronger_than(self):
        return ["C", "R"]

    def weaker_than(self):
        return ["P", "L"]
