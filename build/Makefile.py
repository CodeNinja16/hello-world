# Makefile tool for building the project
#
# See "Requirements.txt" for additional information
#
# File must run from the build directory, for more info see requirements

# [IMPORTS]
import os
import sys
import py_compile

# Command line args
args = sys.argv # Shorthand

# Check command line args are present
if len(args) < 2:
	print("E: No build target specified")
	print("Please specify at least one option")
	
	quit()

script = args[0] # Current script name
target = args[1] # Current build target
flags = [] # Populated if needed

def parse_flags():
    if not len(args) < 2:
        for i in range(2, len(args)):
            flags.append(args[i])
            
def pause_thread():
    input("Press enter to continue...")
            
def error_msg(detail):
    print("An error occured and the operation was aborted")
    print("Detail: " + detail)
    pause_thread()
    sys.exit(-1)
    
def compile_main():
    
    # Change directory to root
    os.chdir(os.getcwd() + "\..")
    print("Attempting to compile from " + os.getcwd())
    
    # Try and compile our main file
    try:
        py_compile.compile('__main__.py', cfile=os.getcwd() + "\\Main.pyc")
    except Exception as e:
        error_msg("Error during compilation: " + str(e))
        
def clean():
    # Change directory to root
    os.chdir(os.getcwd() + "\..")

    os.remove("Main.pyc")
	
    print("Cleaned build files and removed compilation result")
    
         
if __name__ == "__main__":
    print("Test python makefile experiment")
    print("By OverEngineeredCode")
    
    parse_flags() # We don't actually need the flags yet
    
    # MAIN TARGET LOOP
    
    if target == "clean":
        clean()
    elif target == "build":
        compile_main()
    else:
        error_msg("Unspecified or invalid build target")
        
print("Task succeeded")
pause_thread()
