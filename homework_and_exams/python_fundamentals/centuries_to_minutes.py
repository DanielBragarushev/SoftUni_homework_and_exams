centuries = int(input())
years_in_centuries = 100
days_in_year = 365.2422
hours_in_day = 24
minutes_per_hour = 60

years = centuries * years_in_centuries
days = int(years * days_in_year)
hours = hours_in_day * days
minutes = minutes_per_hour * hours

print(f"{centuries} centuries = "
      f"{years} years = {days} days = "
      f"{hours} hours = {minutes} minutes")
