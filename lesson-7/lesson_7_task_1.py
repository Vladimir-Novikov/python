class Matrix:
    def __init__(self):
        self.list = []
        self.new_list = []

    def __add__(self, matrix_data):
        self.list.append(matrix_data)

    def addition(self):
        if len(self.list) > 1:
            data_1 = self.list[0]
            data_2 = self.list[1]
            for i in range(len(matrix_1)):
                total = [x + y for x, y in zip(data_1[i], data_2[i])]
                self.new_list.append(total)
            return self.new_list

    def __str__(self):
        self.addition()
        if self.new_list:
            print('Сумма матриц: ')
            return '\n'.join(map(str, self.new_list))
        else:
            for q_of_matrix in range(len(self.list)):
                return '\n'.join(map(str, self.list[q_of_matrix]))


matrix = Matrix()
matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
matrix + matrix_1
print(matrix) # если одна матрица - печатаем ее
matrix + matrix_2
print(matrix) # если две матрицы - печатаем сумму матриц
