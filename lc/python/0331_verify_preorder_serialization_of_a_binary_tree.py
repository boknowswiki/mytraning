# binary tree and stack
# someone's answer:

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        top = -1
        preorder = preorder.split(',')
        for s in preorder:
            stack.append(s)
            top += 1
            while(self.endsWithTwoHashes(stack,top)):
                h = stack.pop()
                top -= 1
                h = stack.pop()
                top -= 1
                if top < 0:
                    return False
                h = stack.pop()
                stack.append('#')
            #print stack
        if len(stack) == 1:
            if stack[0] == '#':
                return True
        return False

    def endsWithTwoHashes(self,stack,top):
        if top<1:
            return False
        if stack[top]=='#' and stack[top-1]=='#':
            return True
        return False
