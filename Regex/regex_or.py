import re
#Note that each new line is a comand placed in the terminal. In simple terms, this is not a program.

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
#Batman

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
#'Tina Fey'

###################################################################


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
#'Batmobile'
mo.group(1)
#'mobile'

###################################################################
#Using question mark

# >>> batRegex = re.compile(r'Bat(wo)?man')
# >>> mo1 = batRegex.search('The Adventures of Batman')
# >>> mo1.group()
# 'Batman'
# >>> mo2 = batRegex.search('The Adventures of Batwoman')
# >>> mo2.group()
# 'Batwoman'


####################################################################
#Matching a Zero with a *
# >>> batRegex = re.compile(r'Bat(wo)*man')
# >>> mo1 = batRegex.search('The Adventures of Batman')
# >>> mo1.group()
# 'Batman'
# >>> mo2 = batRegex.search('The Adventures of Batwoman')
# >>> mo2.group()
# 'Batwoman'
# >>> mo3 = batRegex.search('The Adventures of Batwowowowoman')
# >>> mo3.group()
# 'Batwowowowoman'

                                #           \d
                                #           Any numeric digit from 0 to 9.
                                #           \D
                                #           Any character that is not a numeric digit from 0 to 9.
                                #           \w
                                #           Any letter, numeric digit, or the underscore character.
                                #           (Think of this as matching “word” characters.)
                                #           \W
                                #           Any character that is not a letter, numeric digit, or the
                                #           underscore character.
                                #           \s
                                #           Any space, tab, or newline character. (Think of this as
                                #           matching “space” characters.)
                                #           \S
                                #           Any character that is not a space, tab, or newline.

# Create email regex.
emailRegex = re.compile(r'''(
 [a-zA-Z0-9._%+-]+ # username
 @ # @ symbol
 [a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip, re
phoneRegex = re.compile(r'''(



(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip, re
phoneRegex = re.compile(r'''(

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
 for groups in phoneRegex.findall(text):
phoneNum = '-'.join([groups[1], groups[3], groups[5]])
if groups[8] != '':
phoneNum += ' x' + groups[8]
matches.append(phoneNum)
 for groups in emailRegex.findall(text):
matches.append(groups[0])

for groups in emailRegex.findall(text):
matches.append(groups[0])
# Copy results to the clipboard.
if len(matches) > 0:
pyperclip.copy('\n'.join(matches))
print('Copied to clipboard:')
print('\n'.join(matches))
else:
print('No phone numbers or email addresses found.')

)''', re.VERBOSE)

