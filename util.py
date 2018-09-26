"""
MODULE DOCSTRING STUFF


"""

from datetime import date

def get_date_from_string(datestring):
    """ Converts a string like MM/DD/YY or M/D/YYYY into a datetime.date
        instance.

        Checks for bad values for month number, day number.
        Also handles both 2 character years and 4 character years.  If the
        year of a 2-digit date is more than 5 years in the future, assume
        it's from the last century.

        >>> parse_date_from_string("1/1/17")
        datetime.date(2017, 1, 1)
        >>> parse_date_from_string("8/5/70")
        datetime.date(1970, 8, 5)

    """
    try:
        month,day,year = [int(date_num) for date_num in datestring.split('/')]
    except:
        Exception(f"Date string ({datestring}) must be in MM/DD/YY format.")
        return None

    # If a 2-digit year is provided, assume it's from 1900s if it's greater
    # than current year - 2000. Otherwise, assume it's from the 2000s.        
    if year < 100:     
    # got a 2-digit year in the datestring. Make it 4digits.    
        if year > date.today().year - 2000 + 5:
            year += 1900
        else:
            year += 2000

    #sanity check for years
    if year < 1900 or year > 2023:  
        raise Exception(f"Year must be > 1900 and < 2023: {datestring}")

    if month < 1 or month > 12:
        raise Exception(f"Month in date is out of range: {datestring}")

    if day < 1 or day > 31:
        raise Exception(f"Month in date is out of range: {datestring}")

    #sanity check for day values given a particular month
    # To do handle year 2000 (no leap year)
    if ((month in [4, 6, 9, 11] and day > 30) or
        (month == 2 and 
            ((day > 28 and (year%4 != 0 or year == 2000)) or
             (day > 29 and (year%4 == 0 and year!= 2000))))):
        raise Exception(f"Day in date is out of range: {datestring}")

    return date(year, month, day)  


def make_full_name(first_name, last_name, middle_initial=""):
    """
    # TODO - this doesn't use self. Should it even be a mthod?

    # Note that it's possible that middle might be more than one 
    # character, so even if they provide something else, just use first char

    # Note that I am tempted to make sure that the names don't contain
    # any numbers or weird punctuation and to force them all into title case
    # and to not include any spaces.  
    # However, I'm not going to because of legit names like
    # Rip van Winkle
    # We will use the first name and Last name exactly as the user entered
    # it with the same capitalization and/or punctuation
    # We're even allowing the empty string because some people legally only
    # have one name.
    """
    if middle_initial:
        return f"{first_name} {middle_initial[0:1]}. {last_name}"
    else:
        return f"{first_name} {last_name}"



def get_year_diff(earlier_date, later_date):
    """ Takes in two dates and returns the difference in years
         between them.
    """
    year_diff = later_date.year - earlier_date.year
    if later_date.month < earlier_date.month:
        return year_diff - 1
        
    elif later_date.month == earlier_date.month:
        if cutoff_date.day <  earlier_date.day:
            return year_diff - 1
                       
    return year_diff # later_date.month > earlier_date.month