### Developed by am4t0r
### 1.4.2019
### twitter : https://twitter.com/bozkurtyakupp

import re 											# import regex
content = input("Content : ")						# Get a content
s = re.sub(r'[=]', r'":"', content)					# Replace ' = ' char to ' ":" ' 
s2 = re.sub(r'[&]', r'","', s)						# Replace ' & ' char to ' "," '
s3 = re.sub(r'^|$', r'"', s2)						# Add double quotation marks to the beginning and end of content
print("""

**********************************************************
*                                                        *
*     URL Query Strings Parametres to Json Data          *	
*                 author : am4t0r                        *
*                                                        *
**********************************************************

""")
print(*"_"*12 , "JSON DATA" , *"_"*12, "\n")
print(s3+'\n')



