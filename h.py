import sys
import time

# Page numbers
def pageNumbers(str, pn):
    if(pn!=""):
        str+=" pp."+pn+"."
    return str

# Format author list
def formatAuthorList(authorList):
    if(len(authorList)==1):
        return authorList[0]
    else:
        authorOut = ""
        for author in authorList:
            authorOut += author + " "
    return authorOut[:-1]

# book
def book(n,y,t,e,pl,p,pn):
    return pageNumbers(n+", "+y+". *"+t+".* "+e+" ed. "+pl+": "+p+".", pn)

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
    # Authors
    authorsBeforeFormat=[]
    authorList=[]
    moreAuthors = True
    while(moreAuthors):
        authorIn=raw_input("Author:")
        # If author is one word
        if(len(authorIn.split())<2):
            print "Error: Author name invalid"
        else:
            authorsBeforeFormat.append(authorIn)
        more=raw_input("More authors?")
        if(more.lower()=="no"):
            # if no authors in list
            if(len(authorsBeforeFormat)==0):
                print "Error: No authors"
            else:
                moreAuthors = False
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
    if(ref!="web"):
        pn=raw_input("Page numbers:")

    # Authors split and format
    for author in authorsBeforeFormat:
        # Split author to surename and firstname
        author=author.split()
        if(len(author)>2):
            authorList.append(author[len(author)-1].title()+", "+author[0][0].upper()+"."+author[1][0].upper()+".")
        else:
            authorList.append(author[1].title()+", "+author[0][0].upper()+".")

    # Format author list
    n = formatAuthorList(authorList)

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
