views.py:
	
	handle_uploaded_file(file,filename): Takes in file and name of the file, then loops through chunks of the file to write it onto the server.

	PostRequestMethod(request):	Handles post requests, takes in the request. Tries to upload an image but if that is not contained in the request it tries to update 									information in the database using the information in the request.

	getStudents(students): Takes in student objects from the database and transforms them into a json objects to send to the front-end. Returns the json object.

	viewStudent(request): Takes in a request object, handles post requests (if applicable), selects students from the database if they are listed as students then calls the function to create json object and sends it to the viewStudents front-end

	viewGraduate(request): Takes in a request object, handles post requests (if applicable), selects students from the database if they are listed as grads then 	calls the function to create json object and sends it to the viewStudents front-end

	ViewDropout(request): Takes in a request object, handles post requests (if applicable), selects students from the database if they are listed as dropouts then calls the function to create json object and sends it to the viewStudents front-end




viewStudents.html, viewGraduates.html, viewDropouts.html:

	getCookie(name): Takes in the name of the item it searches for, returns the cookie that relates to this name. In this case was used for the csrftoken.

	onSelectionChnaged(): Finds which row is selected and updates the student panel to reflect the selected row.

	loadFile(): Takes the image loaded to the file selector and sets it as the image in the student panel.

	deleteSelected(): Finds the selected row, confirms the user wants to delete and if yes the selected student is removed from the database and the grid.

	imageUpload(): Takes the image loaded to the file selector and sends a post request to upload the image and sets the image_path in the database.

	fileUpload(): Takes the file loaded to the file selector and sends a post request to upload the file and sets the file_path in the database.

	sortData(sortModel, data): Takes in the grid data and a sort model and allows for the sorting of a column in the grid.

	filterData(filterModel, data): Takes in the grid data and a filter model and allows for filtering of select columns in the grid.



addStudent.html (only did front end for add student):
	
	loadFile(): Takes the image loaded to the file selector and sets it as the image in main image component on the screen.




Software required to run the program:
	django
	django rest framework
	python
	
To run:
	go to the ICT_Admin folder and in the terminal type: python manage.py runserver

User guide will be on the website.
