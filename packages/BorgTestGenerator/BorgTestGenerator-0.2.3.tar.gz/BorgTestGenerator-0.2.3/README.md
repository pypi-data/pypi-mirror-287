# BorgTestGenerator

> OpenAI assistants automations to generate python3 unittest files

BorgTestGenerator is a Python library that generates unit test files from Python scripts using the OpenAI API.

## Installation

### Installation ( with venv )

This section provides instructions for installing the project using a virtual environment (venv).

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/BorgTestGenerator.git
    cd BorgTestGenerator
    ```

2. **Create a virtual environment:**
    ```sh
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Linux or macOS:
        ```sh
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```

4. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```


## Usage if BorgTestGenerator python library

To use the `Assistant` class from the `BorgTestGenerator` module in your code, you need to follow these steps:

1. Import the `Assistant` class from the `BorgTestGenerator` module in your Python file. Make sure the `BorgTestGenerator` module is installed in your Python environment using the `pip install BorgTestGenerator` command.

    ```python
    from BorgTestGenerator import Assistant
    ```

2. Create an instance of the `Assistant` class using the constructor. You can provide additional arguments to the constructor based on your application's needs.

    ```python
    assistant = Assistant()
    ```

3. Use the methods and attributes of the `assistant` instance to interact with the assistant. The `Assistant` class may have methods to perform different tasks, such as generating automated tests, code analysis, etc. Refer to the documentation of the `BorgTestGenerator` module to know the available methods and their specific usages.

    ```python
    assistant.generate_tests()
    ```

This is a basic example of how to use the `Assistant` class from the `BorgTestGenerator` module. Make sure to refer to the module's documentation for more detailed information on features and available options.