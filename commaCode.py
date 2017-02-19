# Comma Code
# Returns a string with all the items separated by a comma and a space, with
# an *and* inserted before the last item

spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(listValue):
    for i in range((len(listValue)-1)):
        print(listValue[i] + ", ",end='')
    print("and " + listValue[-1])


commaCode(spam)
