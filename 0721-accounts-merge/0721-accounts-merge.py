class Solution:
    def accountsMerge(self, accounts):
        parent = {}  # email -> parent email
        email_to_name = {}  # email -> name

        # Step 1: Initialize parent map
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 2: Union emails in the same account
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        # Step 3: Group emails by root parent
        groups = {}
        for email in parent:
            root = find(email)
            if root not in groups:
                groups[root] = []
            groups[root].append(email)

        # Step 4: Build result
        result = []
        for emails in groups.values():
            result.append([email_to_name[emails[0]]] + sorted(emails))

        return result
