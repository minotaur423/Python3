# Minimum of Two
# Of two numbers, please, select one with minimum value.
numbers = '4530935 -7046905 -6053968 -3773809 -720333 -2827580 -3589271 -1194369 -1307901 -7419932 -9402924 4982685 3813773 1740340 7824338 -6500810 -6851464 1953149 -5295578 8531462 -2270289 -4221325 6832977 -9125445 -5010709 -5607113 2783857 7664374 404074 -5555971 -2627230 -5064991 -2602877 1318802 1161199 6676789 8491221 7571927 -4517579 -2816679 -9848005 -3920504 -7833994 3965768 7819836 9990344 7464957 -9031627 1943494 -7830620'
num_list = numbers.split()
length = len(num_list)
even_nums = slice(0,length,2)
odd_nums = slice(1,length,2)
even_list = num_list[even_nums]
odd_list = num_list[odd_nums]
for i in range(len(even_list)):
    if int(even_list[i]) < int(odd_list[i]):
        print(even_list[i], end=' ')
    else:
        print(odd_list[i], end=' ')