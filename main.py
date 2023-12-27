# Import necessary libraries
import PySimpleGUI as sg
from pytube import YouTube
import os
import threading

# Function to download and convert a YouTube video to MP3
def download_and_play(url, destination='.', status_elem=None):
    try:
        # Create a YouTube object using the provided URL
        yt = YouTube(url)
        
        # Update the status element to indicate the download is in progress
        status_elem.update("Download in progress...")

        # Get the stream for the video (only audio) and download it
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=destination)

        # Rename the downloaded file with a .mp3 extension
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # Update the status element to indicate the download is complete
        status_elem.update(yt.title + " has been successfully downloaded.")
    except Exception as e:
        # Handle exceptions and update the status element with an error message
        status_elem.update(f"Error: {str(e)}")

# Function to handle updating the status based on the GUI events
def update_status(window, event, values, status_elem):
    if event == "Start Converting":
        # If the "Start Converting" button is pressed, initiate the download in a separate thread
        status_elem.update("Downloading...")
        download_thread = threading.Thread(target=download_and_play, args=(values['-URL-'], values['-DESTINATION-'], status_elem))
        download_thread.start()

# GUI layout
layout = [
    [sg.Text("Enter the URL of the video you want to download and play:"), sg.Input(key='-URL-')],
    [sg.Text("Select the destination folder:"), sg.FolderBrowse(key='-DESTINATION-', target='-DESTINATION-')],
    [sg.Button("Start Converting")],
    [sg.Text("", size=(40, 2), key='-STATUS-')]
]

# Create the PySimpleGUI window
window = sg.Window("YTMP3", layout)

# Event loop for handling GUI events
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        # Exit the program if the window is closed
        break
    else:
        # Update the status based on the user's actions
        update_status(window, event, values, window['-STATUS-'])

# Close the PySimpleGUI window when the loop exits
window.close()
