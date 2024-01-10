#leetcode question

# s = "MCMXCIV"
# M = 1000, CM = 900, XC = 90 and IV = 4.= 1994

class Solution(object):
    def romanToInt(self, s):   # we are converting roman numerals to integers
        count = 0
        
        if s == "":    # we set s to a empty string
            return count

        for x in range(0, len(s)): #we did this to start at 0 and then stop at the number of elements in our string
            #switch case 
            #s = IV 
            if s[x] == 'I' and s[x+1] == 'V': #s[0] = I and s[1] = V 
                #we dont want to use I or V again from the string
                #That specific location
                #x + 1 to turn x from x = 1 in the loop to become x = 2
                #x[2] and check for its if statements
                count += 4 #count adds 4 to the total
            elif s[x] == 'I' and s[x+1] == 'X':
                count += 9
            elif s[x] == 'X' and s[x+1] == 'L':
                count += 40
            elif s[x] == 'X' and s[x+1] == 'C':
                count += 90
        
            elif s[x] == 'C' and s[x+1] == 'D':
                count += 400
               
            elif s[x] == 'C' and s[x+1] == 'M':
                count += 900

            elif s[x] == 'I':
                count += 1  # we add 1 to our count 
            elif s[x] == "V":
                count += 5
            elif s[x] == "X":
                count += 10
            elif s[x] == "L":
                count += 50
            elif s[x] == "C":
                count += 100
            elif s[x] == "D":
                count += 500
            elif s[x] == "M":
                count += 1000
            
        return count

self1 = None
s = "MCMXCIV"
result = Solution.romanToInt(self1, s)
print(result)