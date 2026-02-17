class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        
        # hour first digit
        if time[0] == '?':
            if time[1] != '?' and int(time[1]) > 3:
                time[0] = '1'
            else:
                time[0] = '2'
        
        # hour second digit
        if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'
        
        # minute first digit
        if time[3] == '?':
            time[3] = '5'
        
        # minute second digit
        if time[4] == '?':
            time[4] = '9'
        
        return "".join(time)
