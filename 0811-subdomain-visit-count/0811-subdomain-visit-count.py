class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(int)

        for domain in cpdomains:
            count, domain = domain.split()
            subdomains = domain.split(".")
            print(count, subdomains)

            for i in range(len(subdomains)):
                subs = ".".join(subdomains[i:])
                print(subs)
                # have to do add for dupes of int counts like com, etc
                res[subs] += int(count)
            
        print(res)
        res_2 = []
        for domain, count in res.items():
            res_2.append(f"{count} {domain}")
        
        return res_2
                    