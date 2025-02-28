class StringIterator:

    def __init__(self, compressedString: str):
        stack=[]
        prev=''
        num=0
        for x in compressedString:
            if x.isdigit():
                num=num*10+int(x)
            else:
                stack.append([prev,num])
                prev=x
                num=0
        self.stack=stack[1:]+[[prev,num]]
        return

    def next(self) -> str:
        if self.stack:
            x=self.stack[0][0]
            self.stack[0][1]-=1
            if self.stack[0][1]==0:
                self.stack.pop(0)
            return x
        return ' '

    def hasNext(self) -> bool:
        return len(self.stack)>0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()