import sys, argparse, os, shutil, cmd, re, zipfile

__all__ = ["__version__"]
__pygstudio_version__ = "1.1"
__version__ = "1.1"

def warn(message):
    print("\033[93m" + message + "\033[0m")

if sys.version_info < (3, 8, 0):
    warn("[Warning]: Pygstudio may not work as intended in lower versions of python. " 
         "It is recommended to have python 3.8.0 or above!")
    
def _ignore_dir(directory, files): return ["__pycache__"]

def _get_user_choice(message):
    choice = input(message + " (y/n) ")
    if choice.lower().startswith("y"): return True
    elif choice.lower().startswith("n"): return False
    return _get_user_choice(message)

# class CLIPROMPT(cmd.Cmd):
#     intro = f"Hello Pygstudio! Made by EF. Version {__version__}"
#     prompt = ">>> "
#     def do_exit(self, args): sys.exit()
#     def do_create(self, args): 
#         largs = re.findall(r'\"*.?\"|\S+', args)
#         print(largs, len(largs))
#         output_name = DEFAULT_OUTPUT_NAME
#         output_directory = "."
#         if len(largs) > 0 and largs[0] != "": output_name = largs[0]
#         if len(largs) > 1: output_directory = largs[1]
            
#         copy_template(output_directory, output_name)
    
#     def help_exit(self): print(UPPERHEAD.format("Description") + "\n- Exits pygstudio.")
#     def help_create(self): print(UPPERHEAD.format("Description") + "\n- " + DESCRIPTION_CREATE + 
#         f"\n- Usage: create [project_name (default='{DEFAULT_OUTPUT_NAME}')] " 
#         "[output_directory (default=current_directory)]")

def main():
    mparser = argparse.ArgumentParser(
        prog="pygstudio",
        description="A cli to easily create pygstudio based games.",
        epilog="@ pygstudio v1.1 by flamfrosticboio"
    )
    
    subparser = mparser.add_subparsers()
    parser_create = subparser.add_parser("create", help='creates a new pygstudio project from template')
    parser_create.add_argument('name', type=str, help="name of the project")
    parser_create.add_argument("-o", "--output", type=str, default=".", 
                               help='the output directory of the project (default=".")')
    mparser.add_argument("-v", "--version", action="version",
                        help="prints the version of pygstudio and cli",
                        version=f"pygstudio {__pygstudio_version__} (cli version: {__version__})")
    
    args = mparser.parse_args()
    if not any(vars(args).values()):
        sys.exit("No arguments provided. Type `pygstudio -h` for help.")
    elif args.name:
        copy_template(args.output, args.name)
        
        
def copy_template(output_folder, output_name, skip=False):
    output_folder = os.path.abspath(output_folder) + "\\" + output_name
    template_folder = os.path.dirname(os.path.abspath(__file__)) + "\\template"
    
    if os.path.exists(output_folder) and skip == True:
        choice = _get_user_choice("Warning: The project exists! Overwrite?")
        if choice == True: shutil.rmtree(output_folder)
        else: return print("Operation is cancelled!")   # returning print nice
        
    if not os.path.isdir(template_folder):
        template_zip = os.path.join(os.path.dirname(template_folder), "template.zip")
        with zipfile.ZipFile(template_zip, "r") as zip_ref:
            zip_ref.extractall(template_folder)
        
    shutil.copytree(template_folder, output_folder, ignore=_ignore_dir)
    
    main_file_directory = output_folder + "\\main_game.py"
    
    with open(main_file_directory, "rt") as main_file: 
        contents = main_file.read().replace("$MYPYGSTUDIOGAME",  output_name)
        
    with open(main_file_directory, "wt") as main_file: 
        main_file.write(contents)
        
    os.rename(main_file_directory, output_folder + "\\" + output_name + ".py")
    
    print(f"Successfully created a new Pygstudio project at '{os.path.abspath(os.path.dirname(output_folder))}'")
    
if __name__ == '__main__': 
    main()