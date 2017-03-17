import subprocess
import sys

def create_project(project_name):
	try:
		retcode = subprocess.call("mkdir " + project_name, shell=True)
		if retcode < 0:
			print("Failed to create project directory. return code: %d", retcode)
		else:
			print "Created project directory."
	except OSError as e:
		print("Execution failed: ", e)

def create_subdirectories(project_name):
	try:
		retcode = subprocess.call("mkdir " + 
			project_name + "/bin " + project_name + "/srcs " + 
			project_name + "/build " + project_name + "/tests ", shell=True)
		if retcode < 0:
			print("Failed to create project subdirectories. return code: %d", retcode)
		else:
			print "Created project subdirectories..."
	except OSError as e:
		print("Execution failed: ", e)


def create_gitignore():
	try:
		retcode = subprocess.call("echo ")
	except OSError as e:
		print("Execution failed: ", e)


def main():
	print "************************************************************************************"
	print "What is the project name?"
	project_name = raw_inpfut()
	create_directories(project_name) # use raw_input() as the argument
	print "What language will you be using?"
	language = raw_input()
	if language == 'c' or language == 'C' or language == 'C++':
		# create_c_environment()
		pass
	create_gitignore()

if __name__ == '__main__':
	main()
