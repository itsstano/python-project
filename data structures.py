#list data structures
myclassmate=["eric","joan","daniel","susan","purity"]
mynos=[4,9,20,3,1,50,-9]
myclassmate[0]="daniel"
mynos.sort()
myclassmate.append("christine")
myclassmate.insert(2,"michael")
for classmates in myclassmate:
    print(classmates)
myclassmate.pop(0)
print(myclassmate)
print(mynos)
#this is a tuple
countries=("Kenya","Uganda","Tanzania","Burundi")
print(countries[2])
for x in countries:
    print(x)
#sets data structures

cars={"Toyota","Nissan","Mercedes","Subaru","Rangerover"}
print(cars)
for y in cars:
    print(y)
#dictonary data structures
matunda={
    "price":50,
    "color":"Green",
    "name":"banana"
}
bei=matunda["price"]
matunda.update({"gender":"female"})
matunda.pop("price")
print(matunda)
print(bei)