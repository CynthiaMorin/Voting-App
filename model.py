import os #learned how to use the import os feature at: https://www.geeksforgeeks.org/os-module-python-examples/
import csv #generates a csv file for votes
import uuid #for unique identifiers for voters
from datetime import datetime

class VoterDatabase:
    def __init__(self, filename: str = "voter_data.csv"):
        """
        Initializes the voter database. If the specified CSV file doesn't exist, it gets created with the appropriate headers.
        """
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["VoterID", "VotedFor", "Timestamp"])  #sAdd columns for voter ID, vote, and timestamp

    def has_voted(self, voter_id: str) -> bool:
        """
        Check if a given voter ID has already voted, using the unique identifier of the voter.
        Returns True if the voter has already voted, False otherwise.
        """
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  #skips the header row
            for row in reader:
                if row[0] == voter_id:  #Matches voter ID to test for duplicate votes
                    return True
        return False

    def record_vote(self, voter_id: str, candidate: str) -> None:
        """
        Records a vote in the database using the unique identifier of the voter and the name of the candidate the voter is voting for.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #Gets the current time to record in the csv
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, candidate, timestamp])

    def generate_voter_id(self) -> str:
        """
        Generates a unique voter ID that displays at the top of the window and is recorded in the CSV.
        """
        return str(uuid.uuid4())
