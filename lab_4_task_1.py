def my_func(a):
  s = 0
  for i in range (0, len(a),1) :
    s = s + a [i]
  return s/len(a)
s = [1, 3, 7]
print (my_func(s))

def my_func(a):
  s = 1
  for i in range ( 0, len(a),1) :
    s = s * a [i]
  return s
s = [1, 3, 7]
print (my_func(s))