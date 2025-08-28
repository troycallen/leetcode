class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(int)
        print(res)

        for domain in cpdomains:
            count, domain = domain.split()
            print(count,domain)
            count = int(count)
            subs = domain.split('.')
            print(subs)
            for i in range(len(subs)):
                res[".".join(subs[i:])] += count
        
        print(res)
        fmat = ["{} {}".format(c, d) for d, c in res.items()]
        return fmat