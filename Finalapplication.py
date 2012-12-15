import sys
import tkinter as obj
from getpass import getpass

# A login.txt file will be created which will store the username and password of users.
# Another file named with user name will be created that will store the contact details of the user.
# A third file will be message.txt file that will store the messages along with sender ad recipient name. 



if __name__=='__main__':
	Name_string = raw_input("Enter the name\n")  #Getting user-name
	Pass_string = getpass('Enter your password: ') #Getting password
	choice = raw_input("Enter the toolkit\n")  # Enter any random value
	
	
	name_field1 = ""
	phoneno_field1 = ""
	rbgender1 = ""
	spin_day1 = 0
	drop_month1 = ""
	spin_year1 = 0
	byname_field1 = ""
	byphoneno_field1 = ""
	send_name_field1 = ""
	send_message_area1 = ""

	def OnClickClear():
		messages_area.Clear_area()

#Function will write the contact informations like Name, phone No., gender, date of birth in the file corresponding to each user
	def OnClickSave():	
		global Name_string
		global name_field
		global phoneno_field
		global rb_gender	
		global spin_day
		global drop_month
		global spin_year							
		name_field1 = name_field.Get_text()
		name_field.Clear_field()	
		phoneno_field1 = phoneno_field.Get_text() 
		phoneno_field.Clear_field()
		rbgender1 = rbgender.Get_selected()
		print rbgender1
		spin_day1 = spin_day.Get_value()
		print spin_day1
		drop_month1 = drop_month.Get_value()
		spin_year1 = spin_year.Get_value()
		path = Name_string + ".txt"
		Contact_file2 = open(path, 'a+')
		Contact_file2.write("1" + "\n")
		Contact_file2.write(name_field1 + "\n")
		Contact_file2.write(phoneno_field1 + "\n")
		Contact_file2.write(rbgender1 + "\n")
		Contact_file2.write(str(spin_day1) + "/" + str(drop_month1).strip('[]') + "/" +  str(spin_year1) + "\n")
		Contact_file2.write("1" + "\n")
		Contact_file2.close()
		

# Function to search the contact details either by name or by phone number from user contact list or file.
	def OnClickSearch():
		global Name_string
		global byname_field
		global byphone_field
		global check_byname
		global check_byphone
		global results_area
		flag1 = 0
		flag2 = 0
		if(check_byname.Is_checked()):
			byname_field1 = byname_field.Get_text() 
			flag1 = 1
			
		Search_path = Name_string + ".txt"
		Search_file = open(Search_path, 'r')
		results_area.Clear_area()
		results_area.Append_text(byname_field1)
		if(flag1 == 1):
			tag1 = 0
			tag2 = 0
			tag3 = 0
			tag4 = 0
			for line in Search_file:
				
				if(tag2 == 1):
					
					if(line == "1"+"\n" or line == "1"):
						tag1 = 0
						tag2 = 0
					else:
						print line
						results_area.Append_text(line)
				elif(tag3 == 0 and (line == "1"+"\n" or line == "1")):
					
					tag1 = 1
				elif(tag3 == 1 and (line == "1"+"\n" or line == "1")):
					
					tag3 =0
				else:
					if(tag1 == 1 and (line == byname_field1 + "\n" or line == byname_field1)):
						print line
						tag2 = 1
					else:
						tag1 = 0
						tag2 = 0
						tag3 = 1
		

# User can Send message to the other user in his contact list. Message will be stored in a file with sender and recepient name.
	def OnClickSend():
		global send_name_field
		global send_message_area
		send_name_field1 = send_name_field.Get_text()
		send_name_field.Clear_field()
		send_message_area1 = send_message_area.Get_text()
		print send_message_area1,"meaasge"
		send_message_area.Clear_area()
		#write it in the messaged.txt file
		Message_file2 = open('messages.txt', 'a+r')
		Message_file2.write("1" + "\n")
		Message_file2.write(send_name_field1 + "\n")
		global Name_string
		Message_file2.write(Name_string + "\n")
		Message_file2.write(send_message_area1 + "\n")
		Message_file2.write("1"+ "\n")
		Message_file2.close()

	

#Checking the validity of Username ad Password from fike LogIn.txt
	def Check1():
		
		i = 0
		j = 0
		tag = 0
		res = 0
		count = 0
		global Name_string
		global Pass_string
		Pass_file = open('LogIn.txt', 'a+r')
		#print Pass_file
		#Pass_file.readlines()
		for line in Pass_file:
			print line
			if(count%2 == 0 and line == Name_string + "\n" or line == Name_string and j == 0):
				
				j = 1
				tag = 1
			else:
				if(j == 1):
					j = 0
					if(line == Pass_string + "\n" or line == Pass_string):
						res = 1	
						
					else:
						break
					
		if(res == 1):
			Check2()
		elif(res == 0 and tag == 0):
			
			Pass_file.write(Name_string + "\n")
			Pass_file.write(Pass_string + "\n")
			Check2()
		elif(res == 0 and tag == 1):
			print "Password Incorrect - Try Again"
			sys.exit("Password Incorrect")
	

