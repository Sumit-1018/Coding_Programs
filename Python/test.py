class OurException(Exception):
	def __init__(self,message):
		self.message=message
class UsingUserException:
    try:
		a=int(input("a: "))
		b=int(input("b: "))
		if b==0:
			print("user defined exception: b should be greater than 0")
			raise OurException
		else:
			c=a+b
			d=a/b
			print("division operation successful with result:",d)
    except OurException as err:
        print("user defined exception:",err.message)