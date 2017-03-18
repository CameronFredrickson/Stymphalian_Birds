import subprocess
import sys
import io
import shutil

def create_project(project_name):
	try:
		retcode = subprocess.call("mkdir " + project_name, shell=True)
		if retcode < 0:
			print("Failed to create project directory. return code: %d", retcode)
		else:
			print "Created project directory."
	except OSError as e:
		print("Execution failed in create_project: ", e)


def create_subdirectories(project_name):
	try:
		retcode = subprocess.call("mkdir " + 
			project_name + "/bin " + project_name + "/srcs " + 
			project_name + "/build " + project_name + "/tests ", shell=True)
		if retcode < 0:
			print("Failed to create project subdirectories. return code: %d", retcode)
		else:
			print "Created project subdirectories."
	except OSError as e:
		print("Execution failed in create_subdirectories: ", e)


def create_gitignore(project_name):
	try:
	#	retcode = subprocess.call("echo # OS generated files #"
	#		"\n######################\n.DS_Store\n._.DS_Store\n"
	#		"# Compiled source #\n###################\n"
	#		"a.out\n*.o"
	#		"# Directories #\n###################\n"
	#		"bin/"
	#		"> .gitignore", shell=True)
		retcode = 0
		with io.FileIO(".gitignore", "w") as file:
			file.write("bin/")
		shutil.move('.gitignore', project_name)
		if retcode < 0:
			print("Failed to create .gitignore file. return code: %d", retcode)
		else:
			print "Created project .gitignore file."		
	except OSError as e:
		print("Execution failed in create_gitignore: ", e)


def main():
	print "************************************************************************************"
	print "What is the project name?"
	project_name = raw_input()
	create_project(project_name) # use raw_input() as the argument
	print "What language will you be using?"
	language = raw_input()
	if language == 'c' or language == 'C' or language == 'C++':
		# create_c_environment()
		pass
	create_gitignore(project_name)

if __name__ == '__main__':
	main()
