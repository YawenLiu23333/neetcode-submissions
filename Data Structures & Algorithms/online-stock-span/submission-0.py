class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        ind = 1

        if not self.stack:
            self.stack.append([price, ind]) #PRICE AND SPAN IN PARIS
            return self.stack[-1][1]
        elif self.stack[-1][0] > price:
            self.stack.append([price, ind])
            return self.stack[-1][1]
        
        
        while self.stack and self.stack[-1][0] <= price:
            print(self.stack)
           
            stackP, stackIND = self.stack.pop() 
            ind += stackIND
            
        self.stack.append([price, ind]) 

        return self.stack[-1][1]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)