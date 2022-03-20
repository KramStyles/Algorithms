def pages(summary):
    hold = counter = 0
    for num in range(1,summary+1):
        if hold >= summary:
            return print(counter)
        hold += len(str(num))
        counter += 1
    return print(counter)

def pages_shorter(summary):
    pagecount=0
    i=0
    while summary != pagecount:
        i+=1
        pagecount+=len(str(i))
    return i

pages_shorter(25)
pages_shorter(5)
pages(185)
pages(1095)
pages(660)
