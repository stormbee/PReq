# PReq

# Path Requirements

`Path Requirements` is a simple graphical user interface application that allows you to select a directory and automatically generate a `requirements.txt` file. This file will list all the directories present inside the selected folder.

## Features

- **Directory Selection**: Easy-to-use GUI to select your desired directory.
- **Automated File Generation**: Once a directory is chosen, the application will generate a `requirements.txt` file, listing all the subdirectories.
- **File Opening**: Directly open the generated `requirements.txt` with a single click.

## How to use

1. Click on **Open** to select a directory.
2. Click on **Create** to generate the `requirements.txt` file.
3. Click on **Open File** to view the generated file.

## How to compile to a single .exe file

If you wish to compile this script into a standalone `.exe` file, you can use `PyInstaller`. Here's how:

### Pre-requisites:

- Install `PyInstaller`:


### Compilation Steps:

1. Navigate to the directory containing your script.
2. Run the following command:


- `--onefile` creates a single executable.
- `--windowed` ensures no console window appears when the GUI is opened.
- `--icon=/media/r.ico` replaces the default icon of the executable with the one you specify.

3. After compilation, you'll find the `.exe` file inside the `dist` directory.

## Contribution

Feel free to fork this repository and make any changes or improvements you see fit. Pull requests are also welcome!
