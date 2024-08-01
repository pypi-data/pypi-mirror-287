# AI-Agent (Auto-Code Executor)

AI-Agent (Auto-Code Executor) is a Python module that dynamically executes Python functions based on textual input. It leverages a language model (LLM) to match the input text with function descriptions and then executes the corresponding function from a specified file.

## Features

- **Dynamic Function Execution**: Executes Python functions based on descriptive input text.
- **AST Parsing**: Uses Abstract Syntax Tree (AST) to extract function names and descriptions.
- **LLM Integration**: Utilizes a language model to find and execute the appropriate function.
- **Flexible Module Loading**: Imports functions from any Python file at runtime.

## Installation

Install the module using pip:


## Usage Example

from ai_agent import Controller

input_text = "what is 10+90?"
controller = Controller(input_text, 'sample.py')

result = controller.execute()
print(result) 


```bash
pip install ai-controller


