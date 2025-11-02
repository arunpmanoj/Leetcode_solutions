class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num=""
        for i in range(len(number)):
            if digit == number[i]:
                new_number=number[:i]+number[i+1:]
                if new_number>max_num:
                    max_num=new_number
        return max_num
            
            