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
