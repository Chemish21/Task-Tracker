# Task-Tracker
A Command Line Interface program to track tasks taken from suggested projects by roadmap.sh 
source: https://roadmap.sh/projects/task-tracker

**Commands**: There are five basic commands that can be done.  These are add, delete, update, mark, and list.  

Usage:
  
  **add**:  add a task.  Simply type add and then write a description of the task to be added.  
  example:
          add "Buy Groceries"


  **delete**:  delete a task.  Provide the id number of the task to be deleted.  
  example: 
          delete 2


  **update**:  update a tasks description.  Provide id number of desired task and then write new description.  
  example: 
          update 1 "Buy Clothes"


  **mark**:  marks a tasks status.  The options are todo, in-progress, and done.  Must provide id of task and then write desired mark.  
  example: 
          mark 1 "todo"


  **list**:  Displays a task or tasks.  Tasks can be listed individually with '-id' or all with '-a'.  Note with '-id' you must provide the id of desired task.  Tasks can also be listed by status with '-d' for finished tasks, 
  '-ud' for unfinished tasks, and '-ip' for in-progress tasks.

  Usage of '-id'  
  example: 
          list -id 1

  Usage of other options  
  example: 
          list -a
          list -d
          list -ud
          list -ip
