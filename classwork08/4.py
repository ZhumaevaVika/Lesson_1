a = ['sdk', 'sussks', 'susus', 'slkdfs0', 'fkjhsusls']
c = list(filter(lambda x: x.find('sus') > -1, a))
print(*c)