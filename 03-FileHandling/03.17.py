import re
tekst='To be or not to be, that is the question'
samogłoski=re.findall('[aeiou]',tekst)
print(samogłoski)