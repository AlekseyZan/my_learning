t = input()
r = input()
if t==r:
    print("ничья")
elif (t=="камень" and r=="ящерица") or (t=="камень" and  r=="ножницы") or (t=="ножницы" and r=="бумага") or (t=="ножницы" and  r=="ящерица") or (t=="бумага" and r=="камень") or (t=="бумага" and r=="Спок") or (t=="ящерица" and r=="бумага") or (t=="ящерица" and r=="Спок") or (t=="Спок" and r=="камень") or (t=="Спок" and r=="ножницы"):  
    print("Тимур")
else:
    print("Руслан")  


                