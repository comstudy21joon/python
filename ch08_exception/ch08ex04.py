class UserDefinitionError(Exception):
	pass

try:
	raise UserDefinitionError("User definition error!")
except UserDefinitionError as e:
	print(e)
