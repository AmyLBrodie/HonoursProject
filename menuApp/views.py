from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render_to_response

from menuApp.models import Student, StudentInfo, ContactDetails, EmploymentInfo, EmploymentHistory, WeekendPlacement

# Create your views here.

# Uploads the file to the server
def handle_uploaded_file(file, filename):
	with open('static/' + filename, 'wb+') as destination:
		for chunk in file.chunks():
			destination.write(chunk)

# Deals with incoming post requests
def postRequestMethod(request):
	if request.method == 'POST':
		# file uploads
		try:
			handle_uploaded_file(request.FILES['image'], str(request.FILES['image']))
		# database edits
		except:
			s_id = request.POST.get('s_id')
			column = request.POST.get('column')
			newValue = request.POST.get('newValue')
			oldValue = request.POST.get('oldValue')

			if (column == "name"):
				student = Student.objects.get(student_id = s_id)
				student.name = newValue
				student.save()
			elif (column == "contact"):
				newArray = newValue.split(",")
				try:
					student = ContactDetails.objects.filter(student=Student.objects.get(student_id=s_id))
					for s in student:
						s.delete()

					s = Student.objects.get(student_id=s_id)
					for i in newArray:
						student = ContactDetails(student=Student.objects.get(student_id=s_id),contact=i)
						student.save()
				except:
					s = Student.objects.get(student_id=s_id)
					student = ContactDetails(student=Student.objects.get(student_id=s_id),contact=newValue)
					student.save()

			elif (column == "idNumber"):
				student = Student.objects.get(student_id=s_id)
				student.id_no = newValue
				student.save()
			elif (column == "classNumber"):
				try:
					student = StudentInfo.objects.get(student=Student.objects.get(student_id=s_id))
					student.class_no = newValue
					student.save()
				except:
					s = Student.objects.get(student_id=s_id)
					student = StudentInfo(student=Student.objects.get(student_id=s_id),class_no=newValue,grad_or_student='student',dropout='0')
					student.save()
			elif (column == "year"):
				try:
					student = StudentInfo.objects.get(student=Student.objects.get(student_id=s_id))
					student.year = newValue
					student.save()
				except:
					s = Student.objects.get(student_id=s_id)
					student = StudentInfo(student=Student.objects.get(student_id=s_id),year=newValue,grad_or_student='student',dropout='0')
					student.save()
			elif (column == "weekend"):
				newArray = newValue.split(",")
				try:
					student = WeekendPlacement.objects.filter(student=Student.objects.get(student_id=s_id))
					for s in student:
						s.delete()

					s = Student.objects.get(student_id=s_id)
					for i in newArray:
						student = WeekendPlacement(student=Student.objects.get(student_id=s_id),placement=i)
						student.save()
				except:
					s = Student.objects.get(student_id=s_id)
					student = WeekendPlacement(student=Student.objects.get(student_id=s_id),placement=newValue)
					student.save()
			elif (column == "internship"):
				try:
					student = EmploymentInfo.objects.get(student=Student.objects.get(student_id=s_id))
					student.internship = newValue
					student.save()
				except:
					s = Student.objects.get(student_id=s_id)
					student = EmploymentInfo(student=Student.objects.get(student_id=s_id),internship=newValue)
					student.save()
			elif (column == "current"):
					try:
						student = EmploymentInfo.objects.get(student=Student.objects.get(student_id=s_id))
						student.current_employment = newValue
						student.save()
						if oldValue != "":
							student1 = EmploymentHistory(student=Student.objects.get(student_id=s_id),employment=oldValue)
							student1.save()
					except:
						s = Student.objects.get(student_id=s_id)
						student = EmploymentInfo(student=Student.objects.get(student_id=s_id),current_employment=newValue)
						student.save()
			elif (column == "history"):
				newArray = newValue.split(",")
				try:
					student = EmploymentHistory.objects.filter(student=Student.objects.get(student_id=s_id))
					for s in student:
						s.delete()

					s = Student.objects.get(student_id=s_id)
					for i in newArray:
						student = EmploymentHistory(student=Student.objects.get(student_id=s_id),employment=i)
						student.save()
				except:
					s = Student.objects.get(student_id=s_id)
					student = EmploymentHistory(student=Student.objects.get(student_id=s_id),employment=newValue)
					student.save()
			elif (column == "status"):
				try:
					student = StudentInfo.objects.get(student=Student.objects.get(student_id=s_id))
					student.grad_or_student = newValue
					if(str(newValue).lower() == "dropout"):
						student.dropout = "1"
					else:
						student.dropout = "0"
					student.save()
				except:
					s = Student.objects.get(student_id=s_id)
					student = StudentInfo(student=Student.objects.get(student_id=s_id),grad_or_student=newValue,dropout='0')
					student.save()
			elif (column == "dropout"):
				try:
					student = StudentInfo.objects.get(student=Student.objects.get(student_id=s_id))
					student.dropout = newValue
					if (str(newValue) == "1"):
						student.grad_or_student = "dropout"
					student.save()
				except:
					s = Student.objects.get(student_id=s_id)
					student = StudentInfo(student=Student.objects.get(student_id=s_id),dropout=newValue)
					student.save()
			elif (column == "deceased"):
				student = Student.objects.get(student_id=s_id)
				student.deceased = newValue
				student.save()
			elif (column == "appActive"):
				student = Student.objects.filter(student_id=s_id)
			elif (column == "image_path"):
				print(newValue)
				student = Student.objects.get(student_id=s_id)
				student.image_path = newValue
				student.save()
			elif (column == "file_path"):
				print(newValue)
				student = Student.objects.get(student_id=s_id)
				student.file_path = newValue
				student.save()
			elif (column == "delete"):
				student = Student.objects.get(student_id=s_id)
				student.delete()

