import tkinter as tk
from tkinter import messagebox
from model import VoterDatabase
from controller import VoteManager

class VotingApp:
    def __init__(self, root: tk.Tk):
        """
        Initialize the voting application GUI.
        root is the main Tkinter window.
        """
        self.root = root
        self.root.title("Voting App") #window title for GUI
        
        #Sets a fixed window size
        self.root.geometry("300x100")
        
        #Makes the GUI non resizable
        self.root.resizable(False, False)

        #Sets up the database and voting manager
        self.database = VoterDatabase()
        self.manager = VoteManager(self.database)

        #Generates a unique voter ID for this session so that duplicate votes cannot be cast
        self.voter_id = self.database.generate_voter_id()

        #Creates and arranges the text and buttons on the GUI window 
        self.message_label = tk.Label(root, text=f"Your Voter ID is: {self.voter_id}", font=("Arial", 10))
        self.message_label.pack()

        self.vote_label = tk.Label(root, text="Choose a candidate:", font=("Arial", 12))
        self.vote_label.pack()

        self.john_button = tk.Button(root, text="John", command=lambda: self.cast_vote("1"))
        self.john_button.pack()

        self.jane_button = tk.Button(root, text="Jane", command=lambda: self.cast_vote("2"))
        self.jane_button.pack()

    def cast_vote(self, candidate_key: str) -> None:
        """
        Handle vote casting for a selected candidate, where candidate_key is the key representing the selected candidate.
        """
        message = self.manager.process_vote(self.voter_id, candidate_key)
        if "already" in message: #error handler for duplicate votes
            self.message_label.config(text=message, fg="red")
        else:
            self.message_label.config(text=message, fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
