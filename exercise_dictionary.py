dog ={
    "Name":"Puppy",
    "Color":"White",
    "Breed":"German shepherd",
    "leg" :"Short",
    "Age":"6",

}
print(dog)
student={
    "first_name":"Lucy",
    "last_name":"Obahor",
    "Gender":"Female",
    "Age":"24",
    "Marital Status":"Single",
    "skills":["Cooking","Sleeping","Javascript","Python"],
    "Country":"Nigeria", 
    "City":"Abuja",
    "Address":{'street':'Space street',
        'zipcode':'02210'}
}
print(len(student))
values=student.values()
print(values)
student ["skills"] ="Facebook","React"
print(student)
keys=student.keys()
print(keys)
print(student.items())
student.pop("first_name")
print(student)
del student
print(student)
