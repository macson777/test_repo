from random import randint


class Matrix:
    def __init__(self, data=None):
        if not data:
            data = []
            for i in range(5):
                row = []
                for j in range(5):
                    row.append((randint(0, 9)))
                data.append(row)
            self.n = 5
            self.m = 5
        else:
            self.n = len(data)
            self.m = len(data[0])
        self.data = data

    def __str__(self):
        result = ''
        for row in self.data:
            result += ' '.join(map(str, row)) + '\n'
        return result

    def __getitem__(self, i):
        return self.data[i]


