from src.sign import Sign


class Rock(Sign):

    def identifier(self):
        return "R"

    def stronger_than(self):
        return ["L", "C"]

    def weaker_than(self):
        return ["P", "S"]
