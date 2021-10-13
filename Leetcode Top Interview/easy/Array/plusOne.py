class Solution:

    # 自己的寫法，效率上看起來不用改
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.reverse()
        
        carry = 1
        for i in range(len(digits)):
            if digits[i] + carry > 9:
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
                break
        
        digits.reverse()
        
        if carry == 1:
            digits.insert(0, 1)
        
        return digits