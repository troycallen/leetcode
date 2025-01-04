class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)

        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x : (x[1])):
            users[user].append(site)

        patterns = Counter()

        for user, sites in users.items():
            patterns.update(set(combinations(sites,3)))

        return max(sorted(patterns), key = patterns.get)