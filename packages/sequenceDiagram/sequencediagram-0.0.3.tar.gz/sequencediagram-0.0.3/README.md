# Sequence Diagram Generator for Python

## Overview

This Python library generates sequence diagrams for your Python code using the Mermaid.js format. It allows you to visualize the interactions between various parts of your code, aiding in better understanding and documentation. 

## Features

- **Mermaid.js Integration**: Utilizes Mermaid.js for generating sequence diagrams.
- **HTML Generation**: Generates an HTML file containing the sequence diagram.
- **Function Decoration**: Decorate functions/methods with `@sequenceDiagram` to include them in the sequence diagram.

## Installation

To install the library, you can use pip:

```bash
pip install sequenceDiagram
```

## Usage

### Importing the Library

```python
from sequenceDiagram import sequenceDiagram, writehtml
```

### Decorating Functions

Use the `@sequenceDiagram` decorator to mark the functions you want to include in the sequence diagram.

```python
@sequenceDiagram
def function_a():
    print("Function A")

@sequenceDiagram
def function_b():
    function_a()
    print("Function B")
```

### Generating the HTML

After decorating the desired functions, use the `writehtml` function to generate the HTML file with the sequence diagram.

```python
html_path = "path/to/sequence_diagram.html"
writehtml(html_path)
```

### Example

Here's a complete example:

```python
from sequenceDiagram import sequenceDiagram, writehtml

@sequenceDiagram
def function_a():
    print("Function A")

@sequenceDiagram
def function_b():
    function_a()
    print("Function B")

@sequenceDiagram
def main():
    function_b()
    print("Main Function")

if __name__ == "__main__":
    main()
    writehtml("sequence_diagram.html")
```

This will generate an HTML file named `sequence_diagram.html` in the specified path, containing the sequence diagram of the interactions between `main`, `function_b`, and `function_a`.


## Contact

For any questions or issues, please open an issue on the GitHub repository or connect with me at brijesh.kulkarni@gmail.com

---