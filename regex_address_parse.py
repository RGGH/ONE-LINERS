t= '''\n\t\t\t\t\t\t\n\t\t\t\t\t\t68169\xa0\n\t\t\t\t\t\tMannheim\n\t\t\t\t\t\t\n\t\t\t\t\t\t',
 '\n\t\t\t\t\t'''

t='''\n\t\t\t\t\t\tAnna-Sammet-Str. Süd ? ?',
 '\n\t\t\t\t\t\t\n\t\t\t\t\t\t68309\xa0\n\t\t\t\t\t\tMannheim\n\t\t\t\t\t\t\n\t\t\t\t\t\t',
 '\n\t\t\t\t\t'''
					
import re

t = t.replace("\\t", "")

city = ""
street = ""

full_address = re.findall(r"(\w[A-Za-z]+)",t)

city = full_address[-1]

postcode = re.findall(r"(\d{5})",t)
postcode = ("".join(postcode))

street = full_address[:-2]
street = " ".join(street)

print(f'city={city}\n')
print(f'postcode={postcode}\n')
print(f'street={street}\n')
#
