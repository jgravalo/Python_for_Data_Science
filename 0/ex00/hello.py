ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"
#ft_tuple[1] = "Spain!"
del ft_tuple
ft_tuple = ("Hello", "Spain!")
ft_set.remove("tutu!")
ft_set.add("Barcelona!")
ft_dict["Hello"] = "42Barcelona!"
#

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)