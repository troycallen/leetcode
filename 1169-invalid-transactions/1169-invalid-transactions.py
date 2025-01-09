class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []

        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')

            if int(amount) > 1000:
                invalid.append(t)
                continue
            
            for i2, t2 in enumerate(transactions):
                name2, time2, amount2, city2 = t2.split(',')
                if i2 != i:
                    if name == name2 and city != city2 and abs(int(time2) - int(time)) <= 60:
                        invalid.append(t)
                        break
                    
        return invalid

        