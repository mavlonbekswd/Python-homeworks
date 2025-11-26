from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} - {self.status} (Due: {self.due_date})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added successfully!")

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print("Task not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            print(task)

    def show_incomplete_tasks(self):
        incomplete = [t for t in self.tasks if t.status == "Incomplete"]
        if not incomplete:
            print("All tasks are complete!")
        else:
            for t in incomplete:
                print(t)


# -------- CLI Interface --------
def main():
    todo = ToDoList()

    while True:
        print("\n1. Add Task\n2. Mark Task Complete\n3. List All Tasks\n4. Show Incomplete Tasks\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            desc = input("Description: ")
            due = input("Due date (YYYY-MM-DD): ")
            task = Task(title, desc, due)
            todo.add_task(task)
        elif choice == "2":
            title = input("Enter task title to mark complete: ")
            todo.mark_complete(title)
        elif choice == "3":
            todo.list_all_tasks()
        elif choice == "4":
            todo.show_incomplete_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully!")

    def list_all_posts(self):
        if not self.posts:
            print("No posts yet.")
            return
        for post in self.posts:
            print(post)

    def posts_by_author(self, author):
        found = [p for p in self.posts if p.author == author]
        if not found:
            print(f"No posts by {author}.")
        else:
            for p in found:
                print(p)

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print("Post deleted.")
                return
        print("Post not found.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print("Post updated.")
                return
        print("Post not found.")

    def show_latest_posts(self, n=3):
        latest = sorted(self.posts, key=lambda x: x.created_at, reverse=True)[:n]
        for post in latest:
            print(post)


# -------- CLI Interface --------
def main():
    blog = Blog()

    while True:
        print("\n1. Add Post\n2. List All Posts\n3. Posts by Author\n4. Delete Post\n5. Edit Post\n6. Show Latest Posts\n7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            post = Post(title, content, author)
            blog.add_post(post)
        elif choice == "2":
            blog.list_all_posts()
        elif choice == "3":
            name = input("Author name: ")
            blog.posts_by_author(name)
        elif choice == "4":
            title = input("Enter title to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            title = input("Enter title to edit: ")
            new_content = input("New content: ")
            blog.edit_post(title, new_content)
        elif choice == "6":
            blog.show_latest_posts()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Remaining balance: {self.balance}")

    def __str__(self):
        return f"Account {self.account_number} - {self.holder_name} - Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("Account added successfully!")

    def find_account(self, acc_num):
        for acc in self.accounts:
            if acc.account_number == acc_num:
                return acc
        return None

    def deposit(self, acc_num, amount):
        acc = self.find_account(acc_num)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, acc_num, amount):
        acc = self.find_account(acc_num)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Transferred {amount} from {from_acc} to {to_acc}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One of the accounts not found.")

    def show_all_accounts(self):
        for acc in self.accounts:
            print(acc)


# -------- CLI Interface --------
def main():
    bank = Bank()

    while True:
        print("\n1. Add Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Show All Accounts\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            acc_num = input("Account number: ")
            name = input("Account holder: ")
            balance = float(input("Initial balance: "))
            acc = Account(acc_num, name, balance)
            bank.add_account(acc)
        elif choice == "2":
            acc_num = input("Account number: ")
            amount = float(input("Deposit amount: "))
            bank.deposit(acc_num, amount)
        elif choice == "3":
            acc_num = input("Account number: ")
            amount = float(input("Withdraw amount: "))
            bank.withdraw(acc_num, amount)
        elif choice == "4":
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amount = float(input("Transfer amount: "))
            bank.transfer(from_acc, to_acc, amount)
        elif choice == "5":
            bank.show_all_accounts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
