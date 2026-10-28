class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0

        for bill in bills:
            # print(change)
            if bill == 5:
                fives += 1
            
            elif bill == 10:
            #check previous change, update 
                if fives <= 0:
                    return False
                else:
                    fives -= 1
                    tens += 1

            else:
                # print(change[5])
                if fives > 0 and tens > 0:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        
        return True

        