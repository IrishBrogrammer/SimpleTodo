import json
import sys
import os,glob
import os.path





def PrintToDoList( todoList ) :

   print "\n"
   print "******* TO-DO *******\n"
   for todo in todoList :
       print todo
   print "\n"
   print "*********************"


def PrintHelp() : 
  print "\n"
  print "print : Print list of to-dos" 
  print "add : Add a todo to the list" 
  print "removeitem : Remove item from todo list"
  print "clear : Clear the list"
  print "end : end the program"
  print "\n"


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
        
        if ( command == "help" ) : 
            PrintHelp()
            
        if ( command == "clear" ) :
            todoList = []

    return todoList


# load json to do list
filename = str( sys.argv[1])

print filename
with open( filename ) as data_file :
    data = json.load( data_file )
    
data["todo"] = RunMain( data["todo"])
with open( filename , 'w' ) as f :
    f.write( json.dumps( data , sort_keys=True , indent=4 , separators=(',',':') ))



