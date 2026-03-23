def count_string(strings):
    i = 0
    for x in strings:
        if len(x) >= 2 and x[0] == x[-1]:
            i +=1

    return i                 

print(count_string(['ded','wdfdw','ses']))    