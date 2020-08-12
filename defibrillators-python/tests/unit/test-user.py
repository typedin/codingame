import unittest
from src.solution import User, StringToDecimal


class UserTest(unittest.TestCase):
    def test_a_user_cannot_be_instanciate_with_the_wrong_list(self):
        lines = ["3.879483", "43.608177", "appleSauce"]
        with self.assertRaises(ValueError):
            User(lines, StringToDecimal)

    def test_a_user_has_longitude_and_a_latitude(self):
        lines = ["3.879483", "43.608177"]

        user = User(lines, StringToDecimal)

        assert user.lon == 3.879483
        assert user.lat == 43.608177
