jee={"a","b","c","d","e"}
cet={"c","d","e","h"}
neet={"1","b","c","z"}
print("The number of students applying for jee is:",len(jee))
print("The number of students applying for cet is:",len(cet))
print("The number of students applying for neet is:",len(neet))
print("The names of students applying for jee is:",jee)
print("The names of students applying for cet is:",cet)
print("The names of students applying for neet is:",neet)
print("The names of students applying for jee as well as neet is:",jee.intersection(neet))
print("The names of students applying for jee as well as cet is:",jee.intersection(cet))
print("The names of students applying for neet as well as cet is:",neet.intersection(cet))
print("The names of students applying for jee only:",jee.difference(neet,cet))
print("The names of students applying for all three exams:",jee.intersection(neet,cet))
print("The names of students applying for exams:",jee.union(neet,cet))
print("The names of students applying for jee or neet not both:",jee.symmetric_difference(neet))
