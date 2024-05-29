import sys
from sparse_matrix import SparseMatrix


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <matrix1_file> <matrix2_file> <operation>")
        print("Operations: add, subtract, multiply")
        return


    matrix1_file = sys.argv[1]
    matrix2_file = sys.argv[2]
    operation = sys.argv[3]


    try:
        matrix1 = SparseMatrix.from_file(matrix1_file)
        matrix2 = SparseMatrix.from_file(matrix2_file)
    except Exception as e:
        print(f"Error: {e}")
        return


    try:
        if operation == "add":
            result = matrix1.add(matrix2)
            result_file = "result_add.txt"
        elif operation == "subtract":
            result = matrix1.subtract(matrix2)
            result_file = "result_subtract.txt"
        elif operation == "multiply":
            result = matrix1.multiply(matrix2)
            result_file = "result_multiply.txt"
        else:
            print("Invalid operation")
            return


        result.to_file(result_file)
        print(f"Result written to {result_file}")


    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
