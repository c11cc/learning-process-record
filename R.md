#count frequency:
>y<-rpois(100,5)
>y
  [1]  3  5  6  5  6  4  2  2 10  5  6  7  8  7  4  3  7
 [18]  6  7  3  7  3  4 10  3  2  8  8  4  1  5  6  5  5
 [35]  3  7  5  1  5  4  1  2  7  5  4  5  3  4  5  7  5
 [52]  5  3  6  6  2  8  4  0 10  4  4  4  7  4  4  4  4
 [69]  0  6  3  9  3  4  3  4  4  3  3  5  6  9  3  8  2
 [86]  4  4  3  4  8  8  5 10  7  6  7  7  4  5  3
 
>x<-table(y)
> x
y
 0  1  2  3  4  5  6  7  8  9 10 
 2  3  6 16 22 16 10 12  7  2  4 

#get the name of x and take it as number
> k=as.numeric(names(x))
> k
 [1]  0  1  2  3  4  5  6  7  8  9 10 
> typeof(k)
[1] "double"
> k1=names(x)
> typeof(k1)
[1] "character"
