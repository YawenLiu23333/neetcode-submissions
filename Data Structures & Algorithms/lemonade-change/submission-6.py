class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0}

        for bill in bills:
            print(change)
            if bill == 5:
                change[5] += 1
            
            elif bill == 10:
            #check previous change, update 
                if change[5] <= 0:
                    return False
                else:
                    change[5] -= 1
                    change[10] += 1

            else:
                print(change[5])
                if change[5] < 1 or change[5]* 5 + change[10] *10 < 15:
                    return False
                else:
                    if change[10] > 0:
                        change[10] -= 1
                        change[5] -= 1
                    else:
                        change[5] -= 3
        
        if min(change.values()) < 0:
            return False
        return True

        