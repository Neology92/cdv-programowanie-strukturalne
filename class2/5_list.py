prog = ['Python', 'C#', 'JS', 'PHP']
print(prog)
print(type(prog))

first = prog[0]
print(first)
threeElements = prog[0:3]
print(threeElements)

last = prog[-1]
print(last)

secondFromEnd = prog[-2]
print(secondFromEnd)

#
prog.append('R')
prog.append('Python')
print(prog)

#
countElem = prog.count('Python')
print(countElem)

countElemsOfList = len(prog)
print(countElemsOfList)

#
anotherList = ['C', 'C++']
prog.extend(anotherList)
print('Lista prog: ' + str(prog))
# print(f'Lista prog: {str(prog)}')

#
new = prog
print('Lista prog: ' + str(new))
new.clear()
print('Lista prog: ' + str(new))
print('Lista prog: ' + str(prog))