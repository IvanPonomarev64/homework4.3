nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']
]


class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):    
        self.item = sum(self.nested_list, [])
        return iter(self.item)

    def __next__(self):
        return self

for item in FlatIterator(nested_list):
	print(item)       
        
