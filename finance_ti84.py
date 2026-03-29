P=(24,12,4,2,1)
L=("Qz","Mo","Tr","Se","An")
R=round
I=input
F=float
N=int
def G(s):
 print("1:Qz 2:Mo 3:Tr")
 print("4:Se 5:An")
 return N(I("Per "+s+":"))
def T():
 t=F(I("Taux%:"))/100
 p=G("taux")
 f=P[p-1]
 if f>1:t=(1+t)**f-1
 return t
while True:
 print("=FINANCE=")
 print("1:I.Simpl 2:I.Comp")
 print("3:Actual 4:Remb")
 print("5:Amort 6:Capit")
 print("0:Quit")
 c=N(I("?:"))
 if c==0:break
 if c==1:
  c0=F(I("K:"));t=T()
  n=F(I("An:"));i=c0*t*n
  print("T.an:",R(t*100,4),"%")
  print("Int:",R(i,2))
  print("Mt:",R(c0+i,2))
 elif c==2:
  c0=F(I("K:"));t=T()
  n=N(I("An:"))
  p=N(I("Cp/an:"))
  m=c0*(1+t/p)**(n*p)
  print("T.an:",R(t*100,4),"%")
  print("Mt:",R(m,2))
  print("Int:",R(m-c0,2))
 elif c==3:
  v=F(I("VF:"));t=T()
  n=N(I("An:"))
  print("T.an:",R(t*100,4),"%")
  print("VA:",R(v/(1+t)**n,2))
 elif c==4:
  c0=F(I("K:"));t=T()
  p=G("vers");n=N(I("Ech:"))
  tp=(1+t)**(1/P[p-1])-1
  if tp==0:a=c0/n
  else:a=c0*tp/(1-(1+tp)**(-n))
  print("T.an:",R(t*100,4),"%")
  print("T."+L[p-1]+":",R(tp*100,4),"%")
  print("Ech:",R(a,2))
  print("Tot:",R(a*n,2))
  print("Int:",R(a*n-c0,2))
 elif c==5:
  c0=F(I("K:"));t=T()
  p=G("vers");n=N(I("Ech:"))
  f=P[p-1]
  tp=(1+t)**(1/f)-1
  if tp==0:a=c0/n
  else:a=c0*tp/(1-(1+tp)**(-n))
  r=c0
  print("T.an:",R(t*100,4),"%")
  print("T."+L[p-1]+":",R(tp*100,4),"%")
  print("N|E|I|C|R")
  for k in range(1,n+1):
   i=r*tp;cp=a-i;r=r-cp
   if r<0:r=0
   print(k,R(a,1),R(i,1),R(cp,1),R(r,1))
   if k%f==0 and k<n:I(">")
 elif c==6:
  print("1:Vers 2:Cap")
  ch=N(I("?:"));t=T()
  p=G("vers")
  tp=(1+t)**(1/P[p-1])-1
  if ch==1:
   v=F(I("K vise:"))
   n=N(I("Ech:"))
   if tp==0:a=v/n
   else:a=v*tp/((1+tp)**n-1)
   print("T.an:",R(t*100,4),"%")
   print("T."+L[p-1]+":",R(tp*100,4),"%")
   print("Vers:",R(a,2))
   print("Tot:",R(a*n,2))
   print("Gain:",R(v-a*n,2))
  else:
   a=F(I("Vers:"))
   n=N(I("Ech:"))
   if tp==0:v=a*n
   else:v=a*((1+tp)**n-1)/tp
   print("T.an:",R(t*100,4),"%")
   print("T."+L[p-1]+":",R(tp*100,4),"%")
   print("Cap:",R(v,2))
   print("Tot:",R(a*n,2))
   print("Gain:",R(v-a*n,2))
 I("[OK]")
