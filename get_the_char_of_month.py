
import calendar

def get_month_list(abv=False):
    '''
    abv[abbreviation] is false
    if abv is true, the abv form of month will be used
    '''
    if not abv:
        m = calendar._localized_month('%B')
    else:
        m = calendar._localized_month('%b')
    mlist = []
    for i in range(1,13):
        mlist.append(m[i])
    return mlist

