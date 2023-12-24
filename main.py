# check if the phrenteses is right or wrongly orderd
# like [()] this is write
# but {)] this is wrong
# here we are going to use hash-map and stack data-structures
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack inplementation using array
        stack = []
        closetopen = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        for p in s:
            if p in closetopen:
                if stack and stack[-1] == closetopen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False

me = []
me.append(10)
me.append(20)
print(me[-2])