import numpy as np

def transpose2d(input_matrix: list[list[float]]) -> list:
    """
    Transpose the axis of a 2D list (matrix) of numbers.

    Args:
    input_matrix (list[list[float]]): A 2D list of floats.

    Returns:
    list[list[float]]: The transposed 2D list.
    """
    result = [[
    input_matrix[i][j]
    for i in range(len(input_matrix))]
    for j in range(len(input_matrix[0]))]
    return result

def window1d(input_array: np.ndarray, size: int, shift: int, stride: int) -> list:
    """
    Create a list of windows from a 1D numpy array.

    Args:
    input_array (np.ndarray): Input array.
    size (int): Number of elements in each window.
    shift (int): Number of elements to shift the window by on each step.
    stride (int): The stride between elements within a window.

    Returns:
    list: A list of windows, where each window is a list of elements from the input array.
    """
    result = []   
    start = 0   
    while start + size * stride <= len(input_array):
        window = []
        for i in range(size):
            index = start + i * stride  
            if index < len(input_array):  
                window.append(input_array[index]) 
        result.append(window)  
        start += shift  
    return result 

def convolution2d(input_matrix: np.ndarray, kernel: np.ndarray, stride: int) -> np.ndarray:
    """
    Apply a 2D convolution using a given kernel to the given matrix.

    Args:
    input_matrix (np.ndarray): Input 2D matrix.
    kernel (np.ndarray): Convolution kernel, a smaller 2D matrix.
    stride (int): Stride of the convolution.

    Returns:
    np.ndarray: The convolved matrix.
    """
    kernel_height, kernel_width = kernel.shape
    input_height, input_width = input_matrix.shape
    output_height = (input_height - kernel_height) // stride + 1
    output_width = (input_width - kernel_width) // stride + 1
    output_matrix = np.zeros((output_height, output_width))
    for y in range(output_height):
        for x in range(output_width):
            region = input_matrix[y * stride:y * stride + kernel_height,
                                  x * stride:x * stride + kernel_width]
            output_matrix[y, x] = np.sum(region * kernel)
    return output_matrix
