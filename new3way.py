
# This is just the conditional part of the encoding.
# There are 6 different indels I J K L M N depending on the combination of where the gaps are

outSeq = ''
    for c,d,e in zip(org1,org2,org3):
        if c == '-' and d == '-' and e =='-':
        	pass
    	elif c != '-' and d == '-' and e =='-':
    		outSeq += 'N'
    	elif c == '-' and d != '-' and e =='-':
    		outSeq += 'L'
    	elif c != '-' and d != '-' and e =='-':
    		outSeq += 'K'
    	elif c == '-' and d != '-' and e !='-':
    		outSeq += 'J'
    	elif c == '-' and d == '-' and e !='-':
    		outSeq += 'M'
    	elif c == '-' and d != '-' and e =='-':
    		outSeq += 'I'
    	elif (c == 'A' and d == 'A' and e == 'A') or (c == 'T' and d == 'T' and e == 'T'):
            outSeq += 'a'
        elif (c == 'A' and d == 'A' and e == 'C') or (c == 'T' and d == 'T' and e == 'G'):
            outSeq += 'b'
        elif (c == 'A' and d == 'A' and e == 'G') or (c == 'T' and d == 'T' and e == 'C'):
            outSeq += 'c'
        elif (c == 'A' and d == 'A' and e == 'T') or (c == 'T' and d == 'T' and e == 'A'):
            outSeq += 'd'


