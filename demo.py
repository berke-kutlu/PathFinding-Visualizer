class Foo(object):

     def __init__(self, score):
         self.score = score

     def __lt__(self, other):
         return self.score < other.score

l = [Foo(3), Foo(1), Foo(2)]
l.sort()
for a in l:
    print(a.score)