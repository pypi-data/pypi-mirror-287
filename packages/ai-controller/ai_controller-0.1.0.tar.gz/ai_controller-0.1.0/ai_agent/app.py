import ast, importlib.util, sys, pathlib, json
from langchain_openai import ChatOpenAI
from settings import OPENAI_API_KEY
from constants import PROMPT_FOR_FINDING_FUNCTION


class FunctionLister(ast.NodeVisitor):

    # Define a visitor class to find function definitions
    def __init__(self):
        self.functions = []
    
    def visit_FunctionDef(self, node):
        docstring = ast.get_docstring(node) or "No description"
        self.functions.append((node.name, docstring))
        self.generic_visit(node)

class Controller:
    """
    This class will take a path of a file where all the functions would be present, 
    """
    def __init__(self, input_text, file_name):
        '''
        Execute the function based on the input text and function descriptions.

        Returns:
            The result of the executed function.

        Raises:
            ValueError: If the function is not callable or not defined in the module.
        '''
        self.input_text = input_text
        self.file_name = file_name

        self.filepath = str(pathlib.Path().resolve())+"/{}".format(file_name)
        self.module = self.import_module_from_file(self.filepath)

        # Parse the file content to create an AST
        with open(self.filepath, 'r') as file:
            file_content = file.read()

        parsed_ast = ast.parse(file_content)

        # Instantiate the visitor and visit the parsed AST
        visitor = FunctionLister()
        visitor.visit(parsed_ast)

        # List of functions in the file
        self.function_name_description_obj = {}
        for name, description in visitor.functions:
            # function_name as key and description as value
            self.function_name_description_obj[name] = description


    def import_module_from_file(self, filepath):
        """
        Import a module from a specified file path.

        Args:
            filepath (str): The path to the file containing the module.

        Returns:
            module: The imported module.
        """
        spec = importlib.util.spec_from_file_location("module.name", filepath)
        module = importlib.util.module_from_spec(spec)

        sys.modules["module.name"] = module
        spec.loader.exec_module(module)
        
        return module
    
    def execute_function(self, module, function_name, *args, **kwargs):
        """
        Execute a function by name from the given module.

        Args:
            module: The module from which the function will be executed.
            function_name (str): The name of the function to be executed.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The result of the executed function.

        Raises:
            ValueError: If the function is not callable or not defined in the module.
        """
        if hasattr(module, function_name):
            func = getattr(module, function_name)
            if callable(func):
                return func(*args, **kwargs)
            else:
                raise ValueError(f"{function_name} is not callable.")
        else:
            raise ValueError(f"{function_name} is not defined in the module.")


    def execute(self):
        '''
        Execute the function based on the input text and function descriptions.

        Returns:
            The result of the executed function.

        Raises:
            ValueError: If the function is not callable or not defined in the module.
        '''
        llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.1,
            max_tokens=None,
            timeout=20,
            max_retries=2,
            api_key=OPENAI_API_KEY
        )
        message = PROMPT_FOR_FINDING_FUNCTION.format(input_txt=self.input_text, obj=self.function_name_description_obj)
        response = llm.invoke(message)

        function_obj = json.loads(response.content)

        try:
            return self.execute_function(self.module, function_obj.get("function_name"), *function_obj.get("arguments"))
        except Exception as e:
            raise e