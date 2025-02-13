
# class FifoStack:
#     def __init__(self,c):
#         self.count=c
#         self.ml=[]
#     def push(self,num):
#         if self.count<=len(self.ml):
#             print("no space new element")
#         else:
#             self.ml.insert(0,num)
#     def __str__(self):
#         return str(self.ml)

    # def pop(self):
    #     if not self.ml:
    #         print("no clean to remove")
    #     else:
    #         del self.ml[0]
    #     return self.ml[0]
    # def pop(self):
    #     r = self.ml[0]
    #     for i in range(len(self.ml)-1):
    #         self.ml[i] = self.ml[i+1]
    #     self.ml.pop()
    #     return r

# s=FifoStack(3)
# s.push(12)
# s.push(3) 
# s.push(4)
# print(s)
# print(s.pop())
# s.pop()
# s.pop()
# print(s)

class Mstring:
    def __init__(self,mstr):
        if not isinstance(mstr,str):
            raise TypeError("Only strings can be set")
        else:
            self.__mstr=mstr
    def get(self):
        return self.__mstr
    def set(self, mstr):
        if not isinstance(mstr,str):
            raise TypeError("Only strings can be set")
        else:
            self.__mstr=mstr
    def upper(self):
        tmp=""
        for el in self.__mstr:
            n=ord(el)
            if 97<=n<=122:
                el=chr(n-32)
            tmp+=el
        self.__mstr= tmp
    def lower(self):
        tmp=""
        for el in self.__mstr:
            n=ord(el)
            if 65<=n<=90:
                el=chr(n+32)
            tmp+=el
        self.__mstr=tmp
    def isdigit(self):
        for el in self.__mstr:
            if not (48<=ord(el)<=57):
                return False
            return True 
    def isalpha(self):
        is_alpha=True
        for el in self.__mstr:
            if not (65<=ord(el)<=90 or 97<=ord(el)<=122):
                is_alpha=False
        return is_alpha
    def title(self):
        tmp=""
        capitalize=True
        for el in self.__mstr:
            n=ord(el)
            if el.isalpha():
                if capitalize and 97<=n<=122:
                    el=chr(n-32)
                elif not capitalize and 65<=n<=90:
                    el=chr(n+32)
                capitalize=False
            else:
                capitalize=True
            tmp+=el
        self.__mstr=tmp
s=Mstring("Heloo pello12")
s.upper()
print(s.get())
s.lower()
print(s.get())
print(s.isdigit())
print(s.isalpha())
s.title()
print(s.get())

