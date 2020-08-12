import math
from decimal import Decimal


class StringConverter:
    def __init__(self, aString):
        if not isinstance(aString, str):
            raise ValueError("A string must be provided")

        self.string = aString

    def parse(self):
        raise Exception("This method must be implemented ")


class StringToDecimal(StringConverter):

    def parse(self):
        return float(self.string.replace(',', '.'))


class User():

    def __init__(self, lines, aStringConverter):
        if len(lines) != 2:
            raise ValueError(
                "A list with two entries must be passed as argument \
                (got {})".format(len(lines))
            )
        self.lon = aStringConverter(lines[0]).parse()
        self.lat = aStringConverter(lines[1]).parse()


class Defibrilator():
    def __init__(self, anEntry, aStringConverter):
        if not isinstance(anEntry, list):
            raise ValueError("Entry must be passed as a list")

        if len(anEntry) != 6:
            raise ValueError("Wrong length for entry: expected 6 got {}".format(len(anEntry)))

        self._lines = anEntry

        if not issubclass(aStringConverter, StringConverter):
            raise ValueError("StringConverter is expected")
        self._converter = aStringConverter

    def name(self):
        return self._lines[1]

    def address(self):
        return self._lines[2]

    def lon(self):
        return self._converter(self._lines[4]).parse()

    def lat(self):
        return self._converter(self._lines[5]).parse()


class Algorithm:
    def __init__(self, aUser, defibrilators):
        if not isinstance(aUser, User):
            raise ValueError("A valid user is required")
        self._user = aUser

        if not len(defibrilators):
            raise ValueError("No defibrilators were passed")

        for index in range(len(defibrilators)):
            if not isinstance(defibrilators[index], Defibrilator):
                raise ValueError("Invalid defibrilator was passed at index: {}".format(index))

        self._defibrilators = defibrilators

    def _distanceBetweenUserAndDefibrilator(self, defibrilator):
        return math.sqrt(
            ((defibrilator.lat() - self._user.lat)**2)
            +
            ((defibrilator.lon() - self._user.lon)**2)
        )


class Solution:
    def __init__(self, lines, aStringConverter):
        if not isinstance(lines, list):
            raise ValueError("A valid array of lines must be passed")
        self._lines = lines

        if not isinstance(aStringConverter, type(StringConverter)):
            raise ValueError("A valid StringConverter must be passed")
        self._converter = aStringConverter

        self._user = self._createUser()
        self._defibrilators = self._createDefibrilators()

    def user(self):
        return self._user

    def defibrilators(self):
        return self._defibrilators

    def _createUser(self):
        return User(self._lines[:2], self._converter)

    def _createDefibrilators(self):
        return [
            Defibrilator(line.split(";"), self._converter)
            for line in self._lines[3:]
        ]

    def getClosest(self, distanceCalculator):
        algorithm = distanceCalculator(self._user, self._defibrilators)
        return sorted(
            [
                {
                    "distance": algorithm._distanceBetweenUserAndDefibrilator(defibrilator),
                    "defibrilator": defibrilator
                }
                for defibrilator in self._defibrilators
            ], key=lambda k: k["distance"])[0]["defibrilator"]
