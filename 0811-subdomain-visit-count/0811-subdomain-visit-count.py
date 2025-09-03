class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(int)

        for domain in cpdomains:
            count, domain = domain.split()

            subdomains = domain.split(".")

            for i in range(len(subdomains)):
                subs = ".".join(subdomains[i:])
                #print(subs)
                res[subs] += int(count)
            
        print(res)
        result = []
        for domain,count in res.items():
            result.append(f"{count} {domain}")
        
        return result