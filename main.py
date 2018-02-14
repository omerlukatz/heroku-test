



def start():
	clear()
	start = input('Hello person. I am a computer. Would you like to register as a member of the secret society of awesomeness?   ')

	main = False
	while main == False:
		if start.lower() in ['yes', 'ya', 'yeah', 'sure', 'i guess', 'why not', 'why not?', 'ok', 'okay', 'yup', 'lets do it']:
			clear()
			register()
		else:
			print()
			print('That was not very nice of you!')


def register():


	
	valid_u = False
	while not valid_u:
		clear()
		user = input('Username:   ')
		if username(user):
			clear()
			valid_p = False
			while not valid_p:
				print('Username:   ', user)
				code = input('Password:    ')
				if password(code):
					if valid(user):
						database = open('users_database.txt', 'a')
						database.write('%s,%s\n' % (user, code))
						clear()
						redirect(user, code)
					else:
						clear()
						print('that information was already taken.')
						register()



					


def password(code):
	if len(code) < 8:
		clear()
		print('that is not a valid password. Must me more than 8 characters.')
		print()
		return False
	else:
		return True





def username(user):
	
	if len(user) < 8:
		clear()
		print('that is not a valid username. Must me more than 8 characters.')
		print()
		return False
	else:
		return True




def valid(user):
	#try:
	#	database = open('users_database.json', 'r')
	#	users = database.readlines()
	#	database.close()
	#	for line in users:
	#		line = line.split(',').strip()
	#		if line[0] == user:
	#			print('This username is already taken! pick another.')
	#			return False
	#		else:
	#			return True
	#except:
	#	users = []
	#	return True
	
	with open('users_database.txt','r') as f:
		lines = f.readlines()
		for line in lines:
			if user in line:
				return False
			else:
				return True


def redirect(user, code):
	stuff = False
	while not stuff:
		clear()
		print('Welcome to the home page')
		print()
		print()
		print()
		print('1. Logout')
		print('2. Edit')
		print('3. Search')
		print('4. Post')
		print('5. Delete')
		print()
		print('--------------------------------------------------------')
		print()
		pick = input('What would you like to do?   ')
		if (pick == '1') or (pick.lower() == 'logout'):
			logout()
		elif (pick == '2') or (pick.lower() == 'edit'):
			clear()
			edit(user, code)
		elif (pick == '3') or (pick.lower() == 'search'):
			search()
		elif (pick == '4') or (pick.lower() == 'post'):
			post(user, code)
		elif (pick == '5') or (pick.lower() == 'delete'):
			clear()
			stop = input('Are you sure you want to delete your account?   ')
			if stop.lower() in ['yes', 'ya', 'yeah', 'sure', 'i guess', 'why not', 'why not?', 'ok', 'okay', 'yup', 'lets do it']:
				clear()
				haha = input('Really?   ')
				if haha.lower() in ['yes', 'ya', 'yeah', 'sure', 'i guess', 'why not', 'why not?', 'ok', 'okay', 'yup', 'lets do it']:
					clear()
					last = input('For real???   ')
					if last.lower() in ['yes', 'ya', 'yeah', 'sure', 'i guess', 'why not', 'why not?', 'ok', 'okay', 'yup', 'lets do it']:
						delete(user, code)
					else:
						clear()
						redirect(user,code)
				else:
					clear()
					redirect(user,code)
			else:
				clear()
				redirect(user, code)
		else:
			clear()
			print('That wasnt an option!')
			stuff = False




def begin():
	clear()
	print('SECRET SOCIETY OF AWESOMENESS')
	print('--------------------------------------------------------')
	print()
	print()
	print('1. Login')
	print('2. Video')
	print('3. Create Account')
	print('--------------------------------------------------------')
	print()
	eh = input('What would you like to do?   ')
	if (eh == '1') or (eh.lower() == 'login'):
		clear()
		login()
	elif (eh == '2') or (eh.lower() == 'video'):
		clear()
		url = ['https://www.youtube.com/watch?v=-7akjeomUck&t=32s', 'https://www.youtube.com/watch?v=vTIIMJ9tUc8', 'https://www.youtube.com/watch?v=TIIWPACxHDU', 'https://www.youtube.com/watch?v=Uq734_nZ7Eo', 'https://www.youtube.com/watch?v=pDk5gaKQsnw', 'https://www.youtube.com/watch?v=grAOfOjONfY', 'https://www.youtube.com/watch?v=X1ahJsDNDTQ', 'https://www.youtube.com/watch?v=x3c0JgZ59QQ', 'https://www.youtube.com/watch?v=Ze6j-JdibK0', 'https://www.youtube.com/watch?v=IcwP26wK5KM', 'https://www.youtube.com/watch?v=JPZGxmRycV4', 'https://www.youtube.com/watch?v=PJVP0RTRlWE', 'https://www.youtube.com/watch?v=tdOflj-esBA', 'https://www.youtube.com/watch?v=Db_jd9ZaS6Y', 'https://www.youtube.com/watch?v=d1JA-nh0IfI', 'https://www.youtube.com/watch?v=6ZBqv-EdWOk']
		ran_url = random.choice(url) 
		webbrowser.open_new_tab(ran_url)
	elif (eh == '3') or (eh.lower() == 'create account'):
		clear()
		register()


