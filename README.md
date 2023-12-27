# PYTMP3  

## A simple python ytmp3 application  

  **Don't use for public song sharing**
  I have created a really simple python youtube to mp3 download, as a fix for all the stupid ytmp3 sites online that are viruses. Its simple to use, fully open-source, and.. well yeah.

  You can use the pre-built exe file, or follow instructions below to build one yourself if you dont trust random exe files (smart btw).

  ##### Check the releases tab for the pre-built pytmp3 exe file  

  # App instructions  
  - Simply open the exe, you can minimize the command prompt window (black window) but **DONT** close it, it will close the app.
  - Input a valid youtube URL and select (using the browse button) the folder to download to. *Default directory is the folder the app is in*
  - Hit the convert button and you are done!
  
  ## App explanation
  - The black window is a command prompt, this is a python interpreter *not everyone has python already installed on their pc*, this simply tells the pc how to run the exe file as python.
   - Each important part of the code will have a comment explaning it

  # Build instructions
  - To build the python file as an exe for yourself, you will have to have python on your pc [Python](python.org).
  - Next go to command prompt and install pyinstaller [Pyinstaller Website](https://pyinstaller.org/en/stable/), using the command `pip install -U pyinstaller`
   - **NOTE use the --onfile arg to install as one exe with python interpreter and dependencies**
  - Open a command prompt/shell window, and navigate to the directory where your .py file is located, then build your app with the following command:
   - `pyinstaller --onefile your_program.py` OR `pyinstaller your_program.py` *If you don't know what you're doing, use the --onefile arg*
  - Your bundled application should now be available in the dist folder, located in the same directory as your python file.
