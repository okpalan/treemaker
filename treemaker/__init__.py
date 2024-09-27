from .treemaker import TreeMakerParser,TreeMakerTokenzier


def main():
    parser = argparse.ArgumentParser(description="Create directories and files from a tree structure.")
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
    print(f"Structure created successfully in '{args.output}'.")

if __name__ == "__main__":
    main()
