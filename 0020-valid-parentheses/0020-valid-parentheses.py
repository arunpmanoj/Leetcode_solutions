class Solution:
    def isValid(self, s: str) -> bool:
        s=s.replace(" ","")
        stk=[]
        for ele in s:
            if(ele=='{'):
                stk.append("}")
            elif(ele=="("):
                stk.append(")")
            elif ele=="[" :
                    stk.append("]")
            elif not stk or ele!=stk.pop():#checking stack is empty or the ele is same as popped elemnt
                return False
        if stk:
            return False
        else:
            return True