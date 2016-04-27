import json
import sys
import os,glob
import os.path


class bcolors:
    OKBLUE = '\033[94m'
    TODO = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def PrintToDoList( todoList ) :

   print "******* TO-DO *******\n"
   for todo in todoList :
       print todo
   print "\n"
   print "*********************"


def RunMain( todoList ) :
    run = True
    command = ""
    while ( run ) :
        command = raw_input( " Enter a command ")

        if ( command == "print" ) :
            PrintToDoList( todoList )

        if ( command == "end" ) :
            run = False

        if ( command == "add" ) :
            newTodo = raw_input( "Add todo ")
            todoList.append( newTodo )

        if ( command == "removeitem" ) :
            str_index = raw_input("index")
            index = int( str_index)
            todoList.pop( index )

        if ( command == "clear" ) :
            todoList = []

    return todoList

# load json to do list
filename = str( sys.argv[1])

print filename
with open( filename ) as data_file :
    data = json.load( data_file )
    todoList = data["todo"]


data["todo"] = RunMain( data["todo"])


with open( filename , 'w' ) as f :
    f.write( json.dumps( data , sort_keys=True , indent=4 , separators=(',',':') ))
