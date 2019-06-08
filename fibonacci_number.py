# print 10 fibonacci number
# define before calling, this is different from Perl

def calculation(m,n,counts):
  while(counts<10):
    counts+=1
    m,n=n,m+n
    print("%d:%d" %(counts,m))
  
calculation(0,1,0)