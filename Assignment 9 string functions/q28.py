def rotation_equal(s1,s2):
    if len(s1)==len(s2):
        for _ in range(len(s1)):
            if s1==s2:
                print("True")
                break
            else:
                lis=list(s1)
                temp=lis[0]
                for i in range(len(lis)-1):
                    lis[i]=lis[i+1]
                lis[len(lis)-1]=temp
                s1="".join(lis)
        else:
            print("False")
    else:
        print("False")
        return
s1='abcd'
s2='cda'
rotation_equal(s1,s2)