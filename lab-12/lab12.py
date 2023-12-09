

import tkinter as tk
import firebase_admin
from firebase_admin import db


cred = firebase_admin.credentials.Certificate('lab12.json')
firebase_admin.initialize_app(
    cred, {'databaseURL': 'https://lab-12-a3127-default-rtdb.firebaseio.com/'})
ref = firebase_admin.db.reference('/')


class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat App")

        self.message_listbox = tk.Listbox(master, height=15, width=50)
        self.message_listbox.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(master, width=40)
        self.message_entry.pack(padx=10, pady=5)

        self.name_entry = tk.Entry(master, width=40)
        self.name_entry.pack(padx=10, pady=5)

        self.send_button = tk.Button(
            master, text="Send", command=self.send)
        self.send_button.pack(pady=5)

        self.messages_stream = ref.child(
            'messages').listen(self.theStream)

    def send(self):
        textOfMassege = self.message_entry.get()
        name_text = self.name_entry.get()
        if textOfMassege:
            newOne = {'name': name_text, 'text': textOfMassege}
            ref.child('messages').push(newOne)
            self.message_entry.delete(0, 'end')

    def theStream(self, event):
        if event.event_type == 'put':
            if event.path == '/':

                if event.data is not None:
                    for key in event.data:
                        message = event.data[key]
                        self.theMessage(message)
            else:

                message = event.data
                self.theMessage(message)

    def theMessage(self, message):
        name = message.get('name', 'Unknown')
        text = message.get('text', '')
        display_message = f'{name}: {text}'
        self.message_listbox.insert('end', display_message)
        self.message_listbox.yview(tk.END)

    def close(self):

        self.messages_stream = None
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    chat_app = ChatApp(root)
    root.protocol("WM_DELETE_WINDOW", chat_app.close)
    root.mainloop()
