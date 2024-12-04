import requests
import json
import tkinter as tk
from tkinter import Entry, Button, scrolledtext, messagebox
from tkinter import filedialog

def get_user_info():
    username = us_entry.get()
    repo_name = repo_entry.get()

    if username == 'MarlinFirmware' and repo_name=='Marlin':
        u = 'MarlinFirmware'
        r = 'Marlin'
        url = f"https://api.github.com/repos/{u}/{r}"
        response = requests.get(url)
        response.raise_for_status()
        user_data = response.json()

        info = {
            "company": user_data.get("company"),
            "created_at": user_data.get("created_at"),
            "email": user_data.get("email"),
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "url": user_data.get("html_url"),
        }

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "w") as f:
                json.dump(info, f, indent=4)
            messagebox.showinfo("Success", f"Data saved to {file_path}")

root = tk.Tk()
root.title('Kushlakova')
root.geometry('600x400')

username_label = tk.Label(root, text="GitHub Username:")
username_label.grid(row=1, column=1)
us_entry = Entry(root,width=30)
us_entry.grid(row=1,column=2)


repo_label = tk.Label(root, text="GitHub Repositories:")
repo_label.grid(row=2, column=1)
repo_entry = Entry(root,width=30)
repo_entry.grid(row=2,column=2)

get_button = tk.Button(root, text="Get Info", command=get_user_info)
get_button.grid(row=4, column=2)

root.mainloop()