def search():
	clear()
	searaching = input('Search user:   ')
	clear()
	print('Search user:   ' + searaching)
	print('--------------------------------------------------------')
	with open('users_database.txt','r') as f:
		lines = f.readlines()
		acc = 0
		for line in lines:
			line = line.split(',')
			username = line[0]
			if searaching in username:
				print('                     ' + username)
				print('--------------------------------------------------------')
			else:
				pass
		input()
		redirect(user, code)




def post(user,code):
	clear()
	print('Post')
	print('--------------------------------------------------------')
	print()
	print()
	print('1. Wall')
	print('2. My posts')
	print('3. Back')
	print('--------------------------------------------------------')
	print()
	eh = input('What would you like to do?   ')
	if (eh == '1') or (eh.lower() == 'wall'):
		clear()
		postwall(user,code)
	elif (eh == '2') or (eh.lower() == 'my posts'):
		clear()
		myposts(user,code)
	elif (eh == '3') or (eh == ''):
		clear()
		redirect(user,code)





def postwall(user,code):
	clear()
	print('Wall')
	print('--------------------------------------------------------')
	with open('user_post.txt','r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.split(',')
			username = line[0]
			text = line[1]
			print(username + ': ')
			print('     ' + text)
			print('--------------------------------------------------------')
	f.close()
	sure = input('would you like to post?   ')
	if sure.lower() in ['yes', 'ya', 'yeah', 'sure', 'i guess', 'why not', 'why not?', 'ok', 'okay', 'yup', 'lets do it']: 
		clear()
		mind = input('What\'s on your mind?   ')
		with open('user_post.txt','a') as f:
			f.write(user +',' + mind + '\n')
		f.close()
		print(username + ': ')
		print('     ' + mind)
		print('--------------------------------------------------------')
		post(user,code)
	else:
		post(user,code)




def myposts(user,code):
	clear()
	print('Wall')
	print('--------------------------------------------------------')
	with open('user_post.txt','r') as f:
		lines = f.readlines()
		acc = 0
		for line in lines:
			line = line.split(',')
			username = line[0]
			text = line[1]
			if username == user:
				acc += 1
				print(str(acc) + '. ' +username + ': ')
				print('     ' + text)
				print('--------------------------------------------------------')
			else:
				pass
	f.close()
	delete = input('would you like to delete a post?   ')
	if delete.lower() in ['yes', 'ya', 'yeah', 'sure', 'i guess', 'why not', 'why not?', 'ok', 'okay', 'yup', 'lets do it']: 
		which = input('Copy and paste the one you would like to delete here:   ')
		with open('user_post.txt','r') as f:
			lines = f.readlines()
			acc = ''
			for line in lines:
				line = line.split(',')
				text = line[1]
				print(text + '***')
				if text.lower() == which.lower() + '\n':
					pass
				else:
					acc += line[0] + ',' + text
		with open('user_post.txt','w') as f:
			f.write(acc)
		f.close()
	else:
		post(user,code)






def login():
	boi = False
	while not boi:
		user = input('Username:   ')
		clear()
		print('Username:  ', user)
		code = input('Password:   ')
		with open('users_database.txt','r') as f:
			lines = f.readlines()
			for line in lines:
				print()
				if line.strip() == user + ',' + code:
					clear()
					redirect(user, code)
				else:
					clear()
					print('Try again.')
					boi = False





def edit(user, code):
	print('EDIT')
	print('--------------------------------------------------------')
	print()
	print('1. Username')
	print('2. Password')
	print()
	print('--------------------------------------------------------')
	print()
	eh = input('What would you like to edit?   ')
	if eh in ['1', 'username', 'Username']:
		clear()
		new_u = input('What would you like to change your username to?   ')
		if valid(new_u) and username(new_u):
			with open('users_database.txt','r') as f:
				lines = f.readlines()
				acc = ''
				for line in lines:
					if line.strip() == user + ',' + code:
						print('oofer_gang')
						acc += new_u + ',' + code + '\n'
					else:
						acc += line
			f.close()
			with open('users_database.txt','w') as f:
				f.write(acc)
			f.close()
			clear()
			redirect(user, code)
		else:
			clear()
			print('The username you picked was either taken or to short.')
			print('--------------------------------------------------------')
			edit(user, code)
	elif eh in ['2', 'password', 'Password']:
		clear()
		new_p = input('What would you like to change your password to?   ')
		if valid(new_u) and username(new_u):
			with open('users_database.txt','r') as f:
				lines = f.readlines()
				acc = ''
				for line in lines:
					if line.strip() == user + ',' + code:
						acc += user + ',' + new_p + '\n'
					else:
						acc += line
			f.close()
			with open('users_database.txt','w') as f:
				f.write(acc)
			f.close()

			clear()
			redirect(user, code)
		else:
			clear()
			print('The password you picked was either taken or to short.')
			print('--------------------------------------------------------')
			edit(user, code)




def delete(user, code):
	with open('users_database.txt','r') as f:
		lines = f.readlines()
		acc = ''
		for line in lines:
			if line.strip() == user + ',' + code:
				pass
			else:
				acc += line
	
	with open('users_database.txt','w') as f:
		f.write(acc)



def logout():
	clear()
	yaynay = input('Are you sure you want to log out?   ')
	stuff = False
	while not stuff:
		if yaynay.lower() in ['yes', 'ya', 'yeah', 'sure', 'i guess', 'why not', 'why not?', 'ok', 'okay', 'yup', 'lets do it', 'yea']:
			begin()
		else:
			redirect(user, code)
			



def clear():
	os.system('clear')




# start()
begin()





