Pyota may be an imitation of iota() function in Go,C++ etc.

# Use as follows:

``````
newiota = Iota()

newiota.__parseInput__('''
    A
    B = iota
    C
    _
    D = 6*8
    E
    F = iota+100
''')

print(newiota.get_values())
print(newiota.F)