import os

class VoterDatabase:
    def __init__(self, filename: str = "voter_data.txt"):
        """Initialize the database."""
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write("ID,VotedFor\n")

    def has_voted(self, voter_id: str) -> bool:
        """Checks if the voter has already voted before casting a vote and logging it to the system."""
        with open(self.filename, 'r') as file:
            for line in file.readlines()[1:]:
                if line.split(",")[0] == voter_id:
                    return True
        return False

    def record_vote(self, voter_id: str, candidate: str) -> None:
        """Records a vote in the voter data text file if the user has not already voted."""
        with open(self.filename, 'a') as file:
            file.write(f"{voter_id},{candidate}\n")
