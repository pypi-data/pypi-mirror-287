import numpy as np

def convolution2d(input_matrix: np.ndarray, kernel: np.ndarray, stride: int = 1) -> np.ndarray:
    """
    Performs a 2D convolution operation on the given input matrix using the specified kernel and stride.

    Parameters:
    ----------
    input_matrix : np.ndarray
        A 2D Numpy array of real numbers representing the input matrix to be convolved.
    kernel : np.ndarray
        A 2D Numpy array of real numbers representing the convolution kernel.
    stride : int, optional
        An integer greater than 0 that determines the stride (step size) for moving the kernel across the input matrix. Default is 1.

    Returns:
    -------
    np.ndarray
        A 2D Numpy array of real numbers representing the result of the convolution operation.

    Raises:
    ------
    TypeError
        If `input_matrix` or `kernel` is not a Numpy ndarray, or if `stride` is not a positive integer.

    Example:
    -------
    >>> input_matrix = np.array([
    ...     [1.0, 2.0, 3.0],
    ...     [4.0, 5.0, 6.0],
    ...     [7.0, 8.0, 9.0]
    ... ])
    >>> kernel = np.array([
    ...     [1.0, 0.0],
    ...     [0.0, -1.0]
    ... ])
    >>> stride = 1
    >>> convolution2d(input_matrix, kernel, stride)
    array([
        [ 6.0,  6.0],
        [ 0.0, -6.0]
    ])
    """
    # Type checks
    if not isinstance(input_matrix, np.ndarray):
        raise TypeError("input_matrix must be a numpy ndarray")
    if not isinstance(kernel, np.ndarray):
        raise TypeError("kernel must be a numpy ndarray")
    if not isinstance(stride, int) or stride <= 0:
        raise TypeError("stride must be a positive integer")
    
    # Get dimensions
    input_matrix_h, input_matrix_w = input_matrix.shape
    kernel_h, kernel_w = kernel.shape

    # Calculate dimensions of the output matrix
    output_matrix_h = (input_matrix_h - kernel_h) // stride + 1
    output_matrix_w = (input_matrix_w - kernel_w) // stride + 1
    
    # Initialize the output matrix
    output_matrix = np.zeros((output_matrix_h, output_matrix_w))

    # Perform the convolution operation
    for i in range(0, output_matrix_h):
        for j in range(0, output_matrix_w):
            output_matrix[i, j] = (input_matrix[i*stride:i*stride+kernel_h, j*stride:j*stride+kernel_w] * kernel).sum()

    return output_matrix
