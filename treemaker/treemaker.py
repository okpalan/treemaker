import os
import re
import argparse

class TreeMakerTokenzier:
    def __init__(self, tree_structure, symbols=None):
        self.tree_structure = tree_structure
        self.symbols = symbols or {
            'directory': '├──',
            'last_directory': '└──',
            'separator': '│',
        }
        self.tokens = []
        
    def tokenize(self):
        lines = self.tree_structure.split('\n')
        for line in lines:
            self.process_line(line)
        return self.tokens
    
    def process_line(self, line):
        indent_level = len(re.match(r'^\s*', line).group()) // 4  # Assuming each indentation is 4 spaces
        cleaned_line = line.strip()
        
        # Check for directory or file based on symbols
        if cleaned_line.startswith(self.symbols['directory']) or cleaned_line.startswith(self.symbols['last_directory']):
            directory_name = cleaned_line.split(maxsplit=1)[1].strip()  # Get the directory name
            self.tokens.append({'type': 'directory', 'name': directory_name, 'indent': indent_level})
        elif '.' in cleaned_line:  # It's a file
            self.tokens.append({'type': 'file', 'name': cleaned_line, 'indent': indent_level})
        else:
            pass

class TreeMakerParser:
    def __init__(self, tokens, base_path="."):
        self.tokens = tokens
        self.base_path = base_path
        self.current_path = base_path
        self.path_stack = []
    
    def parse(self):
        for token in self.tokens:
            try:
                if token['type'] == 'directory':
                    self.handle_directory(token)
                elif token['type'] == 'file':
                    self.handle_file(token)
            except Exception as e:
                print(f"Error: {e}")
    
    def handle_directory(self, token):
        directory_name = token['name'].strip('/')
        
        # Validate directory name
        if not self.is_valid_path(directory_name):
            raise ValueError(f"Invalid directory name: {directory_name}")
        
        # Move up the stack if indent is less (moving to a parent directory)
        while len(self.path_stack) > token['indent']:
            self.path_stack.pop()
        
        self.current_path = os.path.join(self.base_path, *self.path_stack, directory_name)
        
        # Create the directory if it does not exist
        if not os.path.exists(self.current_path):
            os.makedirs(self.current_path)
        else:
            raise FileExistsError(f"Directory already exists: {self.current_path}")
        
        # Add the directory to the path stack for future nesting
        self.path_stack.append(directory_name)
    
    def handle_file(self, token):
        file_name = token['name']
        
        # Validate file name
        if not self.is_valid_path(file_name):
            raise ValueError(f"Invalid file name: {file_name}")
        
        file_path = os.path.join(self.current_path, file_name)
        
        # Create the file if it does not exist
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("")  # Create an empty file
        else:
            raise FileExistsError(f"File already exists: {file_path}")
    
    def is_valid_path(self, name):
        # Check for illegal characters (e.g., on Windows)
        return bool(re.match(r'^[^<>:"/\\|?*]+$', name))


