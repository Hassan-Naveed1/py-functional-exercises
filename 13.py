#13.Convert a list of radii into circle areas using map().
list = [1,2,3,4,5,6]
circle_area = map(lambda x: (x*x) * 3.14159, list)
print(tuple(circle_area))