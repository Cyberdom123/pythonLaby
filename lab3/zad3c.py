import pandas as pd
import csv

class Cacher:
    def __init__(self, filename="cache.csv"):
        self.filename = filename
        try:
            self.df = pd.read_csv(self.filename,sep=',', index_col=0, header=None )
        except:
            self.df = pd.DataFrame()
    
    def load_cache(self, key):
        result = True

        try:
            self.df = pd.read_csv(self.filename,sep=',', index_col=0, header=None)
            cache = self.df.to_dict()
        except:
            cache = {}

        # print(cache)
        try:
            value = cache[1][key]
            # print(f"Znaleziono parametr o kluczu {key}")
        except:
            # print(f"Nie znaleziono parametru o kluczu {key}")
            result = False
            value = 0

        return result, value
        
    def save_to_cache(self, key, value):
        with open(self.filename, 'a') as file:
            file.write(f"{key},{value}\n")
        
        

def cache(function):
    cacher = Cacher(f"{function.__name__}.csv")

    def wrapper(x, **kwargs):
        result, value = cacher.load_cache(x)

        if result:
            return value
        else:
            value = function(x, **kwargs)
            if dump := kwargs.get("dump"):
                cacher.save_to_cache(x, value)
            return value

    return wrapper

@cache
def fibonacci(n, **kwargs):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1, dump=False) + fibonacci(n - 2, dump=False)

cacher = Cacher()

a, y = cacher.load_cache(22)
print(y)
# fibonacci = cache(fibonacci)
print(fibonacci(8, dump=True))
# cacher.save_to_cache(112, 221)