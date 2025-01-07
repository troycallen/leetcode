class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        return re.findall(p.replace('*', '.*'), s) != []