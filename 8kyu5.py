# Your function takes two arguments:

# current father's age (years)
# current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

# ====

def twice_as_old(dad_years_old, son_years_old):

    if dad_years_old > son_years_old * 2:
        compare = dad_years_old - son_years_old
        years_ago = compare - son_years_old
        print("The father was twice as old as his son after " +str(years_ago)+" years.")
    
    elif dad_years_old < son_years_old * 2:
        compare = dad_years_old - son_years_old
        years_ago = son_years_old - compare
        print("The father was twice as old as his son " +str(years_ago)+" years ago.")
    elif dad_years_old == son_years_old * 2:   
        print("The father is twice as old as his son.")
    else:
        return 0


twice_as_old(36, 7)
