nhead = int(input())
nleg = int(input())

def animals(nhead,nleg):
    if nleg % 2 != 0 or nhead == 0 or nhead > nleg:
        print('no solution')
    else:
        rab = (nleg - 2 * nhead)/2
        chic = nhead - rab
    return(int(rab),int(chic))
print(animals(nhead,nleg))