# Getting Message from the file message.txt

	def Check2():
		#------------------------------------------------------------------------------------------------
		global frame
		#------------------------------------------------------------------------------------------------
		Message_file = open('messages.txt', 'a+r')
		tag1 = 0
		tag2 = 0
		tag3 = 0
		global Name_string
		global message_area
	
		print Name_string
		for line in Message_file:
			
			if(tag2 == 1):
				
				if(line == "1"+"\n" or line == "1"):
					tag1 = 0
					tag2 = 0
				else:
					print line
					messages_area.Append_text(line)
			elif(tag3 == 0 and (line == "1"+"\n" or line == "1")):
				
				tag1 = 1
			elif(tag3 == 1 and (line == "1"+"\n" or line == "1")):
				
				tag3 =0
			else:
				if(tag1 == 1 and (line == Name_string + "\n" or line == Name_string)):
					print line
					tag2 = 1
				else:
					tag1 = 0
					tag2 = 0
					tag3 = 1
				#Append the text of the text area with the text present in messages file where the name agrees 
		
		window.Display()    #Display the window
		Message_file.close()
	
	window = obj.Dashboard('Application', 1000, 670)	

	a_contacts = obj.Static_text(25, 25, text = "Add Contacts ---> ")			# Creating static text1
	window.Add(a_contacts)
	name = obj.Static_text(20, 65, text = "Name")
	window.Add(name)

	phoneno = obj.Static_text(20, 105, text = "Phone No")
	window.Add(phoneno)

	gender = obj.Static_text( 25, 150, text = "Gender")
	window.Add(gender)

	dob = obj.Static_text(-10, 195, text = "Date of Birth")
	window.Add(dob)

	name_field = obj.Text_field( 130, 60, length = 270)
	window.Add(name_field)
	
	phoneno_field = obj.Text_field(130, 100, length = 270)
	window.Add(phoneno_field)

	rbgender = obj.Radio_button("Male",130, 150)					# Creating a Radio Button Set1			
	rbgender.Add_radio_button("Female", 210, 150)
	window.Add(rbgender)

	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']			 # List of entries in combo-box
	drop_month = obj.Drop_list(110, 190, "January", months, 125, 25)	# Creating a Combo box
	window.Add(drop_month)

	spin_day = obj.Spin_list(235, 190, 50, 25, 1, 31)
	window.Add(spin_day)

	spin_year = obj.Spin_list(320, 190, 75, 25,1950,2012)
	window.Add(spin_year)

	save_btn = obj.Create_button(170, 250, "Save", 85, 25)						# Creating Submit Button
	save_btn.Click_listener(OnClickSave)
	window.Add(save_btn)								# Adding it to frame1

	messages = obj.Static_text(25, 300, text = "Messages Recieved --->")
	window.Add(messages)

	messages_area = obj.Text_area(25, 330, 375, 250)
	window.Add(messages_area)

	clear_btn = obj.Create_button(170, 600, "Clear", 85, 25)						# Creating Submit Button
	clear_btn.Click_listener(OnClickClear)
	window.Add(clear_btn)						# Adding it to frame1


	s_contacts = obj.Static_text(500, 25, text = "Search Contacts ---> ")	# Creating static text1
	window.Add(s_contacts)

	byname = obj.Static_text(480, 65, text = "By Name")
	window.Add(byname)
	
	select = obj.Static_text(890, 25, text = "Select")
	window.Add(select)

	byname_field = obj.Text_field( 605, 60)
	window.Add(byname_field)

	check_byname = obj.Check_box(900, 60, "", 20, 20)		# Adding entries
	window.Add(check_byname)				# Adding it to frame1		
		

	search_btn = obj.Create_button(690, 160, "Search", 85, 25)     # Creating Submit Button
	search_btn.Click_listener(OnClickSearch)
	window.Add(search_btn)				# Adding it to frame1

	results = obj.Static_text(500, 200, text = "Results --->")
	window.Add(results)

	results_area = obj.Text_area(500, 230, 450, 125)
	window.Add(results_area)

	message = obj.Static_text(500, 370, text = "Send Message --->")
	window.Add(message)

	send_name = obj.Static_text(500, 410, text = "Name")
	window.Add(send_name)

	send_message = obj.Static_text(500, 450, text = "Message")
	window.Add(send_message)

	send_name_field = obj.Text_field( 605, 405, length = 270)
	window.Add(send_name_field)

	send_message_area = obj.Text_area( 605, 445, 270, 140)
	window.Add(send_message_area)

	send_btn = obj.Create_button(690, 600, "Send", 85, 25)		# Creating Submit Button
	send_btn.Click_listener(OnClickSend)
	window.Add(send_btn)					# Adding it to frame1
	
	Check1()	


########################################################################################################
