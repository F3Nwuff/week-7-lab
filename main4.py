from main3 import array
ar = array(["zero","one","two","three","four"])

print(ar.get(0))
ar.append("five")
ar.pop()
ar.extend(["five","six","seven"])
ar.insert(8,"eight")
ar.index("zero")
print(ar.length())