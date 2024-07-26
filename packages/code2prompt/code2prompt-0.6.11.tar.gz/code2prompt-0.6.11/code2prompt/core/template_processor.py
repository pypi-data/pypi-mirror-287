from typing import OrderedDict
import os 
from jinja2 import Environment, FileSystemLoader
from code2prompt.utils.include_loader import CircularIncludeError, IncludeLoader
from prompt_toolkit import prompt
import re

def load_template(template_path):
    """ Load a Jinja2 template from a file. """
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError as e:
        raise IOError(f"Error loading template file: {e}") from e

def get_user_inputs(template_content):
    """ Extract user-defined variables from the template and prompt for input. """
    # Use a regex pattern that excludes Jinja execute blocks and matches the new input syntax
    pattern = r'{{\s*input:([^{}]+?)\s*}}'
    user_vars = re.findall(pattern, template_content)
    user_inputs = {}
    
    for var in user_vars:
        # Strip whitespace from the variable name
        clean_var = var.strip()
        # Only prompt for non-empty variable names that haven't been prompted before
        if clean_var and clean_var not in user_inputs:
            user_inputs[clean_var] = prompt(f"Enter value for {clean_var}: ")
    
    return user_inputs


def process_template(template_content, files_data, user_inputs, template_path):
    try:
        template_dir = os.path.dirname(template_path)
        env = Environment(
            loader=IncludeLoader(template_dir),
            autoescape=True,
            keep_trailing_newline=True
        )
        template = env.from_string(template_content)
        return template.render(files=files_data, **user_inputs)
    except CircularIncludeError as e:
        raise ValueError(f"Circular include detected: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error processing template: {e}")