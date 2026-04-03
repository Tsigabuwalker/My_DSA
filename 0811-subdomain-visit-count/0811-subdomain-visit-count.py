class Solution:
    def subdomainVisits(self, cpdomains):
        counts = {}
        
        for item in cpdomains:
            count_str, domain = item.split()
            count = int(count_str)
            
            parts = domain.split(".")
            
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                
                if subdomain in counts:
                    counts[subdomain] += count
                else:
                    counts[subdomain] = count
        
        result = []
        for domain in counts:
            result.append(str(counts[domain]) + " " + domain)
        
        return result