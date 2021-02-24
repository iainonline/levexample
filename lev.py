import Levenshtein as lev

a = 'compare this'
b = 'to this'

Distance = lev.distance(a.lower(), b.lower())
Ratio = lev.ratio(a.lower(), b.lower())

print('Levenshtein distance is: ', Distance)
print('Levenshtein ratio is: ', Ratio)