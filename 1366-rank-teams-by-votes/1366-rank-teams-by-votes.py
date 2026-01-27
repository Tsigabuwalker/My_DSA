class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        # 1. Initialize a dictionary to store vote counts for each team
        # Each team has a list of counts, one for each possible rank position
        num_teams = len(votes[0])
        # We use a dict of lists: { 'A': [0, 0, 0], 'B': [0, 0, 0] ... }
        rank_counts = {team: [0] * num_teams for team in votes[0]}
        
        # 2. Fill the vote counts
        for vote in votes:
            for i, team in enumerate(vote):
                rank_counts[team][i] += 1
        
        # 3. Sort the teams
        # Key explanation: 
        # - We want to sort by the counts descending, so we use '-' on counts
        #   or just rely on the fact that we compare the lists. 
        # - Because we want DESCENDING for votes but ASCENDING for the team letter,
        #    we can use a custom key.
        
        teams = list(votes[0])
        
        # We sort based on:
        # 1st: The rank_counts list (negated for descending order)
        # 2nd: The team name itself (for alphabetical tie-breaking)
        teams.sort(key=lambda x: ([-count for count in rank_counts[x]], x))
        
        return "".join(teams)