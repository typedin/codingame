from src.sign import Sign


class Scissors(Sign):

    def identifier(self):
        return "C"

    def stronger_than(self):
        return ["P", "L"]

    def weaker_than(self):
        return ["R", "S"]
