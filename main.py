import PySimpleGUI as sg
from pytube import YouTube
import os
import threading

def download_and_play(url, destination='.', status_elem=None):
    try:
        yt = YouTube(url)
        status_elem.update("Download in progress...")

        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        status_elem.update(yt.title + " has been successfully downloaded.")
    except Exception as e:
        status_elem.update(f"Error: {str(e)}")

def update_status(window, event, values, status_elem):
    if event == "Start Converting":
        status_elem.update("Downloading...")
        download_thread = threading.Thread(target=download_and_play, args=(values['-URL-'], values['-DESTINATION-'], status_elem))
        download_thread.start()

layout = [
    [sg.Text("Enter the URL of the video you want to download and play:"), sg.Input(key='-URL-')],
    [sg.Text("Select the destination folder:"), sg.FolderBrowse(key='-DESTINATION-', target='-DESTINATION-')],
    [sg.Button("Start Converting")],
    [sg.Text("", size=(40, 2), key='-STATUS-')]
]

window = sg.Window("YTMP3", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    else:
        update_status(window, event, values, window['-STATUS-'])

window.close()
