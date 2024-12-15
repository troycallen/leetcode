class Solution:
  def equalFrequency(self, word: str) -> bool:
    counts = Counter(Counter(word).values())

    if len(counts) == 1:
      return 1 in counts or 1 in counts.values()
      
    if len(counts) == 2:
      return counts[1] == 1 or counts[min(counts) + 1] == 1

    return False