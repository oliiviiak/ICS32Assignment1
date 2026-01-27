Program Description
This file system inspector and explorer is a Python program that allows
users to navigate directory contents using various command-line
commands. The program supports 4 main commands: L (list directory contents
with options for recursive search, file-only filtering, file name filtering,
and extension filtering), C (creates .dsu files), D (deletes .dsu files),
R (reads .dsu file).such as recursive searching, file-only listing,
filtering by filename, and filtering by file extensions. 
The program handles common errors and runs until the user enters "Q" to quit.

Command Format
[COMMAND] [INPUT] [[-]OPTION] [INPUT]

All Commands
    L - List the contents of the user specified directory.
    Q - Quit the program.
    C - Create a new file in the specified directory.
    D - Delete the file.
    R - Read the contents of a file.

Options of the 'L' command:
    -r Output directory content recursively.
    -f Output only files, excluding directories in the results.
    -s Output only files that match a given file name.
    -e Output only files that match a given file extension.

Options for 'C' command:
    -n allows the user to specify the name of the file.
