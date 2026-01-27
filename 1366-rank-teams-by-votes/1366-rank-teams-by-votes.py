class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        # 1. Initialize a dictionary to store vote counts for each team
        # num_teams represents the number of available positions (e.g., 26 max)
        num_teams = len(votes[0])
        
        # rank_counts mapping: { 'A': [pos1_count, pos2_count, ...], ... }
        rank_counts = {team: [0] * num_teams for team in votes[0]}
        
        # 2. Populate the counts from each voter
        for vote in votes:
            for i, team in enumerate(vote):
                rank_counts[team][i] += 1
        
        # 3. Sort the teams
        teams = list(votes[0])
        
        # Key logic:
        # - We want to sort by the counts DESCENDING.
        # - We want to sort by the character ASCENDING as a tie-breaker.
        # Python sorts tuples element-by-element. By negating the counts, 
        # the largest original count becomes the "smallest" negative number, 
        # putting it at the front of the sorted list.
        teams.sort(key=lambda x: ([-count for count in rank_counts[x]], x))
        
        return "".join(teams)