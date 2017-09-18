class Contact():
	def __init__(self, name, phone, email, website, birthday, linkedin, picture):
		self.name=name
		self.phone=phone
		self.email=email
		self.website=website
		self.birthday=birthday
		self.linkedin=linkedin
		self.picture=picture

	def set_contact(self, name, phone, email, website, birthday, linkedin, picture):
		self.name=name
		self.phone=phone
		self.email=email
		self.website=website
		self.birthday=birthday
		self.linkedin=linkedin
		self.picture=picture

	def get_contact(self):
		print(self.name, self.phone, self.email, self.website, self.birthday, self.linkedin ,self.picture)




new_name=input("What is your name?")
new_phone=input("Phone Number?")
new_email=input("What is your email?")
new_website=input("The name of your website?")
dob=input("Your date of birth?")
linkedin=input("LinkedIn Name?")
pictureid=input("Picture Id")

new_contact=Contact(new_name, new_phone, new_email, new_website, dob, linkedin, pictureid)

new_contact.set_contact(new_name, new_phone, new_email, new_website, dob, linkedin, pictureid)

new_contact.get_contact()
