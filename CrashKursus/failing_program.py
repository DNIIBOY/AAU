"""
Original code:

school = 'Aalborg University'
class = Programering for matematikere
number of lecures = 12
minutes per lecture = 130
total minutes = number of lectures * hours per
lecture "Compute total minutes for entire class"
total hours = total minutes / 60
remaining minutes = total minutes % 60
print 'The class {Class} is held at {school} over
{number of lectures} lectures for at total of {total
hours} hours and {remaining minutes}"
"""

school = "Aalborg University"  # Use consistent quotes
school_class = "Programering for matematikere"  # Use quotes, don't use reserved words
number_of_lectures = 12  # No spaces in variable names, spelling mistake
minutes_per_lecture = 130  # No spaces in variable names
total_minutes = (
    number_of_lectures * minutes_per_lecture
)  # No spaces in variable names, undefined variable
lecture = "Compute total minutes for entire class"  # Equals sign missing
total_hours = total_minutes / 60  # No spaces in variable names
remaining_minutes = total_minutes % 60  # No spaces in variable names

# Missing f-string and parentheses and incosistent qoutes and variable names, newlines and string contents
print(
    f"The class {school_class} is held at {school} over {number_of_lectures} lectures for at total of {total_hours} hours and {remaining_minutes} minutes"
)
