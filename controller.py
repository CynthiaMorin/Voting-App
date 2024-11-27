class VoteManager:
    #Initialize the voting class
    def __init__(self, database):
        self.database = database
        self.candidates = {"1": "John", "2": "Jane"} #Use keys to represent candidates, for use in the process_vote method
    
    def validate_voter_id(self, voter_id: str) -> bool: #Use the true/false method to determine voter ID validity
        """Ensures the voter ID is all letters."""
        return voter_id.isalpha()

    def process_vote(self, voter_id: str, candidate_key: str) -> str:
        """If voter ID is not all letters or has already voted, an error is returned."""
        if not self.validate_voter_id(voter_id):
            return "Invalid voter ID. Must contain only letters."
        if self.database.has_voted(voter_id):
            return "You have already voted!"
        self.database.record_vote(voter_id, self.candidates[candidate_key])
        return f"Vote recorded for {self.candidates[candidate_key]}."
