#count vowels 
name = "Anusha"
vowels =["A","E","I","O","U"]
count =0
for char in name.upper():
    if char in vowels:
        count =count+1
print(count)