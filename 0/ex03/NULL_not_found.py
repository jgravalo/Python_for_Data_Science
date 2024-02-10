def NULL_not_found(object: any) -> int:
#your code here
	#print(f"{object}", ':', object, type(object)) if object == 0 else print("type not found")
	if object == 0:
		print(f"{object}", ':', object, type(object))
		return 0
	print("type not found")
	return 1
# no terminado
