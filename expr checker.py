para=str(input("input Paragraph :"))

def balc(para):
    keep=[]
    exp=["(","[","{"]
    for i in para:
        if i in exp:
            keep.append(i)
        else:
            if not keep:
                return False
            j=keep.pop()
            if j=='(':
                if i!=")":
                    return False
            if j=='{':
                if i!="}":
                    return False
            if j=='[':
                if i!="]":
                    return False
    if keep:
        return False
    return True


if (balc(para)):
    print("Balanced")
else:
    print("Not Balanced")
                
