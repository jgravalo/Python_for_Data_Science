def all_thing_is_obj(object: any) -> int:
#your code here
	if type(object) == str:
		print(object, "is in the kitchen", ':', type(object))
	elif type(object) == int or type(object) == float or type(object) == complex:
		print("type not found")
	else:
		print(type(object).__name__, ':', type(object))
	return 42