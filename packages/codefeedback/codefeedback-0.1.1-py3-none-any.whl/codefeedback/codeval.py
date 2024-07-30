# my_extension.py
import random
from .general_check import check, check_syntax

from IPython.core.magic import Magics, magics_class, line_magic


@magics_class
class MyMagics(Magics):
    def __init__(self, shell):
        super().__init__(shell)
        self.solutions = {}

    @line_magic
    def load(self, line):
        """Load a Python script and extract variables."""
        script_name = line.strip()
        if not script_name:
            print("Please provide a script name.")
            return

        solutions = get_variables_from_pyscript(script_name)
        if not solutions:
            print(f"Could not load any variables from {script_name}.")
        else:
            try:
                self.solutions = solutions['solution']
            except KeyError:
                print("The variable 'solution' is not defined")
                return
            finally:
                print(f"Successfully loaded solutions from: {script_name}")

    @line_magic
    def check(self, line):
        task_name, *code_lines = line.split('\n', 1)
        response = '\n'.join(code_lines)
        check_list, answer = self.solutions[task_name]
        evaluation_function(response, answer, check_list)


def load_ipython_extension(ipython):
    ipython.register_magics(MyMagics)


def get_variables_from_pyscript(file_path):
    # Read the PyScript file
    with open(file_path, 'r') as file:
        script_content = file.read()

    # Create a dictionary to hold the global variables
    global_vars = {}

    # Execute the script content in the global context
    exec(script_content, globals(), global_vars)

    # Return the global variables found in the script
    return global_vars


def evaluation_function(response, answer, check_list: list):
    correct_feedback = random.choice(["Good Job!", "Well Done!", "Awesome"])
    general_feedback = check(response)
    print(general_feedback)
