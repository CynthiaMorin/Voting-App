import tkinter as tk
from tkinter import messagebox
from model import VoterDatabase
from controller import VoteManager

class VotingApp:
    def __init__(self, root): #Initialize all the different variables, messages, labels, and files that will be run at once
        self.root = root
        self.root.title("Voting App")
        self.database = VoterDatabase()
        self.manager = VoteManager(self.database)

        self.message_label = tk.Label(root, text="", font=("Arial", 10))
        self.message_label.pack()

        self.id_label = tk.Label(root, text="Enter your Voter ID:", font=("Arial", 12))
        self.id_label.pack()

        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        self.vote_label = tk.Label(root, text="Choose a candidate:", font=("Arial", 12))
        self.vote_label.pack()

        self.john_button = tk.Button(root, text="John", command=lambda: self.cast_vote("1"))
        self.john_button.pack()

        self.jane_button = tk.Button(root, text="Jane", command=lambda: self.cast_vote("2"))
        self.jane_button.pack()

    def cast_vote(self, candidate_key: str): 
        voter_id = self.id_entry.get().strip()
        message = self.manager.process_vote(voter_id, candidate_key)

        """Changes the message color to the voter based on whether or not they have voted. If an error is present, red is the color."""
        if "Invalid" in message or "already" in message:
            self.message_label.config(text=message, fg="red")
        else:
            self.message_label.config(text=message, fg="green")

        self.id_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
