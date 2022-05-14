import regex as re

lis=["Instagram","emails"]
para=str(input("Input paragraph: "))

link=re.findall(r"[A-Za-z0-9_%+-.]+"
               r"@[A-Za-z0-9.-]+"
               r"\.[A-Za-z]{2,5}",para)

han1=re.findall(r"[A-Za-z0-9_%+-.]+"
               r"@[A-Za-z0-9.-]+"
               r"\.[A-Za-z]{2,5}"
               r"/.[A-Za-z0-9]",para)

han2=re.findall(r" @[A-Za-z0-9.-]+",para)

for i in range(0,len(link)):
    temp=link[i].split('/')
    if temp[0] in han1:
        link.remove(temp[0])
        
print("Instagram :", han1+han2)
print("emails :", link)


