class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(int)

        for domain in cpdomains:
            count, domain = domain.split()
            #print(count, domain)
            subdomains = domain.split('.')
            #print(subdomains)
            
            for i in range(len(subdomains)):
                #print(subdomains[i:])
                subs = '.'.join(subdomains[i:])
                #print(subs)
                res[subs] += int(count)
            
        print(res)
        result = []
        for key, val in res.items():
            print(key,val)
            result.append(f"{val} {key}")
        
        return result
        
        