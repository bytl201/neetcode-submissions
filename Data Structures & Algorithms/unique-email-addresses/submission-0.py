class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for addy in emails:
            splitted = addy.split("@")

            local_name = splitted[0]
            domain_name = splitted[1]

            if "+" in local_name:
                i = local_name.find("+")
                local_name = local_name[:i]

            if '.' in local_name:
                i = local_name.find(".")

                while i != -1:
                    print(local_name)
                    local_name = local_name[:i] + local_name[i+1:]
                    i = local_name.find(".")


            res.add(local_name+domain_name)

        return len(res)