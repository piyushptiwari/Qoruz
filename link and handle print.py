import regex as re

lis=["Instagram","emails"]
para=str(input("Input paragraph: "))

link=re.findall(r"[A-Za-z0-9_%+-.]+"
               r"@[A-Za-z0-9.-]+"
               r"\.[A-Za-z]{2,5}",para)

han1=re.findall(r"[A-Za-z0-9_%+-.]+"
               r"@[A-Za-z0-9.-]+"
               r"\.[A-Za-z]{2,5}"
               r"/.[A-Za-z0-9]+",para)

han2=re.findall(r" @[A-Za-z0-9.-]+",para)

for i in range(0,len(link)-1):
    temp=han1[i].split('/')[0]
    if temp in link:
        link.remove(temp)
        
print("Instagram :", han1+han2)
print("emails :", link)


