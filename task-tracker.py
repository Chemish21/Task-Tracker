#Python
from args import args
import tasks

def main():
    if args.command == 'add':
        tasks.add_task(args.task)
    elif args.command == 'delete':
        tasks.delete_task(args.id)
        tasks.update_id()
    elif args.command == 'update':
        tasks.update_task(args.id, args.task)
    elif args.command == 'mark':
        tasks.mark_task(args.id, args.mark)
    elif args.command == 'list':
        if args.identity:
            tasks.list_one(args.identity)
        if args.all:
            tasks.list_all()
        if args.done:
            tasks.list_done()
        if args.undone:
            tasks.list_not_done()
        if args.progress:
            tasks.list_in_progress()
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
