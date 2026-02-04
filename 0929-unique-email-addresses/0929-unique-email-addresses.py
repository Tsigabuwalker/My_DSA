class Solution:
    def numUniqueEmails(self, emails):
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            # Ignore everything after '+' in local name
            if '+' in local:
                local = local[:local.index('+')]
            # Remove all '.' from local name
            local = local.replace('.', '')
            # Reconstruct the normalized email
            normalized = local + '@' + domain
            unique_emails.add(normalized)
        
        return len(unique_emails)
