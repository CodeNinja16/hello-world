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
    os.chdir(os.getcwd() + "..")
    print("Attempting to compile from " + os.getcwd())
    
    # Try and compile our main file
    try:
        py_compile.compile('__main__.py', cfile=os.getcwd() + "build/Main.pyc")
    except:
        error_msg("Error during compilation")
        
def clean():
    pass
    
         
if __name__ == "__main__":
    print("Test python makefile experiment")
    print("By CodeNinja16")
    
    parse_flags() # We don't actually need the flags yet
    
    # MAIN TARGET LOOP
    
    if target == "clean":
        # To be implemented
        pass
    elif target == "build":
        build_main()
    else:
        print("Invalid build target")
        print("Could not compile because a valid build target was not entered")
        
print("Build succeeded")
pause_thread()
