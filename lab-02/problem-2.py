from logic import TruthTable

prop_1 = input('Enter proposition 1: ')
prop_2 = input('Enter proposition 2: ')

table_1 = TruthTable(['p', 'q'], [prop_1])
table_2 = TruthTable(['p', 'q'], [prop_2])

table_1_results = []
for row in table_1.table:
    # add last column (the result) to table1_results
    table_1_results.append(row[-1])

equivalent = True
for i, row in enumerate(table_2.table):
    # check if the last column of table2 is equal to the last column of the same row in table1
    if row[-1] != table_1_results[i]:
        equivalent = False
        break

if equivalent:
    print('The propositions are equivalent')
else:
    print('The propositions are not equivalent')
