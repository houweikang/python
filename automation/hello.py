import re
Nregex = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})')
mo = Nregex.search('djklafjfeiflan(123)-124-1324dsfr')
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group())
print(mo.groups())