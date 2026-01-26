
# Olivia Kong
# oykong@uci.edu
# 92692989

from pathlib import Path
import shlex


# helper method for printing paths
def print_values(list_name):
    for item in list_name:
        print(item)


# L command
def list_files(path):
    p = Path(path)
    all_files = []
    all_dirs = []

    for item in p.iterdir():
        if item.is_file():
            all_files.append(item)
        else:
            all_dirs.append(item)

    print_values(all_files)
    print_values(all_dirs)


# L -r command
def list_recursively(path):
    p = Path(path)
    all_files_dirs = []

    for item in p.rglob("*"):
        all_files_dirs.append(item)

    print_values(all_files_dirs)


# L -f command
def list_only_files(path):
    p = Path(path)
    all_files = []

    for item in p.iterdir():
        if item.is_file():
            all_files.append(item)

    print_values(all_files)


# L -r -f command
def list_only_files_recursively(path):
    p = Path(path)
    all_files = []

    for item in p.rglob("*"):
        if item.is_file():
            all_files.append(item)

    print_values(all_files)


# L -s command
def list_exact_filename(path, file_name):
    p = Path(path)
    all_files = []

    for item in p.iterdir():
        if item.is_file() and item.name == file_name:
            all_files.append(item)

    print_values(all_files)


# L -r -s command
def list_exact_filename_recursively(path, file_name):
    p = Path(path)
    all_files = []

    for item in p.rglob("*"):
        if item.is_file() and item.name == file_name:
            all_files.append(item)

    print_values(all_files)


# L -e command
def list_files_extensions(path, extension_name):
    p = Path(path)
    all_files = []

    for item in p.iterdir():
        if item.is_file() and item.suffix[1:] == extension_name:
            all_files.append(item)

    print_values(all_files)


# L -r -e command
def list_files_extensions_recursively(path, extension_name):
    p = Path(path)
    all_files = []

    for item in p.rglob("*"):
        if item.is_file() and item.suffix[1:] == extension_name:
            all_files.append(item)

    print_values(all_files)


# # C -n command
def create_new_file_in_dir(path, file_name):
    p = Path(path)
    
    if not p.exists():
        raise FileNotFoundError(f"Error: the path {path} was not found.")
    if not p.is_dir():
        raise NotADirectoryError(f"Error: the path {path} is not a directory.")
    
    dsu_filename = f"{file_name}.dsu"
    file_path = p / dsu_filename

    file_path.touch()
    print(file_path)


# # D command
def delete_dsu_file(file_path):
    p = Path(file_path)

    if not p.exists():
        raise FileNotFoundError(f"Error: the file {file_path} was not found.")
    if not p.is_file():
        raise ValueError(f"Error: the path {file_path} is not a file.")
    if p.suffix != ".dsu":
        raise ValueError("ERROR")
    
    p.unlink()
    print(f"{file_path} DELETED ")


# # R command
def print_contents_of_dsu_file(file_path):
    p = Path(file_path)

    if not p.exists():
        raise FileNotFoundError(f"Error: the file {file_path} was not found.")
    if not p.is_file():
        raise ValueError(f"Error: the path {file_path} is not a file.")
    if p.suffix != ".dsu":
        raise ValueError("ERROR")
    
    content = p.read_text()

    if not content:
        print("EMPTY")
    else:
        print(content, end='')


def welcome():
    print("Welcome to the File System Inspector!\n")
    print("Here's the format for the user input:")
    print("[COMMAND] [INPUT] [[-]OPTION] [INPUT]\n")
    print("Commands:")
    print("  L - List the contents of the user specified directory.")
    print("  Q - Quit the program.\n")
    print("Options for \"L\":")
    print("-r Output directory content recursively.")
    print("-f Output only files, excluding directories in the results.")
    print("-s Output only files that match a given file name.")
    print("-e Output only files that match a given file extension.")


def main():
    # welcome()

    create_new_file_in_dir("testdir", "hello")
    # delete_dsu_file("testdir/hello.dsu")
    print_contents_of_dsu_file("testdir/hello.dsu")

    # while True:

    #     user_input = input("\nEnter command or type \"Q\" to quit: ").strip()

    #     if not user_input:
    #         continue

    #     full_input = shlex.split(user_input)
    #     command = full_input[0]

    #     if command == "Q":
    #         break

    #     if command == "L":
    #         if len(full_input) < 2:
    #             continue

    #         path = full_input[1]
    #         option = full_input[2:]

    #         try:
    #             # recursive functions
    #             if len(option) == 0:
    #                 list_files(path)
    #             elif option[0] == "-r":
    #                 if len(option) == 1:
    #                     list_recursively(path)
    #                 elif option[1] == "-f":
    #                     list_only_files_recursively(path)
    #                 elif option[1] == "-s" and len(option) > 2:
    #                     list_exact_filename_recursively(path, option[2])
    #                 elif option[1] == "-e" and len(option) > 2:
    #                     list_files_extensions_recursively(path, option[2])

    #             # non-recursive functions
    #             elif option[0] == "-f":
    #                 list_only_files(path)
    #             elif option[0] == "-s" and len(option) > 1:
    #                 list_exact_filename(path, option[1])
    #             elif option[0] == "-e" and len(option) > 1:
    #                 list_files_extensions(path, option[1])

    #         except FileNotFoundError:
    #             print(f"Error: the path '{path}' was not found.")
    #         except NotADirectoryError:
    #             print(f"Error: '{path}' is a valid file path,",
    #                   "but a directory path is required.")
    #         except PermissionError:
    #             print(f"Error: Permission denied for '{path}'")

    #     else:
    #         print("Invalid/Unsupported, try again.")


if __name__ == "__main__":
    main()
