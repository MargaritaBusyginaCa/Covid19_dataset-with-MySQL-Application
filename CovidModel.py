import CovidView
#COMPLETED BY MARGARITA BUSYGINA

class CovidModel:
    def __init__(self, pruid, date, numconf, numdeaths, prname, prnameFR, numtoday, ratetotal):
        self.pruid = pruid
        self.date = date
        self.numconf = numconf
        self.numdeaths = numdeaths
        self.prname = prname
        self.prnameFR = prnameFR
        self.numtoday = numtoday
        self.ratetotal = ratetotal


# getters for all the attributes of a record object
def get_pruid(self):
    return self._pruid


def get_date(self):
    return self._date


def get_numconf(self):
    return self._numconf


def get_numdeaths(self):
    return self._numdeaths


def get_prname(self):
    return self._prname


def get_prnameFR(self):
    return self._prnameFR


def get_numtoday(self):
    return self._numtoday


def get_ratetotal(self):
    return self._ratetotal


# Setters for all the attributes
def set_pruid(self, x):
    self._pruid = x


def set_date(self, x):
    self._date = x


def set_numconf(self, x):
    self._numconf = x


def set_numdeaths(self, x):
    self._numdeaths = x


def set_prname(self, x):
    self._prname = x


def set_prnameFR(self, x):
    self._prnameFR = x


def set_numtoday(self, x):
    self._numtoday = x


def set_ratetotal(self, x):
    self._ratetotal = x
