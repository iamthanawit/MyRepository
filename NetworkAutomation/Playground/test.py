string = "11 - 13, 12 - 14, 13 - 15"

mydict = dict((x.strip(), int(y.strip()))
            for x, y in (element.split('-')
                         for element in string.split(', ')))

print(mydict)


mydict = dict((x.strip(), int(y.strip())) for x, y in (element.split('-') for element in string.split(', ')))