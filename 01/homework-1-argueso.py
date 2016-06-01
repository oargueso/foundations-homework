#Olaya Argueso Perez
print ("May 23, 2016")
#Homework

year_of_birth = input("What year were you born in?")
age = 2016 - int(year_of_birth)
if age < 0:
    print ("Are you sure?")
    year_of_birth = input("What year were you born in?")
    age = 2016 - int(year_of_birth)
else:
    print ("You are ", age, "years old")

heartbeats = age * 37843200
print ("So your heart has already beaten roughly", heartbeats, "times since you were born")

bluewhaleheartbeats = age * (37843200/12)
print ("By the same time, the heart of a blue whale born in ", year_of_birth, "has beaten roughly ", bluewhaleheartbeats, "times")

rabbitheartbeats = age * (37843200*2.85)
if rabbitheartbeats > 1000000000:
    print ("And the heart of a rabbit born in ", year_of_birth, "has beaten roughly ", rabbitheartbeats/10000000, " billion times")
else:
    print ("And the heart of a rabbit born in ", year_of_birth, "has beaten roughly ", rabbitheartbeats, "times")

venusyears = age * 1.6
print ("You are ", venusyears, "years old in Venus years")

neptuneyears = age/165
print ("You are ", neptuneyears, "years old in Neptune years")

if age > 41:
    print ("Your are roughly", age - 41, "older than me")
elif age < 41:
    print ("You are roughly", 41 - age, "younger than me")

if int(year_of_birth)%2 == 0:
    print ("You were born in an even year")
else:
    print("Your were born in an odd year")

if int(year_of_birth) <= 1975:
    print ("The Pittsburgh Steelers have won the Super Bowl 6 times since you were born")
elif int(year_of_birth) <= 1976:
    print ("The Pittsburgh Steelers have won the Super Bowl 5 times since you were born")
elif int(year_of_birth) <= 1979:
    print ("The Pittsburgh Steelers have won the Super Bowl 4 times since you were born")
elif int(year_of_birth) <= 1980:
    print ("The Pittsburgh Steelers have won the Super Bowl 3 times since you were born")
elif int(year_of_birth) <= 2006:
    print ("The Pittsburgh Steelers have won the Super Bowl 2 times since you were born")
elif int(year_of_birth) <= 2009:
    print ("The Pittsburgh Steelers have won the Super Bowl one time since you were born")
else:
    print("The Pittsburgh Steelers have not won the Super Bowl since you were born")

if int(year_of_birth) >= 1933 and int(year_of_birth) < 1945:
    print ("Franklin D. Roosevelt was in office when you were born")
elif int(year_of_birth) >= 1945 and int(year_of_birth) < 1953:
    print ("Harry Truman was in office when you were born")
elif int(year_of_birth) >= 1953 and int(year_of_birth) < 1961:
    print ("Dwight Eisenhower was in office when you were born")
elif int(year_of_birth) >= 1961 and int(year_of_birth) < 1963:
    print ("John F. Kennedy was in office when you were born")
elif int(year_of_birth) >= 1963 and int(year_of_birth) < 1969:
    print ("Lyndon b. Johnson was in office when you were born")
elif int(year_of_birth) >= 1969 and int(year_of_birth) < 1974:
    print ("Richard Nixon was in office when you were born")
elif int(year_of_birth) >= 1974 and int(year_of_birth) < 1977:
    print ("Gerald Ford was in office when you were born")
elif int(year_of_birth) >= 1977 and int(year_of_birth) < 1981:
    print ("Jimmy Carter was in office when you were born")
elif int(year_of_birth) >= 1981 and int(year_of_birth) < 1989:
    print ("Ronald Reagan was in office when you were born")
elif int(year_of_birth) >= 1989 and int(year_of_birth) < 1993:
    print ("George Bush was in office when you were born")
elif int(year_of_birth) >= 1993 and int(year_of_birth) < 2001:
    print ("Bill Clinton was in office when you were born")
elif int(year_of_birth) >= 2001 and int(year_of_birth) < 2009:
    print ("George W. Bush was in office when you were born")
else:
    print ("Barack Obama was in office when you were born")
