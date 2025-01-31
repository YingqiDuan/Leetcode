class TwoSum:

    def __init__(self):
        self.a={}

    def add(self, number: int) -> None:
        self.a[number]=self.a.get(number,0)+1

    def find(self, value: int) -> bool:
        for i in self.a:
            b=value-i
            if b in self.a:
                if b!=i or self.a[i]>1:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)