class Solution:
    def reformatDate(self, date: str) -> str:
        # Your logic goes here
        parts = date.split()
        
        # 1. Handle Day (Remove "st", "nd", "rd", "th")
        day = parts[0][:-2]
        if len(day) == 1:
            day = "0" + day
            
        # 2. Handle Month
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        month = months[parts[1]]
        
        # 3. Handle Year
        year = parts[2]
        
        return f"{year}-{month}-{day}"