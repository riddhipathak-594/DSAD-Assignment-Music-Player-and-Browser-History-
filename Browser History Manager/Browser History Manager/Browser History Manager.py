import tkinter as tk
from tkinter import messagebox

class Page:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class History:
    def __init__(self):
        self.current = None  # Current page pointer
        self.head = None     # First page pointer

    def visit_page(self, url):
        new_page = Page(url)
        if self.current:
            # Remove all forward history when visiting a new page
            self.current.next = None
            new_page.prev = self.current
            self.current.next = new_page
        else:
            self.head = new_page  # Set as the first page if none exist
        self.current = new_page  # Set the new page as the current page

    def go_back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.url
        return None

    def go_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.url
        return None

    def get_history(self):
        history = []
        node = self.head
        while node:
            if node == self.current:
                history.append(f"> {node.url} (Current)")
            else:
                history.append(node.url)
            node = node.next
        return history

    def clear_history(self):
        self.head = None
        self.current = None

class BrowserApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Riddhi Browser History Manager")
        self.root.configure(bg="#1c1c1c")  # Dark background

        self.history = History()

        # URL Entry
        self.url_entry = tk.Entry(root, width=50, bg="#333", fg="green", insertbackground="white")
        self.url_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Visit Page Button
        self.visit_button = tk.Button(root, text="Visit", command=self.visit_page, bg="#444", fg="green")
        self.visit_button.grid(row=0, column=2, padx=5)

        # Navigation Buttons
        self.back_button = tk.Button(root, text="Back", command=self.go_back, bg="#444", fg="green")
        self.back_button.grid(row=1, column=0, padx=5, pady=5)

        self.forward_button = tk.Button(root, text="Forward", command=self.go_forward, bg="#444", fg="green")
        self.forward_button.grid(row=1, column=1, padx=5, pady=5)

        self.clear_button = tk.Button(root, text="Clear History", command=self.clear_history, bg="#444", fg="green")
        self.clear_button.grid(row=1, column=2, padx=5, pady=5)

        # Label for History Display
        self.history_label = tk.Label(root, text="Browser History", bg="#1c1c1c", fg="green", font=("Arial", 12, "bold"))
        self.history_label.grid(row=2, column=0, columnspan=3, pady=(10, 0))

        # History Display
        self.history_listbox = tk.Listbox(root, width=60, height=15, bg="#333", fg="green", selectbackground="#444", selectforeground="white")
        self.history_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.update_history_display()

    def visit_page(self):
        url = self.url_entry.get().strip()
        if url:
            self.history.visit_page(url)
            self.update_history_display()
            self.url_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a URL.")

    def go_back(self):
        url = self.history.go_back()
        if url:
            self.update_history_display()
        else:
            messagebox.showinfo("Navigation", "No more history to go back to.")

    def go_forward(self):
        url = self.history.go_forward()
        if url:
            self.update_history_display()
        else:
            messagebox.showinfo("Navigation", "No more history to go forward to.")

    def clear_history(self):
        self.history.clear_history()
        self.update_history_display()
        messagebox.showinfo("Clear History", "Browsing history cleared.")

    def update_history_display(self):
        # Clear the Listbox
        self.history_listbox.delete(0, tk.END)

        # Populate Listbox with history
        for entry in self.history.get_history():
            self.history_listbox.insert(tk.END, entry)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserApp(root)
    root.mainloop()