# pull student record from the database and create json string
def getStudents(students):
	rows = ''
	for s in students:
		rows += '{"s_id":"' + str(s.student.student_id) + '",'
		theStudent = Student.objects.get(student_id=s.student.student_id)
		if (theStudent.name is None ):
			rows += '"name":"",'
		else:
			rows += '"name":"' +theStudent.name + '",'

		if (theStudent.id_no is None ):
			rows += '"idNumber":"",'
		else:
			rows += '"idNumber":"' + theStudent.id_no + '",'
		if (theStudent.image_path is None ):
			rows += '"imagePath":"",'
		else:
			rows += '"imagePath":"' + theStudent.image_path + '",'
		if (theStudent.file_path is None ):
			rows += '"filePath":"",'
		else:
			rows += '"filePath":"' + theStudent.file_path + '",'

		rows += '"deceased":"' + str(theStudent.deceased) + '",'

		history = EmploymentHistory.objects.filter(student=s.student)
		temp = ''
		for h in history:
			h = h.employment
			h = h.replace("'","’")
			h = h.replace('"','')
			h = " " + h
			temp += '"' + h + '", '
		temp = temp [:-1]
		temp = temp [:-1]
		if (len(temp) == 0):
			rows += '"history":"",'
		else:
			temp = '[' + temp + ']'
			rows += '"history":'+ temp +','

		try:
			current = str(EmploymentInfo.objects.get(student=s.student).current_employment)
			current = current.replace("'","’")
			rows += '"current":"'+ current +'",'
		except:
			rows += '"current":"",'

		try:
			placement = str(EmploymentInfo.objects.get(student=s.student).internship)
			placement = placement.replace("'","’")
			rows += '"internship":"'+ placement +'",'
		except:
			rows += '"internship":"",'

		placement = WeekendPlacement.objects.filter(student=s.student)
		temp = ''
		for w in placement:
			w = w.placement
			w = w.replace("'","’")
			w = " " + w
			temp += '"' + w + '", '
		temp = temp [:-1]
		temp = temp [:-1]

		if (len(temp) == 0):
			rows += '"weekend":"",'
		else:
			temp = '[' + temp + ']'
			rows += '"weekend":'+ temp +','

		try:
			rows += '"classNumber":"'+str(StudentInfo.objects.get(student=s.student).class_no)+'",'
		except:
			rows += '"classNumber":"",'

		try:
			rows += '"year":"'+str(StudentInfo.objects.get(student=s.student).year)+'",'
		except:
			rows += '"year":"",'

		contact = ContactDetails.objects.filter(student=s.student)
		temp = ''
		for c in contact:
			c = c.contact
			c = " " + c
			temp += '"' + c + '", '
		temp = temp [:-1]
		temp = temp [:-1]

		if (len(temp) == 0):
			rows += '"contact":"",'
		else:
			temp = '[' + temp + ']'
			rows += '"contact":'+ temp +','

		try:
			rows += '"status":"'+str(StudentInfo.objects.get(student=s.student).grad_or_student)+'",'
		except:
			rows += '"status":"",'

		try:
			rows += '"dropout":"'+str(StudentInfo.objects.get(student=s.student).dropout)+'"'
		except:
			rows += '"dropout":""'

		rows += '},'

	rows = rows[:-1]
	return rows

# view students view, pulls all records from the database that are current students and sends it to the front-end
def viewStudent(request):
	postRequestMethod(request)

	students = StudentInfo.objects.filter(grad_or_student="student")

	rows = getStudents(students)

	return render(request, "viewStudents.html", {'sInfo':rows})

# view graduates view, pulls all records from the database that are graduates and sends it to the front-end
def viewGraduate(request):
	postRequestMethod(request)

	students = StudentInfo.objects.filter(grad_or_student="grad")

	rows = getStudents(students)

	return render(request, "viewGraduates.html", {'sInfo':rows})

# view dropouts view, pulls all records from the database that are dropouts and sends it to the front-end
def viewDropout(request):
	postRequestMethod(request)

	students = StudentInfo.objects.filter(grad_or_student="dropout")

	rows = getStudents(students)

	return render(request, "viewDropouts.html", {'sInfo':rows})
