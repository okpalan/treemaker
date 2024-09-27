
# TreeMaker

**TreeMaker** is a Python tool that allows you to create a directory structure and files from a specified tree format. The tool parses the input tree structure and generates the corresponding directories and files in the specified output location.

## Features

- Create directories and files based on a tree structure defined in a text file.
- Customizable symbols for tree structure representation.
- Error handling for invalid paths and file creation issues.
- Command-Line Interface (CLI) for easy usage.

## Installation

To use TreeMaker, you can clone the repository and install the required dependencies.

```bash
git clone https://github.com/okpalan/treemaker.git
cd treemaker
pip install -r requirements.txt
```

## Usage

After installing, you can run the TreeMaker tool from the command line with the following command:

```bash
python treemaker.py --input path/to/tree_structure.txt --output path/to/output_directory
```

### Example Tree Structure

Your input file should contain a tree structure formatted like this:

```
├── directory1
│   ├── subdirectory1
│   └── file1.txt
└── directory2
    └── file2.txt
```

### Creating Files with Content

You can also specify content for files in the tree structure by including a colon (`:`) followed by the content, like so:

```
├── directory1
│   ├── subdirectory1
│   └── file1.txt: This is the content of file1.
└── directory2
    └── file2.txt: This is the content of file2.
```

## Error Handling

TreeMaker includes error handling for common issues, such as:
- Invalid paths (e.g., directories with illegal characters)
- File creation failures (e.g., permission issues)
- Duplicate directory and file names

## Contributing

Contributions are welcome! If you have suggestions for improvements or have found bugs, please open an issue or submit a pull request. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

- Thanks to the open-source community for their contributions and support.
