class Symbol(object):
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplemented
    def __hash__(self):
        return hash(self.value)
        
if __name__ == "__main__":
    x = Symbol("Py")
    y = Symbol("Py")

    symbols = set() # Set is immutable 
    symbols.add(x)  # but this is unhashable because this object mutable
    symbols.add(y)

    print(x is y)
    print(x == y)
    print(len(symbols))

