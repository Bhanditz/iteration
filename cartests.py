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

