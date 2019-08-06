#tax
class tax:
    def __init__(self,amount1):
        self.amount1 = amount1
    @property
    def amount(self):

        taxes = (0.05*self.amount1)
        return (taxes)

    