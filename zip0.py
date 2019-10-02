sales_north = [350, 287, 550, 891, 241, 653, 882]
sales_south = [551, 254, 901, 776, 105, 502, 976]
for s1, s2 in zip(sales_north, sales_south):
    print(s1 — s2)

# >>> -201
#     33
#     -351
#     115
#     136
#     151
#     -94