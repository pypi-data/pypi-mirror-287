[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)

## Data Transformation Library

This project is a POC for a Python library designed to assist data scientists with data transformations.

### Key Features:

This library consists of 3 functions: Transpose, Time Series Windowing and Cross-Correlation.
Here's a brief explanation of these functions:

1. **Transpose:** Transposes a given matrix (2D tensor).

    - **Function Signature:**

    ```python
    def transpose2d(input_matrix: list[list[float]]) -> list[list[float]]:
    ```

    - **Parameters:**
    `input_matrix`: A list of lists of real numbers, where each inner list represents a row in the matrix.

    - **Returns:**
    A new list of lists representing the transposed matrix, where the rows of the original matrix become the columns of the new matrix, and the columns of the original matrix become the rows of the new matrix.

    - **Example:**

    ```python
    # Input
    input_matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
    ]

    # Output
    output_matrix = [
    [1.0, 4.0],
    [2.0, 5.0],
    [3.0, 6.0]
    ]
    ```
    In this example, the input matrix with dimensions 2x3 (2 rows and 3 columns) is transformed into an output matrix with dimensions 3x2 (3 rows and 2 columns).

2. **Window Extraction:** Extracts overlapping windows from a 1D array with specified size, shift, and stride.

    - **Function Signature:**

    ```python
    def window1d(input_array: list | np.ndarray, size: int, shift: int = 1, stride: int = 1) -> list[list | np.ndarray]:
    ```
    
    - **Parameters:**
    `input_array`: A list or 1D Numpy array of real numbers.
    `size`: A positive integer that determines the size (length) of each window.
    `shift`: A positive integer that determines the shift (step size) between different windows. Default is 1.
    `stride`: A positive integer that determines the stride (step size) within each window. Default is 1.

    - **Returns:**
    A list of lists or 1D Numpy arrays of real numbers, where each element represents a window extracted from the input array according to the specified parameters.

    - **Example:**

    ```python
    # Input
    input_array = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    size = 3
    shift = 2
    stride = 1

    # Output
    output_matrix = [
    [1.0, 2.0, 3.0],
    [3.0, 4.0, 5.0]
    ]
    ```
    In this example, the input array [1.0, 2.0, 3.0, 4.0, 5.0, 6.0] is processed with a window size of 3, a shift of 2, and a stride of 1. This results in extracting windows of length 3 from the input array, where each new window starts 2 elements after the previous one, and each window advances one element at a time.

3. **Cross-Correlation:** Applies a 2D convolution operation on a matrix using a given kernel and stride.

    - **Function Signature:**

    ```python
    def convolution2d(input_matrix: np.ndarray, kernel: np.ndarray, stride: int = 1) -> np.ndarray:
    ```
    
    - **Parameters:**
    `input_matrix`: A 2D Numpy array of real numbers representing the input matrix to be convolved.
    `kernel`: A 2D Numpy array of real numbers representing the convolution kernel.
    `stride`: An integer greater than 0 that determines the stride (step size) for moving the kernel across the input matrix. Default is 1.

    - **Returns:**
    A 2D Numpy array of real numbers representing the result of applying the convolution operation. The output matrix will have reduced dimensions compared to the input matrix, depending on the size of the kernel and the stride.

    - **Example:**

    ```python
    # Input
    input_matrix = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
    ])
    kernel = np.array([
    [1.0, 0.0],
    [0.0, -1.0]
    ])
    stride = 1

    # Output
    output_matrix = np.array([
    [ 6.0,  6.0],
    [ 0.0, -6.0]
    ])
    ```
    In this example, the input_matrix is convolved with the kernel using a stride of 1. The resulting output_matrix is a 2D array where each element represents the result of applying the kernel to the corresponding region of the input matrix.

### Installation

Follow these steps to initialize and run this Poetry-based project in a new environment.

1. The library is available on PyPI and can be installed using pip:

    ```bash
    pip install data-transformation-library-jmarci
    ```

**Alternatively:** Clone this repository from your version control system (e.g., GitHub, GitLab).

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Ensure that Poetry is installed in your new environment. If not, you can install it using the official installation script:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Navigate to the project directory and install the dependencies specified in the `pyproject.toml` file using Poetry:

    ```bash
    cd <project_directory>
    poetry install
    ```

    This command will create a virtual environment (if it doesn't already exist) and install all the dependencies listed in `pyproject.toml` and `poetry.lock`.

4. Poetry automatically manages virtual environments for you. To activate the virtual environment, you can use:

    ```bash
    poetry shell
    ```

    This will activate the environment, and you can start working within it.

5. After installation, the functions can be imported and used in Python scripts or Jupyter notebooks.

Example usage:

    ```python
    from data_transformation_library.transpose import transpose2d
    from data_transformation_library.time_series_windowing import window1d
    from data_transformation_library.cross_correlation import convolution2d
    import numpy as np

    # Example for transpose2d
    matrix = [[1, 2], [3, 4]]
    transposed_matrix = transpose2d(matrix)
    print(transposed_matrix)

    # Example for window1d
    input_array = [1, 2, 3, 4, 5]
    size = 3
    shift = 3
    list_of_lists = window1d(input_array, size, shift)
    print(list_of_lists)

    # Example for convolution2d
    input_matrix = np.array([[1, 2, 3], [4, 5, 6]])
    kernel = np.array([[1, 0], [0, -1]])
    stride = 1
    np_array = convolution2d(input_matrix, kernel, stride)
    print(np_array)
    ```

### Suggestions for Future Improvements

- **Error Handling:** Include robust error handling to manage invalid input types and values. Raise appropriate exceptions for clear feedback.
- **Parameter Validation:** Validate parameters to ensure they meet expected criteria (e.g., positive integers, correct dimensions).
- **Testing:** Add comprehensive test cases to cover typical and edge cases. Ensure that the functions behave correctly across a range of inputs.

**Feel free to fork this repository and make your own modifications!**
