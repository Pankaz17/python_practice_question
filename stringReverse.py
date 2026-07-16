def reverseTextwitSlicing(b):
    loopRange = len(b)
    reversetext = ""
    for i in range(loopRange + 1):
       slicingStart = loopRange - i
       slicingend = slicingStart + 1
       singleChar = b[slicingStart:slicingend]
       reversetext += singleChar
    print(reversetext)
    
    
reverseTextwitSlicing("Pankaj") 