
from uuid import uuid4
from datetime import datetime


class BaseModel():

	def __init__(self):
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
		format_str = "[{}] ({}) {}"
		return format_str.format(self.__class__.__name__,
			self.id, self.__dict__)

	def __repr__(self):
		return (self.__str__())

	def save(self):
		self.updated_at = datetime.now()

	def to_dict(self):
		dic = {}
		dic["__class__"] = self.__class__.__name__

		for key, val in self.__dict__.items():
			if key == 'updated_at':
				dic[key] = val.isoformat()
			elif key == 'created_at':
				dic[key] = val.isoformat()
			else:
				dic[key] = val
		return dic

	@classmethod
	def to_string(cls):
		print("This is the to string")


base_model = BaseModel(); # create items
print("--------------initiated the classs-------------")
print(base_model)
print("")

print("-------- updating the model ------------------")
base_model.save()
print(base_model)

print()
print("---------- converting to new dict -----------")
print(base_model.to_dict())
print()

