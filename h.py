import sys
import time

# Page numbers
def pageNumbers(str, pn):
    if(pn!=""):
        str+=" pp."+pn+"."
    return str

# book
def book(n,y,t,e,pl,p,pn):
    return pageNumbers(n+"., "+y+". *"+t+".* "+e+" ed. "+pl+": "+p+".", pn)

# web
def web(n,y,t,p):
    return n+"., "+y+", *"+t+"*.[online] Available at: <"+p+"> [Accessed "+time.strftime('%d %B %Y')+"]"
# Journal
def journal(n,y,t,jt,v,pn):
    pageNumbers(n+". "+y+". "+t+". *"+jt+"*. **"+v+"**.", pn)


# Start
title=raw_input("Name of file:")

while(True):
    # Get type
    ref=raw_input("Type:").lower()

    # User quit
    if(ref=="exit" or ref=="q"):
        sys.exit("ByeBye")

    # Get information
    a=raw_input("Author:")
    y=raw_input("Year:")
    t=raw_input("Title:").title()
    if(ref=="journal"):
        jt=raw_input("Journal title:").title()
        v=raw_input("Volume:")
    if(ref!="web" and ref!="journal"):
        e=raw_input("Edition:")
    if(ref!="web"):
        pl=raw_input("Publication location:").title()
    p=raw_input("Publisher:").title()
    pn=raw_input("Page numbers:")

    # Format author
    a=a.split()
    if(len(a)>2): # Middle name
        n=a[len(a)-1].title()+", "+a[0][0]+"."+a[1][0]
    else:
        n=a[1].title()+", "+a[0][0].upper()

    # Get type
    if(ref=="book"):
        harvard = book(n,y,t,e,pl,p,pn)
    elif(ref=="web"):
        harvard = web(n,y,t,p)
    elif(ref=="journal"):
        harvard = journal(n,y,t,jt,v,pn)
    else:
        print "Nope, that's not a thing"

    # Write to file
    print harvard
    open(title+".md", "a").write(harvard + "\n")
