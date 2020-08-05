from src.sign import Sign


class Lizard(Sign):

    def identifier(self):
        return "L"

    def stronger_than(self):
        return ["P", "S"]

    def weaker_than(self):
        return ["R", "C"]
