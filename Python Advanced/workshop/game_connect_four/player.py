class Player:

    def __init__(self, name: str, start_number):
        self._name = name
        self._start_number = start_number


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def start_number(self):
        return self._start_number

    @start_number.setter
    def start_number(self, value):
        self._start_number = value

