import numpy as np


def convolution_2Dshape(height, width, channels, stride, kernel, padding):
    height_out = (height)
    width_out = (width)

def convolution_1Dshape(len_in, padding, dilation, k_size, stride):
    len_out = len_in + (2*padding) - (dilation * (k_size-1)) - 1
    len_out /= stride
    len_out += 1
    return len_out


class MatrixSolver3Var():
    operations = ["addition", "subtract", "multiply", "divide"]

    def __init__(self, input_matrix):
        self.history = []
        self.matrix = np.array(input_matrix)

        self.history.append(input_matrix)
        self.math_history = self.get_display(input_matrix)

    def get_display(self, matrix):
        outstr = (
            f"\n= = = = = = = = = = = = = = = = = = = =" +\
            f"\n{matrix[0][0]}\t{matrix[0][1]}\t{matrix[0][2]}\t|\t{matrix[0][3]}" +\
            f"\n{matrix[1][0]}\t{matrix[1][1]}\t{matrix[1][2]}\t|\t{matrix[1][3]}" +\
            f"\n{matrix[2][0]}\t{matrix[2][1]}\t{matrix[2][2]}\t|\t{matrix[2][3]}" +\
            f"\n= = = = = = = = = = = = = = = = = = = ="
        )
        return outstr

    def display_matrix(self, matrix=None):
        if matrix is None:
            matrix = self.matrix
        print(self.get_display(matrix))
    

    def display_history(self):
        for m in self.history:
            self.display_matrix(m)
            print("\n")

    def transform_line(self, line_number: int, operation: str, number, save=True):
        line = self.matrix[line_number]
        line_history = f"\n\nLine {line_number}"

        if operation.lower() in "addition":
            line_history += f" plus {number}"
            line = np.add(line, number)
        elif operation.lower() in "subtraction":
            line_history += f" minus {number}"
            line = np.subtract(line, number)
        elif operation.lower() in "multiply":
            line_history += f" times {number}"
            line = np.multiply(line, number)
        elif operation.lower() in "divide":
            line_history += f" divided by {number}"
            line = np.divide(line, number)

        line_history += f"\n{self.matrix[line_number]} -> {line}\n"

        self.math_history += line_history
        if save:
            self.matrix[line_number] = line
            self.history.append(self.matrix)
            self.math_history += self.get_display(self.matrix)
        return line

    def transpose_line(self, line_num1, line_num2):
        self.math_history += f"\n\nTransposing line {line_num1} with {line_num2}."

        line1 = np.copy(self.matrix[line_num1])
        line2 = np.copy(self.matrix[line_num2])

        self.matrix[line_num1] = line2
        self.matrix[line_num2] = line1

        self.math_history += f"\n{self.get_display(self.history[-1])} \n\t TO: {self.get_display(self.matrix)}"

    def auto_solve(self):
        self.transform_line(1, "sub", self.transform_line(0, "mult", self.matrix[1][0]/self.matrix[0][0], False))
        self.transform_line(2, "sub", self.transform_line(0, "mult", self.matrix[2][0]/self.matrix[0][0], False))

        self.transform_line(2, "sub", self.transform_line(1, "mult", self.matrix[2][1]/self.matrix[1][1], False))

        self.transform_line(2, "div", self.matrix[2][2])

        self.transform_line(1, "div", self.matrix[1][1])
        self.transform_line(1, "sub", self.transform_line(2, "mult", self.matrix[1][2], False))

        self.transform_line(0, "div", self.matrix[0][0])
        self.transform_line(0, "sub", self.transform_line(1, "mult", self.matrix[0][1], False))
        self.transform_line(0, "sub", self.transform_line(2, "mult", self.matrix[0][2], False))


if __name__ == "__main__":
    s1 = convolution_1Dshape(6000, 0, 1, 4, 1)
    s2 = convolution_1Dshape(s1, 0, 1, 8, 1)
    s3 = convolution_1Dshape(s2, 0, 1, 16, 1)
    s4 = convolution_1Dshape(s3, 0, 1, 1, 1)
    print(s1, s2, s3, s4)