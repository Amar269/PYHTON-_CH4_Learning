# dict can run all types of data and can be modified the data
dict = {
    "name" : "amarnath " ,
    "cgpa" : 8.4,
    "subject" : "cloud computing",
    "sub_list": [99 , 89 , 91 , 88 , 92 , 94],
    "sub_tuple":("hai " , 78 ,  " testing the "),
    "sub_boolean" : True,
    7 : " 7 thala for a resaon " ,
}
print(type(dict))
print((dict))
dict["surname"] = "Kolla's",
print((dict))
print(dict["name"])
print(dict["subject"])
print(dict["sub_list"])

#null nothing can be print in dict
null_dict = {}
print(null_dict)

# NESTED DICT
students = {
    "first name = " : "AMAR_RAMA",
    "subjects_lists_4" : {
        "fla" : 96,
        "CN" : 95,
        "OP_E ": 93,
        "PR _ E" : 94 ,

    },
    "gobal_certified" : "AWS-certified",
}
print([students["subjects_lists_4"]["fla"]])

#DICT Methods
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("cgpa"))
dict.update({"city" : "vijayawada"})
print(dict)


# for sets concept refer the notes .
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))