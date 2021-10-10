table = [["Name","Marks"],["Hasan",350]]
for x in table:

    print(("{:>10} {:>10}").format(*x))