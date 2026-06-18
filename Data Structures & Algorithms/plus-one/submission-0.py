class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        for i in range(len(digits) -1, -1, -1):
            if i == len(digits) - 1:
                curr_sum = digits[i] + 1
                digits[i] = curr_sum % 10
                carry = curr_sum // 10
                continue

            curr_sum = digits[i] + carry
            digits[i] = curr_sum % 10
            carry = curr_sum // 10

        if carry:
            digits.insert(0, carry)

        return digits