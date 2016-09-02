from collections import namedtuple

stock = namedtuple('stock', ['ticker', 'price','shares'])

rec = [('IBM',125.0,100), 
('GOOG',755.0, 200)]

for r in rec:
    print "r is {}".format(r) 
    print(*r)
    s = stock(*r)
    print(s)
 

