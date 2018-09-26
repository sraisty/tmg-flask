from datetime import date
from util import get_date_from_string, make_full_name


ALLOWABLE_GENDERS = ('M', 'F')

class Athlete:

    def __init__(self, first_name, last_name, middle, gender, birth_date, 
             team_code, team_name, school_yr="", age=""):
        self.full_name = make_full_name(first_name, middle_initial=middle, last_name)

        self.set_gender(gender)
        self.set_team(team_code, team_name)
        self.set_age_birthdate(birth_date, age)
        self.set_school_yr(school_yr)
        self.set_division()


    def __repl__():
        print(self)



    def set_gender(self, gender):
        """
        """
        gender = gender.toupper()
        if gender in ALLOWABLE_GENDERS:
            self.gender = gender
        else:
            raise FileContentsError(tokens, 
                    "Bad I-Line record : athlete {} has invalid gender {}"
                    .format(f"{last_name}, {first_name}"))


    def set_team(self, team_code, team_name):
        """
        """
        if team_code:
            # TODO - fix things automagically (or with prompts) if the 
            # team_code and team_name don't match
            # only X chars are allowed or a code, so if user provides too long a 
            # code, just use the first 6 chars
            self.team_code = team_code[0:6]
            self.team_name = team_name
        else:
            self.team_code = "UNA"  #unattached athlete  
            self.team_code = "Unattached" 


    def set_age_from_birthdate(self, birth_date_str, 
                               age, cutoff_date=date.today()):
        """

            >>> athlete = Athlete("Raisty", "Sue", "", "F", "8/5/70", 
                                  "", "", "")
            >>> athlete.set_age_birthdate()
        """
        age = int(age)

        # Assume that the meet's "cutoff date" for calculating age is now
        # if cutoff_date == None:
        #     cutoff_date = date.today()


        birth_date = date(year, month, day)   
        year_diff = get_year_diff(birth_date, cutoff_date) 








if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:   #yay!
        app.run (debug=True)
