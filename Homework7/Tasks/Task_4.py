class KeyValueStorage():
    my_dict = {}

    def __init__(self, path):
        self.path = path
        self.read_a_file()

    def read_a_file(self):
        with open(self.path) as file:
            while True:
                line = file.readline().split('=')
                if line == ['']:
                    break

                if not hasattr(self, line[0]):
                    setattr(self, line[0], line[1][0:len(line[1]) - 1])# using the setter we added the attributes.
                    self.my_dict[line[0]] = line[1][0:len(line[1]) - 1]#adding new elements to the dictionary.1 value=key, 2 value=value.


    def __getitem__(self, key): #created an iterator to access elements not through attributes
        return self.my_dict[key]


storage = KeyValueStorage('Task_04')
print(storage['name'])  # will be string 'kek'
print(storage.song)  # will be 'shadilay'
print(storage.power)  # will be integer 9001
print(storage.variant)
print(storage['test'])


