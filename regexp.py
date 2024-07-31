import re
class regexp:
    """Simple newbie re regex examples."""
    r=re.compile('iterator')
    
    print('re.match examples')
    print(r.match('iterator_my'))
    print(r.match('not tor_my'))
    
    print('re.search examples')
    print(r.search('iterator_my'))
    print(r.search('not tor_my'))
    print('re.search applications')
    print(None==r.search('iterator_my'))
    print(None==r.search('not tor_my'))
# re.match examples
# <re.Match object; span=(0, 8), match='iterator'>
# None
# re.search examples
# <re.Match object; span=(0, 8), match='iterator'>
# None
# re.search applications
# False
# True
