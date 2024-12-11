from model import VoterDatabase  #sImports the VoterDatabase class from the model module

class VoteManager:
    def __init__(self, database: VoterDatabase):
        """
        Initialize the vote manager; this will be the database object for managing voter data.
        """
        self.database = database
        self.candidates = {"1": "John", "2": "Jane"}  #Mapping keys to the two candidate names

    def process_vote(self, voter_id: str, candidate_key: str) -> str:
        """
        Process a vote, using the voter_id (the unique identifier of the voter), to make sure the voter has not yet voted.
        candidate_key assigns the key representing the selected candidate.
        Returns a message indicating outcome of the vote (already voted or successfully voted)
        """
        if self.database.has_voted(voter_id): #error handling
            return f"You have already voted!" 
        candidate_name = self.candidates.get(candidate_key, "Unknown")
        self.database.record_vote(voter_id, candidate_name)
        return f"Vote recorded for {candidate_name}."
