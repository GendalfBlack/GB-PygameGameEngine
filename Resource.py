class InGameResource:

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        if callable(self.update):
            self.update()

    def __init__(self):
        self.name = "Default"
        self._amount = 0
        self.hide = False
        self.update = None
