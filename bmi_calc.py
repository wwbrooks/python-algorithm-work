# Language: Python 3.9.x
# Creation: Thu Nov 7 13:06:03 PST 2024
# Filename: bmi_calc.py
# Descr:    A simple program for demonstrating the usefulness of Python
#           exception handling. For a given value of weight in pounds and 
#           height (in inches), calculates then outputs the corresponding
#           body-mass index. 
#
#           A BMI calculation provides a single number, which the Centers
#           for Disease Control and Prevention (CDC) categorizes as follows:
#
#              • A BMI of less than 18.5 suggests underweight.
#              • A BMI of between 18.5 and 24.9 suggests a healthy weight range.
#              • A BMI of between 25 and 29.9 may indicate overweight.
#              • A BMI of 30 or higher may indicate obesity.
#
#           However, the CDC also notes that BMI does not assess an individual’s
#           body composition or health. It is a screening tool that people
#           should use alongside other tests and assessments to determine
#           potential health risks.
#
# >>> Enter weight (in lbs): 190
# >>> Enter height (in in.): 66
# BMI: 30.7
# (CDC: 18.6-24.9 is normal)
#


def bmi(weight, height):
    """ Returns the the corresponding body-mass index (BMI is one measure used
    to determine normal weight for a given height) as floating point value.
    For example,

    >>> bmi(137, 73)
    18.07299680990805

    """
    result = (float(weight) / float(height * height)) * 703
    return result


def get_users_values():
    """ Returns a tuple representing the weight and height values entered by
    the user, both as integer values.
    """    
    weight = int(input("Enter weight (in lbs): "))
    height = int(input("Enter height (in in.): "))
    return (weight, height)


#
if __name__ == "__main__":
    (wght, hght) = get_users_values()
    their_bmi = bmi(wght, hght)

    print(f'BMI: {their_bmi:.1f}')
    print('(CDC: 18.6-24.9 is normal)\n')
# Source www.cdc.gov



#                            end of file                                       #
