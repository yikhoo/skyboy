import tkinter as tk
import requests
import pyperclip

REURL_API_KEY = '4070ff49d794e13219503b663c974755ecd1b436959c04df8a38b58d65165567c4f5d6'

def shorten_url(long_url, utm_source):
    headers = {'reurl-api-key': REURL_API_KEY, 'Content-Type': 'application/json'}
    data = {'url': long_url, 'utm_source': utm_source}
    response = requests.post('https://api.reurl.cc/shorten', headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        if response_json['res'] == 'success':
            return response_json['short_url']
        else:
            print(f"Error: {response_json['msg']}")
    else:
        print(f"Error: Failed to shorten URL (Status code: {response.status_code})")
        return None

def on_submit():
    long_url = url_entry.get()
    short_url = shorten_url(long_url, 'FB_AD')
    if short_url:
        result_label.config(text=short_url)
        copy_button.config(state=tk.NORMAL)
    else:
        result_label.config(text="Error: Failed to shorten URL")
        copy_button.config(state=tk.DISABLED)

def on_copy():
    pyperclip.copy(result_label.cget("text"))

window = tk.Tk()
window.title("URL Shortener")

url_label = tk.Label(text="Enter a URL to shorten:")
url_label.pack()

url_entry = tk.Entry(width=50)
url_entry.pack()

submit_button = tk.Button(text="Shorten", command=on_submit)
submit_button.pack()

result_frame = tk.Frame()
result_frame.pack()

result_label = tk.Label(master=result_frame, text="")
result_label.pack(side=tk.LEFT)

copy_button = tk.Button(master=result_frame, text="Copy", command=on_copy, state=tk.DISABLED)
copy_button.pack(side=tk.LEFT)

window.mainloop()
