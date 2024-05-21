
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class LoginApp:
    def __init__(self) -> None:
        self.login_window = tk.Tk()
        self.login_window.title('Login Application')
        self.login_window.geometry('400x300')
        self.login_window.configure(bg='#f0f0f0')

        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 12))
        style.configure('TEntry', font=('Helvetica', 12))
        style.configure('TButton', font=('Helvetica', 12), padding=6)

        ttk.Label(self.login_window, text='Username').pack(pady=10)
        self.username_entry = ttk.Entry(self.login_window)
        self.username_entry.pack(pady=5, padx=10)

        ttk.Label(self.login_window, text='Password').pack(pady=10)
        self.password_entry = ttk.Entry(self.login_window, show='*')
        self.password_entry.pack(pady=5, padx=10)

        self.login_button = ttk.Button(
            self.login_window,
            text='Login',
            command=self.login
        )
        self.login_button.pack(pady=20)
        
        self.login_window.mainloop()
        
    def login(self):
        conn = sqlite3.connect('user_db.db')
        cursor = conn.cursor()

        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?;', (username, password))
        user = cursor.fetchone()
 
        if user:
            self.show_profile(user)
        else:
            messagebox.showerror(title='Login Failed', message='Invalid username or password')

        conn.close()

    def show_profile(self, user):
        self.login_window.destroy()
        self.profile_window = tk.Tk()
        self.profile_window.title(f'Profile of {user[0]}')
        self.profile_window.geometry('300x200')
        self.profile_window.configure(bg='#f0f0f0')

        style = ttk.Style()
        style.configure('Profile.TLabel', font=('Helvetica', 12))

        ttk.Label(self.profile_window, text=f'Name: {user[2]}', style='Profile.TLabel').pack(pady=10)
        ttk.Label(self.profile_window, text=f'Age: {user[3]}', style='Profile.TLabel').pack(pady=10)
        ttk.Label(self.profile_window, text=f'E-Mail: {user[4]}', style='Profile.TLabel').pack(pady=10)

        self.profile_window.mainloop()

if __name__ == '__main__':
    LoginApp()

