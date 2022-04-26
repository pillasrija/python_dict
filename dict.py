friends={'tom':'111-222-333',
         'jerry':'666-33-111'
         }
print(friends)
print(friends['tom'])
friends['bob'] = '888-999-666'
print(friends)
friends['bob'] = '888-999-777'
print(friends)
del friends['bob']
print(friends)

# looping items in the dict
values = {'a':'100',
          'b':'200',
          'c':'300',
          'd':'400'
          }
for k in values:
    print(k,":",values[k])

# equality tests in dict ( == and != operators)
d1={"milk":41,"bob":35}
d2={"bob":20,"milk":41}
print(d1==d2)
print(d1!=d2)



