class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1

        for i in range(len(digits)-1,-1,-1):
            sum = carry+digits[i]
            digit=sum
            # print(digit)
            # print(digit%10)
            if sum>9:
                digit=sum%10
                
                carry=(sum//10)%10
                # sum=sum%10
            else:
                carry=0
            digits[i]=digit
        if carry:
            digits.insert(0,carry)
        return digits