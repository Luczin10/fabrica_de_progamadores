'''import os, sys
print("Numero de paramêtros %d"  % len(sys.argv))
for n,p in enumerate(sys.argv):
    
    
    print("Parêmetro %d = %s"%(n,p))
    try:    
        os.mkdir("%s" % p)
        

    except:
        print("erro")
        
'''
a=['p''y''t''h''o''n' ]
b=a[0]
print(b)