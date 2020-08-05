from src.sign import Sign


class Paper(Sign):

    def identifier(self):
        return "P"

    def stronger_than(self):
        return ["R", "S"]

    def weaker_than(self):
        return ["C", "L"]
