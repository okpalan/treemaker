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
        
        if cleaned_line.startswith(self.symbols['directory']) or cleaned_line.startswith(self.symbols['last_directory']):
            directory_name = cleaned_line.split(maxsplit=1)[1].strip()  # Get the directory name
            self.tokens.append({'type': 'directory', 'name': directory_name, 'indent': indent_level})
            print(f"Found directory: {directory_name} at indent level {indent_level}")
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
            except Exception as e:
                print(f"Error: {e}")
    
    def handle_directory(self, token):
        directory_name = token['name'].strip('/')

        # Move up the stack if indent is less (moving to a parent directory)
        while len(self.path_stack) > token['indent']:
            self.path_stack.pop()
        
        self.current_path = os.path.join(self.base_path, *self.path_stack, directory_name)
        
        # Print the path we're about to create
        print(f"Creating directory: {self.current_path}")

        # Create the directory if it does not exist
        if not os.path.exists(self.current_path):
            os.makedirs(self.current_path)
            print(f"Directory created: {self.current_path}")
        else:
            raise FileExistsError(f"Directory already exists: {self.current_path}")
        
        # Add the directory to the path stack for future nesting
        self.path_stack.append(directory_name)

def main():
    parser = argparse.ArgumentParser(description="Create directories from a tree structure.")
    parser.add_argument('--input', type=str, required=True, help="Path to the input tree structure file.")
    parser.add_argument('--output', type=str, default=".", help="Base directory where the structure will be created.")
    args = parser.parse_args()

    # Read the input tree structure from the file
    try:
        with open(args.input, 'r') as f:
            tree_structure = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' does not exist.")
        return
    
    # Tokenize the structure
    tokenizer = TreeMakerTokenzier(tree_structure)
    tokens = tokenizer.tokenize()

    # Parse the tokens and generate the directory structure
    parser = TreeMakerParser(tokens, base_path=args.output)
    parser.parse()
    print(f"Directory structure created successfully in '{args.output}'.")

if __name__ == "__main__":
    main()
