# PYTMP3

## A Simple Python YTMP3 Application

**Caution: Do not use for public song sharing.**

I have created a straightforward Python YouTube to MP3 downloader as a solution for the numerous suspicious YTMP3 sites online that may contain viruses. It's simple to use, fully open-source, and, well, yeah.

You can use the pre-built executable file, or follow the instructions below to build one yourself if you don't trust random executable files (smart move, by the way).

##### Check the Releases tab for the pre-built PYTMP3 executable file.

# App Instructions  
  ###Note: it might take a second the first time, it's installing its dependencies
- Simply open the executable. You can minimize the command prompt window (black window), but **DON'T** close it; it will close the app.
- Input a valid YouTube URL and select (using the browse button) the folder to download to. *The default directory is the folder the app is in.*
- Hit the convert button, and you are done!

## App Explanation

- The black window is a command prompt; this is a Python interpreter (*not everyone has Python already installed on their PC*). It simply tells the PC how to run the executable file as Python.
  - Each important part of the code will have a comment explaining it.

# Build Instructions

- To build the Python file as an executable for yourself, you will need to have Python on your PC [Python](https://python.org).
- Next, go to the command prompt and install PyInstaller [PyInstaller Website](https://pyinstaller.org/en/stable/) using the command `pip install -U pyinstaller`.
  - **NOTE: Use the `--onefile` argument to install as one executable with Python interpreter and dependencies.**
- Open a command prompt/shell window, navigate to the directory where your `.py` file is located, and build your app with the following command:
  - `pyinstaller --onefile your_program.py` OR `pyinstaller your_program.py` (*If you don't know what you're doing, use the `--onefile` argument.*)
- Your bundled application should now be available in the `dist` folder, located in the same directory as your Python file.
