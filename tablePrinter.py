#table printer
#displays justified text in a table


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


#takes the maximum length of strings in a sub-list

maxJust=[0]*len(tableData)

for outer in range(len(tableData)):
        for inner in range(len(tableData[outer])):
            if len(tableData[outer][inner]) > maxJust[outer]:
                maxJust[outer] = len(tableData[outer][inner])
print(maxJust)                


#prints the justified table

def printTable(table):
    for inner in range(len(table[0])):
        for outer in range(len(table)):
            print(table[outer][inner].rjust(maxJust[outer]),end=' ')
        print('')

printTable(tableData)            
