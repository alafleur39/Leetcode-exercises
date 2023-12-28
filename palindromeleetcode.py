class Solution(object): 
    def isPalindrome(self, x): #bool functions return true or false
        print("originial number",x)
        reversed_number = str(x)[::-1] #[::-1]  # we have to read it as only a string
        if str(x) == reversed_number:
            return True
        else:
            return False
        
