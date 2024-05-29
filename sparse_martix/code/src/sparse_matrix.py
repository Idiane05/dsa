class SparseMatrix:
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.data = {}


    @staticmethod
    def from_file(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()


        rows = int(lines[0].strip().split('=')[1])
        cols = int(lines[1].strip().split('=')[1])
        matrix = SparseMatrix(rows, cols)


        for line in lines[2:]:
            line = line.strip()
            if not line:
                continue
            try:
                entry = line.strip('()').split(',')
                if len(entry) != 3:
                    raise ValueError("Input file has wrong format")
                row, col, value = map(int, entry)
                matrix.set_element(row, col, value)
            except ValueError:
                raise ValueError("Input file has wrong format")
       
        return matrix


    def get_element(self, row, col):
        return self.data.get((row, col), 0)


    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]


    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match for addition")
       
        result = SparseMatrix(self.rows, self.cols)
        for key in set(self.data.keys()).union(other.data.keys()):
            result.set_element(key[0], key[1], self.get_element(key[0], key[1]) + other.get_element(key[0], key[1]))
       
        return result


    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match for subtraction")
       
        result = SparseMatrix(self.rows, self.cols)
        for key in set(self.data.keys()).union(other.data.keys()):
            result.set_element(key[0], key[1], self.get_element(key[0], key[1]) - other.get_element(key[0], key[1]))
       
        return result


    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrices dimensions do not match for multiplication")
       
        result = SparseMatrix(self.rows, other.cols)
        for (i, k) in self.data.keys():
            for j in range(other.cols):
                result.set_element(i, j, result.get_element(i, j) + self.get_element(i, k) * other.get_element(k, j))
       
        return result


    def to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"rows={self.rows}\n")
            file.write(f"cols={self.cols}\n")
            for (row, col), value in self.data.items():
                file.write(f"({row}, {col}, {value})\n")


    def __str__(self):
        result = []
        for (row, col), value in self.data.items():
            result.append(f"({row}, {col}, {value})")
        return "\n".join(result)