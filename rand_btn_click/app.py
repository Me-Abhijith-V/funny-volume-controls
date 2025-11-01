import random
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import tkinter as tk

def set_random_volume():
    # Get the default audio device
    devices = AudioUtilities.GetAllDevices()
    speakers = AudioUtilities.GetSpeakers()
    interface = speakers.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get volume range (usually -65.25 to 0.0)
    vol_range = volume.GetVolumeRange()
    min_vol, max_vol = vol_range[0], vol_range[1]

    # Random volume between min and max
    rand_vol = random.uniform(min_vol, max_vol)
    volume.SetMasterVolumeLevel(rand_vol, None)

    # Calculate percentage
    current_vol = int((rand_vol - min_vol) / (max_vol - min_vol) * 100)
    label.config(text=f"Volume set to: {current_vol}%")

# GUI setup
root = tk.Tk()
root.title("🎵 Funny Volume Control 🎵")
root.geometry("400x250")
root.config(bg="#222")

label = tk.Label(root, text="Click the button to randomize volume!", fg="white", bg="#222", font=("Segoe UI", 12))
label.pack(pady=30)

btn = tk.Button(root, text="🔀 Random Volume", font=("Segoe UI", 14, "bold"),
                bg="#4CAF50", fg="white", padx=20, pady=10, command=set_random_volume)
btn.pack(pady=20)

root.mainloop()
