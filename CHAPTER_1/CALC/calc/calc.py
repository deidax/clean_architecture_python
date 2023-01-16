from functools import reduce
class Calc:
    
    def add(self, *args):
        return sum(args)
    
    def sub(self,a, b):
        return a-b
    
    def mult(self, *args):
        if not all(args): raise ValueError
        return reduce(lambda a, b: a*b, args)
    
    def div(self, a, b):
        return a / b if b != 0 else 'inf'
    
    def avg(self, num, ut=None, lt=None):
        if len(num) == 0: return 0
        if ut is not None: num = list(filter(lambda x: x <= ut, num))
        if lt is not None: num = list(filter(lambda x: x >= lt, num))
        return self.div(self.add(*num), len(num)) if len(num) != 0 else 0