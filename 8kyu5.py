# Your function takes two arguments:

# current father's age (years)
# current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

# ====

def twice_as_old(dad_years_old, son_years_old):
    subtrac = int(dad_years_old) - int(son_years_old)
    years_ago = int(subtrac) - int(son_years_old)
    print("The father was twice as old as his son " +years_ago+" years ago" )

print(twice_as_old(34, 16))