#Python
import argparse

#Initializing top-level Parser and Sub-Parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

#Initializing Sub-Parsers
add_parser = subparsers.add_parser('add')
delete_parser = subparsers.add_parser('delete')
update_parser = subparsers.add_parser('update')
mark_parser = subparsers.add_parser('mark')
list_parser = subparsers.add_parser('list')

#Parser Arguments

#Add
add_parser.add_argument('task', type=str, help='Write description of task')

#Delete
delete_parser.add_argument('id', type=int, help='id of task to be deleted')

#Update
update_parser.add_argument('id', type=int, help='id of task to be updated')
update_parser.add_argument('task', type=str, help='Write new task description')

#Mark
mark_parser.add_argument('id', type=int, help='id of task to be marked')
mark_parser.add_argument('mark', type=str, help='Write mark option, options: [1] todo [2] in-progress [3] done')

#List
list_parser.add_argument('-id', '--identify', metavar="task_id",type=int, help='List specific task based on id')
list_parser.add_argument('-a', '--all', action="store_true", help='List all tasks')
list_parser.add_argument('-d', '--done', action="store_true", help='List finished tasks')
list_parser.add_argument('-ud', '--undone', action="store_true", help='List undone tasks')
list_parser.add_argument('-ip', '--progress', action="store_true", help='List in-progress tasks')

#Finalizing arguments
args = parser.parse_args()
