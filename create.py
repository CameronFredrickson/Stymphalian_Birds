import subprocess
import sys
import io
import shutil


def create_project(project_name):
	"""Creates project directory."""
	try:
		retcode = subprocess.call("mkdir " + project_name, shell=True)
		if retcode < 0:
			print("Failed to create project directory. return code: %d", retcode)
		else:
			print "Created project directory."
	except OSError as e:
		print("Execution failed in create_project: ", e)


def create_subdirectories(project_name):
	"""Creates srcs, srcs/includes, bin, test, and build directories 
	in the project directory.
	"""
	try:
		retcode = subprocess.call("mkdir " + 
			project_name + "/bin " + project_name + "/srcs " + 
			project_name + "/build " + project_name + "/tests " +
			project_name + "/srcs/includes", shell=True)
		if retcode < 0:
			print("Failed to create project subdirectories. return code: %d", retcode)
		else:
			print "Created project subdirectories."
	except OSError as e:
		print("Execution failed in create_subdirectories: ", e)


def create_gitignore(project_name):
	"""Creates a .gitignore in the project directory."""
	with io.FileIO(".gitignore", "w") as file:
		file.write("# Directories #\n###################\nbin/\n\n"
				"# OS generated files #\n###################\n"
				".DS_Store\n._*\n.nfs*\n\n"
				"# Compiled source #\n###################\n"
				"a.out\n*.o")
	shutil.move('.gitignore', project_name)
	print "Created project .gitignore file."


def get_c_library(project_name):
	"""Clones the git repository containing a c library
		from https://github.com/CameronFredrickson/libft and removes the .git
		from the cloned directory. 
	"""
	try:
		retcode = subprocess.call("git clone "
			"https://github.com/CameronFredrickson/libft " + project_name + "/libft"
			, shell=True)
		if retcode < 0:
			print("Failed to clone library from github. return code: %d", retcode)
		else:
			print "Cloned libft from github."
	except OSError as e:
		print("Execution failed in get_c_library, 'git clone': ", e)
	try:
		retcode = subprocess.call("rm -rf " + project_name + "/libft/.git", shell=True)
		if retcode < 0:
			print("Failed to remove .git. return code: %d", retcode)
		else:	
			print "Removed .git from libft."
	except OSError as e:
		print("Execution failed in get_c_library, 'rm .git':")


def create_makefile(project_name):
	"""Creates a main.c in scrs and a simple Makefile."""
	with io.FileIO("main.c", "w") as file:
		file.write("int	main()\n{\n\treturn (0);\n}")
	shutil.move('main.c', project_name + '/srcs')
	with io.FileIO("Makefile", "w") as file:
		file.write("NAME = " + project_name +
		"\n\nSRCS = main.c\n\n"
		"HEADERS = srcs/includes\n\n"
		"OBJS = 	$(SOURCE:.c=.o)\n\n"
		"CC = gcc\n\n"
		"MEMERROR = -fsanitize=address\n\n"
		"CFLAGS = -Wall -Wextra -Werror\n\n"
		"LIBFLAG = -L\n\n.PHONY: all clean fclean re\n\n"
		"all: $(NAME)\n\n"
		"$(NAME):\n\t$(CC) $(CFLAGS) $(SOURCE) -I $(HEADERS)\n\n"
		"clean:\n\t/bin/rm -f $(OBJS)\n\n"
		"fclean: clean\n\t/bin/rm -f $(NAME)\n\n"
		"re: fclean all")
	shutil.move('Makefile', project_name)
	print "Created project Makefile."


def main():
	print "************************************************************************************"
	print "What is the project name?"
	project_name = raw_input()
	print "What language will you be using?"
	language = raw_input()
	create_project(project_name)
	create_subdirectories(project_name)
	if language == 'c' or language == 'C':
		get_c_library(project_name)
		create_makefile(project_name)
	create_gitignore(project_name)

if __name__ == '__main__':
	main()
