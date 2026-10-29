def brackets_matching(str):
    openings={'[','{','('}
    closings={']','}',')'}
    stack=[]

    for ch in str:
        if ch in openings:
            stack.append(ch)
        elif ch in closings:
            if not stack:
                print("False")
                break
            else:
                if (stack[-1]=='[' and ch==']') or (stack[-1]=='{' and ch=='}') or(stack[-1]=='(' and ch==')'):
                    stack.pop()
                else:
                    print("False")
                    break
    else:
        print("True")
str="({[]})"
brackets_matching(str)