
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
    	


    only the strong will survive 