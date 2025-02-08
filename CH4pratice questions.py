# first question is to create a dict that's it
pythondict = {
    "table" : ["a piece of furniture" , "it is house used material"],
    "cat" : "a small animal" ,
}
print(pythondict)

# question : for ecah subuject each one class . find how many cls need.
# for this answers is to create one set by this repated will be removed so by this we can find the len  mean how many.
#  are need we can find .

classset = {
    "pyhton" , "c++" , "py" , "c", "py" , "js" ,"js", "c++" , "java" , "java", "java" , "c"
}
print(len(classset))

# 3rd question i have to take 3 user inout marks enter and store in the dict .and create one emepty dict then add them
# answer  basic u can take input and use the dict.update () method to add in the empty set
dict = {}
sub1 = int(input("subject 1 : "))
dict.update({"fla" : sub1})
sub2 = int(input("subject 2 : "))
dict.update({"cn" : sub2})
sub3 = int(input("subject 3 : "))
dict.update({"DA" : sub3})
print(dict)