class MusicSchool:
	students = {
		"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
		"Talina": [28, "555-765-452", ["Cello"]],
		"Eric":   [12, "583-356-223", ["Singing"]]
	}

	def __init__(self, working_hours, revenue):
		self.working_hours = working_hours
		self.revenue = revenue

	def print_students_data(self):
		for key in MusicSchool.students:
			self.print_student(key)

	def print_student(self,student_name):
		value = MusicSchool.students[student_name]
		print("Student: {} who is {} years old and is taking {}".format(student_name, value[0], value[2]))

	def add_student(self,name,data):
		MusicSchool.students[name] = data

	def open_file(self,file_name):
		try:
			file = open(file_name, "x")
		except:
			print("File already exists")
		file = open(file_name, "a+")
		return file

	def save_to_file(self,file_name):
		file = self.open_file(file_name)
		for key in MusicSchool.students:
			data = MusicSchool.students[key]
			file.write("{}:{},{},{}\n".format(key,data[0],data[1],data[2]))
		file.close()
		print("Data written to file")

	def erase_file(self,file_name):
		file = self.open_file(file_name)
		file.truncate(0)
		file.close()
		print("File data erased")

school = MusicSchool(8,15000)
data = [25,"123456",["Guitar","Vocals"]]
school.add_student("Daniel",data)
school.print_students_data()
school.save_to_file("data.txt")