#The list ['a','bb','ccc','dddd', ...] that
# ends with 26 copies of the letter z.
aphla_num = []

for i in range(1,27) :
    aphla_num.append(chr(96 + i) * i)
        
print(aphla_num)