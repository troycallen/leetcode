class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        d = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
            30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
            70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred"
        }

        def get_string(n):
            res = []

            # handlded hundreds (523 - five hundred)
            hundreds = n // 100
            if hundreds:
                res.append(d[hundreds] + " Hundred")

            # hanbdle the remaining 2 in the hundreds (tens and ones)

            # get last 2 (523 - 23)
            last_2 = n % 100

            # if last 2 are greater than 20 we know we dont have weird edge cases
            if last_2 >= 20:
                # can split them into tens and ones
                tens = last_2 // 10
                ones = last_2 % 10
                
                #have to multiply the tens value by 10 since its just 2,3,4, etc.
                res.append(d[tens*10])

                # if we have a ones val we can just append it after in 3rd slot
                if ones:
                    res.append(d[ones])

            # for 1-19 we can just lookup from the map
            elif last_2:
                res.append(d[last_2])

            print(res)
            # we join to get the string from each separate array entry
            return " ".join(res)
        
        # suffixes for groups of 3 digits
        postfix = ["", " Thousand", " Million", " Billion"]
        i = 0

        # build right to left in grps of 3 digits
        res = []
        while num:
            #print(1234567 % 1000)

            # get the last 3 -> 1234567 = 567
            digits = num % 1000

            # convert 3 digits to words
            s = get_string(digits)

            # only add if its not a zero (so we dont get Zero Thousand, Zero Million, etc)
            if s:
                
                res.append(s + postfix[i])  
            
            # remove the rightmost 3 digits and go to next group
            num = num // 1000

            #increment to our next suffix
            i += 1
        # reverse since we bult in reverse order
        res.reverse()

        return " ".join(res)