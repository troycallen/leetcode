class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []

        for i, t1 in enumerate(transactions):
            name, time, amount, city = t1.split(',')

            if int(amount) > 1000:
                invalid.append(t1)
                continue
            
            for j, t2 in enumerate(transactions):
                if i != j:
                    name2, time2, amount2, city2 = t2.split(',')

                    if name == name2 and city != city2 and abs(int(time) - int(time2)) <= 60:
                        invalid.append(t1)
                        break

        return invalid