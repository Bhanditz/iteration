#!/usr/bin/env python
import sys

data = open("cars.csv", 'r')
lines = data.readlines()

car_ids = []
car_makes = []
car_models = []
car_years = []
car_colors = []
car_countries = []

for i in range(1, len(lines)):
    info = lines[i].rstrip().split(',') # [id, make, model, year, color, country]
    car_ids.append(info[0])
    car_makes.append(info[1])
    car_models.append(info[2])
    car_years.append(info[3])
    car_colors.append(info[4])
    car_countries.append(info[5])

def list_for_year(year):
    # print 'list_for_year running'
    for row in range(0, len(car_ids)):
        # print 'for loop working'
        # print car_years[row]
        # print year
        if int(car_years[row]) == year:
            # print "if statement succeeding"
            print car_years[row], car_makes[row], car_models[row]

def toyotas_since_2000():
    toyota_count = 0
    for row in range(0, len(car_ids)):
        if int(car_years[row]) > 2000 and car_makes[row] == "Toyota":
            print car_years[row], car_makes[row], car_models[row]
            toyota_count += 1
    print toyota_count

def most_popular_color():
    color_list = []
    for row in range(0, len(car_ids)):
        if str(car_colors[row]) not in colors:
            color_list.append(car_colors[row])

    print max(color_list)

print "Which problem would you like the solution for?"
request = str(input("> "))

if str(0) in request:
    list_for_year(2006)
elif str(1) in request:
    print "Which year would you like a list of cars from?"
    year_request = input("> ")
    list_for_year(year_request)
elif str(2) in request:
    toyotas_since_2000()
elif str(3) in request:
    most_popular_color()
else:
    print "Not sure what you meant by that. Try inputting an integer"

