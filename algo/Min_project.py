import threading

# Function for single-threaded matrix multiplication
def matrix_multiply(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    # Matrix multiplication logic
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
    return result

# Function for multithreaded matrix multiplication with one thread per row
def multiply_row(row, matrix1, matrix2, result):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[row][j] += matrix1[row][k] * matrix2[k][j]

def multithreaded_matrix_multiply_row(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    threads = []
    
    # Create threads for each row
    for i in range(len(matrix1)):
        thread = threading.Thread(target=multiply_row, args=(i, matrix1, matrix2, result))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    return result

# Function for multithreaded matrix multiplication with one thread per cell
def multiply_cell(i, j, matrix1, matrix2, result):
    for k in range(len(matrix2)):
        result[i][j] += matrix1[i][k] * matrix2[k][j]

def multithreaded_matrix_multiply_cell(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    threads = []
    
    # Create threads for each cell
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            thread = threading.Thread(target=multiply_cell, args=(i, j, matrix1, matrix2, result))
            threads.append(thread)
            thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    return result

# Example usage and comparison
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Single-threaded matrix multiplication
result_single_threaded = matrix_multiply(matrix1, matrix2)
print("Single-Threaded Result:", result_single_threaded)

# Multithreaded matrix multiplication with one thread per row
result_multithreaded_row = multithreaded_matrix_multiply_row(matrix1, matrix2)
print("Multithreaded (One Thread Per Row) Result:", result_multithreaded_row)

# Multithreaded matrix multiplication with one thread per cell
result_multithreaded_cell = multithreaded_matrix_multiply_cell(matrix1, matrix2)
print("Multithreaded (One Thread Per Cell) Result:", result_multithreaded_cell)