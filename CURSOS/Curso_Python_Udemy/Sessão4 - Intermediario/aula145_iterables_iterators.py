#  Generator expression, Iterables e Iterators em python
iterables = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterables) # tem __iter__e__next__
print(next(iterator))
print(next(iterator))
print(next(iterator))