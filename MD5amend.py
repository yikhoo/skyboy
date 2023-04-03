import hashlib
import tkinter as tk
from tkinter import filedialog


# Define a function to calculate the MD5 hash of the selected video file and update the GUI
def calculate_md5_hash():
    # Get the path to the selected video file
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

    # Read the contents of the video file in binary mode
    with open(video_path, "rb") as f:
        video_data = f.read()

    # Calculate the MD5 hash of the video data
    md5_hash = hashlib.md5(video_data).hexdigest()

    # Update the MD5 hash label in the GUI with the calculated value
    md5_hash_label.config(text="MD5 hash: " + md5_hash)


# Define a function to modify the selected video file and update the GUI
def modify_video_file():
    # Get the path to the selected video file
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

    # Read the contents of the video file in binary mode
    with open(video_path, "rb") as f:
        video_data = f.read()

    # Modify the video data (for example, by appending some bytes)
    modified_video_data = video_data + b"some additional bytes"

    # Calculate the new MD5 hash of the modified video data
    modified_md5_hash = hashlib.md5(modified_video_data).hexdigest()

    # Overwrite the original video file with the modified data
    with open(video_path, "wb") as f:
        f.write(modified_video_data)

    # Update the MD5 hash label in the GUI with the new value
    md5_hash_label.config(text="MD5 hash: " + modified_md5_hash)


# Create the GUI window
root = tk.Tk()
root.title("视频MD5修改器")

# Create a button to select the video file and calculate its MD5 hash
calculate_md5_hash_button = tk.Button(root, text="查看视频MD5", command=calculate_md5_hash)
calculate_md5_hash_button.pack(padx=10, pady=10)

# Create a label to display the MD5 hash value
md5_hash_label = tk.Label(root, text="MD5 hash: ")
md5_hash_label.pack(padx=10, pady=10)

# Create a button to select the video file and modify its MD5 hash
modify_video_file_button = tk.Button(root, text="修改视频MD5", command=modify_video_file)
modify_video_file_button.pack(padx=10, pady=10)

# Run the GUI main loop
root.mainloop()
