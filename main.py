#kodilla zadanie Katarzyna Kuich
#Lista zakupów
#Idę do Piekarnia, kupuję tu następujące rzeczy: ['Chleb', 'Pączek', 'Bułki'].
#Idę do Warzywniak, kupuję tu następujące rzeczy: ['Marchew', 'Seler', 'Rukola'].
#W sumie kupuję 6 produktów.

print("\nZadanie 1")
print("Lista zakupow:")
#product list
lista= {'piekarnia':['chleb', 'Pączek', 'bułki','ser'],
'warzywniak':['Marchew', 'seler', 'rukola']
}

#loop add 

count=0
for x,y  in lista.items():
  for z in y:
      for i in range(0,len(y)):
        y[i]=y[i].replace(y[i],y[i].capitalize())
  print("Idę do ",x.capitalize(),"kupuję tu następujące rzeczy:",y)
  count=len(y)+count
print("W sumie kupuję ",count," produktów.")
print("commit1")