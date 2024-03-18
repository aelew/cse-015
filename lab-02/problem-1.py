from logic import TruthTable

# 1. not a
table_1 = TruthTable(['a'], ['-a'])
table_1.display()

print()

# 2. a and b
table_2 = TruthTable(['a', 'b'], ['a and b'])
table_2.display()

print()

# 3. a or b
table_3 = TruthTable(['a', 'b'], ['a or b'])
table_3.display()

print()

# 4. if a then b
table_4 = TruthTable(['a', 'b'], ['a -> b'])
table_4.display()

print()

# 5. a if and only if b
table_5 = TruthTable(['a', 'b'], ['a <-> b'])
table_5.display()

print()
