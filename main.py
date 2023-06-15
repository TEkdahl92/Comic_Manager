import tkinter as tk
from tkinter import messagebox

class ComicManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Comic Manager")
        self.master.geometry("400x400")
        self.master.config(bg='#708090')

        self.comics = []
        self.lend_list = []

        # Labels
        self.login_label = tk.Label(self.master, text="Comic Manager", font=("Helvetica", 16), bg='#708090', fg='white')
        self.login_label.pack()
        self.username_label = tk.Label(self.master, text="Username", font=("Helvetica", 12), bg='#708090', fg='white')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.username_entry.pack()
        self.password_label = tk.Label(self.master, text="Password", font=("Helvetica", 12), bg='#708090', fg='white')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, font=("Helvetica", 12), show="*")
        self.password_entry.pack()

        # Login
        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Helvetica", 12))
        self.login_button.pack()

        # Register
        self.register_button = tk.Button(self.master, text="Register", command=self.register, font=("Helvetica", 12))
        self.register_button.pack()

        self.username = ""
        self.password = ""
        self.managers = []

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        for manager in self.managers:
            if self.username == manager[0] and self.password == manager[1]:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.login_label.destroy()
                self.username_label.destroy()
                self.username_entry.destroy()
                self.password_label.destroy()
                self.password_entry.destroy()
                self.login_button.destroy()
                self.register_button.destroy()
                self.comic_management_screen()
                return
        messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.managers.append([self.username, self.password])
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
    def comic_management_screen(self):
        self.add_comic_label = tk.Label(self.master, text="Add Comic", font=("Helvetica", 16), bg='#708090', fg='white')
        self.add_comic_label.pack()
        self.add_comic_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.add_comic_entry.pack()
        self.add_comic_button = tk.Button(self.master, text="Add Comic", command=self.add_comic, font=("Helvetica", 12))
        self.add_comic_button.pack()
        self.remove_comic_label = tk.Label(self.master, text="Remove Comic", font=("Helvetica", 16), bg='#708090', fg='white')
        self.remove_comic_label.pack()
        self.remove_comic_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.remove_comic_entry.pack()
        self.remove_comic_button = tk.Button(self.master, text="Remove Comic", command=self.remove_comic, font=("Helvetica", 12))
        self.remove_comic_button.pack()
        self.lend_comic_label = tk.Label(self.master, text="Lend comic", font=("Helvetica", 16), bg='#708090', fg='white')
        self.lend_comic_label.pack()
        self.lend_comic_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.lend_comic_entry.pack()
        self.lend_comic_button = tk.Button(self.master, text="Lend Comic", command=self.lend_comic, font=("Helvetica", 12))
        self.lend_comic_button.pack()
        self.view_comics_button = tk.Button(self.master, text="View Comics", command=self.view_comics, font=("Helvetica", 12))
        self.view_comics_button.pack()

    def add_comic(self):
        comic = self.add_comic_entry.get()
        self.comics.append(comic)
        messagebox.showinfo("Success", "comic added successfully")
        self.add_comic_entry.delete(0, tk.END)

    def remove_comic(self):
        comic = self.remove_comic_entry.get()
        if comic in self.comics:
            self.comics.remove(comic)
            messagebox.showinfo("Success", "Comic removed successfully")
        else:
            messagebox.showerror("Error", "Comic not found")
        self.remove_comic_entry.delete(0, tk.END)

    def lend_comic(self):
        comic = self.lend_comic_entry.get()
        if comic in self.comics:
            self.lend_list.append(comic)
            self.comics.remove(comic)
            messagebox.showinfo("Success", "Comic lent successfully")
        else:
            messagebox.showerror("Error", "Comic not found")
        self.lend_comic_entry.delete(0, tk.END)

    def view_comics(self):
        message = "\n".join(self.comics)
        messagebox.showinfo("Comics", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ComicManagement(root)
    root.mainloop()