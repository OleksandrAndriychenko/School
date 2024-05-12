class NegativeDegree(Exception):
    pass
class Calculator(float):
    def __truediv__(self, other):
        try:
            return float(self) / float(other)
        except ZeroDivisionError:
            return 0
    def __add__(self, other):
        try:
            return float(self) + float(other)
        except Exception:
            return 0
    def __sub__(self, other):
        try:
            return float(self) - float(other)
        except Exception:
            return 0
    def __mul__(self, other):
        try:
            return float(self) * float(other)
        except Exception:
            return 0
    def __pow__(self, power, modulo=None):
        try:
            if power >= 0:
                return float(self) ** float(power)
            else:
                raise NegativeDegree
        except Exception:
            return 0
