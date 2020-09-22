import re
import datetime

text = 'ID: 123456 This is a testing class with Python with the number 123456'
# FindAll
matching = re.findall('CLASS|tHIS', text, re.IGNORECASE)

for result in matching:
    print(result)

# Search with replace
search = re.search('123456', text, re.IGNORECASE)
print(search)

if search:
    print('Se encontro el valor')
    text = re.sub('123456', '', text, re.IGNORECASE)
else:
    print('No se encontro el valor')

print(text)

# Split
text = 'ID:123456 This is a testing class with Python with the number 123456'

split = re.split(' ', text)
print(split)

concat = split[4] + ' ' + split[7]
print(concat)

for result in split:
    if result == 'ID:123456':
        print('Se encontró el código')
        break

# Search mas definido
text = 'Este texto contiene el valor del Scenario:HOY ahora'

PatronDeBusqueda = r'(?<=Scenario:)\w+'

variables = re.findall(str(PatronDeBusqueda), text, re.IGNORECASE)
for variable in variables:
    if variable == 'HOY':
        dateToday = str(datetime.date.today().strftime('%d-%m-%Y'))
        text = re.sub('(Scenario:)([^&.]+)', dateToday, text, re.IGNORECASE)
        continue

print(text)



