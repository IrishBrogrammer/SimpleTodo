import json
import sys
import os,glob
import os.path

def PrintDoneList( completed ) : 
  print "\n"
  print "******** DONE ********\n"
  for done in completed :
       print done
  
def PrintToDoList( todoList ) :

   print "\n"
   print "******* TO-DO *******\n"
   index = 0
   for todo in todoList :
       print str(index) + " : " + todo
       index = index + 1
   print "\n"
   print "*********************"


def PrintHelp() : 
  print "\n"
  print "print : Print list of to-dos" 
  print "add : Add a todo to the list" 
  print "removeitem : Remove item from todo list"
  print "clear : Clear the list"
  print "end : end the program"
  print "done : Move an item to the done list" 
  print "undo : Move item from done list to the todo list "
  print "cleartodo : Clear todo list "
  print "cleardone : Clear done list " 
  print "report : Create a json report for the days work "  
  print "\n"


def MoveToDoneList( todoList ) : 

    str_index = raw_input( " Item to move to done : " )
    index = int( str_index )
    
    item = todoList["todo"].pop( index )
    todoList["done"].append( item )
    return todoList

def MoveToTodoList( todoList ) : 

    str_index = raw_input( " Item to move to done : " )
    index = int( str_index )
    
    item = todoList["done"].pop( index )
    todoList["todo"].append( item )
    return todoList
    
    
def ClearPartOfList( todoList ,listToClear ) :
    todoList[listToClear] = []
    return todoList
    
def RemoveItem( todoList  ) : 
    
     str_index = raw_input("index to remove : ")
     index = int( str_index)
     todo = todoList[index]
     confirm = raw_input( "Are you sure you want to remove  : \n" + todo + "\n Y/N \n" )
     
     if ( confirm == "y" or confirm == "Y" ) :
        todoList.pop( index )
        
     return todoList

def PrintReport( todoList ) : 
    with open( "report.json" , "w+" ) as f:
         f.write( "Report \n" )
         for done in todoList["done"] :
            f.write( done + "\n" )




def RunMain( todoList ) :
    run = True
    command = ""
    while ( run ) :
        
        command = raw_input( " Enter a command ")

        if ( command == "print" ) :
            PrintDoneList( todoList["done"])
            PrintToDoList( todoList["todo"] )
        
        if ( command == "end" ) :
            run = False

        if ( command == "add" ) :
            newTodo = raw_input( "Add todo ")
            todoList["todo"].append( newTodo )

        if ( command == "removeitem" ) :
            todoList["todo"] = RemoveItem( todoList["todo"] )
        
        if ( command == "done" ) : 
            todoList = MoveToDoneList( todoList)
        
        if ( command == "help" ) : 
            PrintHelp()
            
        if ( command == "undo" ) : 
            todoList = MoveToTodoList( todoList )
            
        if ( command == "cleartodo" ) : 
            todoList = ClearPartOfList( todoList , "todo" )
            
        if ( command == "cleardone" ) : 
           todoList =  ClearPartOfList( todoList , "done" )
           
        if ( command == "clear" ) :
            todoList = []
            
        if ( command == "report" ) : 
            PrintReport( todoList )
            
    return todoList


# load json to do list
filename = str( sys.argv[1])

print filename
with open( filename ) as data_file :
    data = json.load( data_file )
    
data = RunMain( data )

with open( filename , 'w' ) as f :
    f.write( json.dumps( data , sort_keys=True , indent=4 , separators=(',',':') ))



