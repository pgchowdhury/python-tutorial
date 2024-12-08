"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 06-Dec-2024
    Project: Video Downloader with UI
    Library: Tkinter, TTKBootstrap, PYTUBEFIX
"""
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress

### Functions - Do Something ###
def choose_video():
    if ch_string.get() == 'single':
        single_entry['state'] = 'normal'
        multiple_entry['state'] == 'disabled'
    else:
        single_entry['state'] = 'disabled'
        multiple_entry['state'] = 'normal'

def choose_folder():
    filename = filedialog.askdirectory(initialdir="/")
    save_string.set(value=filename)
    button['state'] = 'normal'

def download_video_button():
    urls = []
    resolution = res_string.get()
    save_location = save_string.get()
    single_url = url_string.get()
    if single_url != '':
        urls.append(single_url)
    else:
        multi_url = multiple_entry.get(1.0, 'end').split(',')
        urls = [url.strip() for url in multi_url]
    #print(urls, resolution, save_location)
    download_video(urls, resolution, save_location)
    
def download_video(urls, resolution, save_location):
    try:
        for url in urls:       
            yt = YouTube(url, on_progress_callback = on_progress)
            print(yt.title)
            if resolution == 'low':
                res_streams = yt.streams.get_lowest_resolution()
            else:
                res_streams = yt.streams.get_highest_resolution()
            res_streams.download(output_path=save_location)
            print("The Video Downloaded Succefully !")
    except Exception as e:
        print(e)
        

### Window ###
window = ttk.Window(themename='journal')
window.title('video downloader')
window.minsize(550, 700)

### Variable ###
ch_string = tk.StringVar()
url_string = tk.StringVar()
res_string = tk.StringVar()
save_string = tk.StringVar()

### Widgets ###
# header
header_label = ttk.Label(master=window, text='YouTube Video Downloader', font=('verdana', 30, 'bold'), bootstyle='primary')

# Choose Single Video or Multiple Video
frame1 = ttk.Frame(master=window)
ch_radio_single = ttk.Radiobutton(master=frame1, text='Single Video', bootstyle='success', value='single', 
                                  variable=ch_string, command=choose_video)
ch_radio_bulk = ttk.Radiobutton(master=frame1, text='Multiple Video', bootstyle='success', value='multiple', 
                                variable=ch_string, command=choose_video)

# Enter Single Video URL
single_entry_label = ttk.Label(master=window, text='Enter Video URL')
single_entry = ttk.Entry(master=window, bootstyle='success', textvariable=url_string, width=40, state='disabled')

# Eneter Multiple Video URL
multiple_entry_label = ttk.Label(master=window, text='Enter Multiple Video URLs (Separated by Comma)')
multiple_entry = tk.Text(master=window, width=40, height=15, state='disabled')

# Choose Resolution
frame2 = ttk.Frame(master=window)
high_radio = ttk.Radiobutton(master=frame2, text='High Resolution', bootstyle='success', value='high', 
                                  variable=res_string)
low_radio = ttk.Radiobutton(master=frame2, text='Low Resolution', bootstyle='success', value='low', 
                                variable=res_string)

# Select the Folder
save_label = ttk.Label(master=window, text='Select the Folder to Save the Video')
frame3 = ttk.Frame(master=window)
save_entry = ttk.Entry(master=frame3, bootstyle='success', textvariable=save_string)
save_button = ttk.Button(master=frame3, bootstyle='success-outline', text='Select Folder', command=choose_folder)

# Download Button
button = ttk.Button(master=window, text='Download', bootstyle='success-outline', state='disabled', command=download_video_button)

### Layout ###
header_label.pack(padx=(20, 20), pady=(20, 20))
frame1.pack(pady=(0, 20))
ch_radio_single.pack(side='left', padx=(0, 20))
ch_radio_bulk.pack()
single_entry_label.pack()
single_entry.pack(pady=(0, 20))
multiple_entry_label.pack()
multiple_entry.pack(pady=(0,20))
frame2.pack(pady=(0, 20))
high_radio.pack(side='left', padx=(0, 20))
low_radio.pack()
save_label.pack()
frame3.pack(pady=(0,20))
save_entry.pack(side='left', padx=(0, 20))
save_button.pack()
button.pack(pady=(20,20))


### Run ###
window.mainloop()