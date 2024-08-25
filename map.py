dogs = [["chica", "aussie"], ["nico", "chihuahua"]]

names = map(
    lambda n: n[0],
    dogs
)

print(list(names))


"""
filter vs. map:

filter:
expects a filtering function that returns true or false.
it will filter results that are true, and will discard the ones that are false

also expects an iterable. each item of the iterable will be processed by the function

the filter object has to be converted to a list, otherwise you won't see the values

-------

map:
expects a function and an iterable.
each item of the iterable will be processed by the function.

the map object has to be converted to a list, otherwise you won't see the values


"""
