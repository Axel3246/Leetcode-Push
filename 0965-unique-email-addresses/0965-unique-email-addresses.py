class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        hmap = {}
        count = 0

        # Iterate through the emails
        for email in emails:
            domain = ''
            idx = 0

            # Let's check what local name we've got (according to the rules with '.' and '@')
            while email[idx] != '+' and email[idx] != '@':
                domain += email[idx]
                idx += 1
                #print(domain)

            # Remove the dots, since they are not important (if there are any), and append the domain searching for '@'s index
            domain = domain.replace('.', '') + email[email.index('@'):]
            #print(f'Replaced Domain {domain}')

            # Add the domain to the hashmap and generate value
            hmap[domain] = hmap.get(domain, 0) + 1

        print(hmap)

        # The unique emails is equal to the hmap lenght
        return len(hmap)

