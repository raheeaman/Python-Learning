g1=input('g1:')
g2=input('g2:')

total=0
gc=0
x=int(g1)
y=int(g2)

if x>=50:
    total=total+x
    gc=gc+1
if y>=50:
    total=total+y
    gc=gc+1
if gc>0:
    print(total/gc)
else:
    print(0.0)
