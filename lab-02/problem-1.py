from logic import TruthTable

# 1. not a
table1 = TruthTable(['a'], ['-a'])
table1.display()

print()

# 2. a and b
table2 = TruthTable(['a', 'b'], ['a and b'])
table2.display()

print()

# 3. a or b
table3 = TruthTable(['a', 'b'], ['a or b'])
table3.display()

print()

# 4. if a then b
table4 = TruthTable(['a', 'b'], ['a -> b'])
table4.display()

print()

# 5. a if and only if b
table5 = TruthTable(['a', 'b'], ['a <-> b'])
table5.display()

print()
