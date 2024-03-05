# AirBnB Clone ✨

This is a command-line interface (CLI) application that replicates some of the core functionalities of the AirBnB website. It allows users to manage and interact with property listings, bookings, and user accounts. The application is built using Python and follows the Model-View-Controller (MVC) design pattern.

## Command Interpreter 🖥

The command interpreter is the main component of the AirBnB clone. It provides a command-line interface for interacting with the application. To start the command interpreter, follow these steps:

1. Clone the AirBnB clone repository from GitHub.
2. Navigate to the root directory of the project.
3. Run the command `./console.py` or `python3 console.py` to start the command interpreter.

Once the command interpreter is running, you can use various commands to interact with the application. Here are some examples of commands you can use:

- `create <class>`: Creates a new instance of a given class.
- `show <class> <id>`: Displays information about a specific instance.
- `update <class> <id> <attribute> <value>`: Updates the value of a specific attribute of an instance.
- `destroy <class> <id>`: Deletes a specific instance.
- `all <class>`: Shows all instances of a specific class or all instances if no class is specified.

For a complete list of available commands and their usage, you can use the `help` command within the interpreter.

## Examples

Here are some examples of commands and their expected output:

(hbnb) create User
b6a6e15c-c67d-4312-9a75-9d084935e579

(hbnb) show User b6a6e15c-c67d-4312-9a75-9d084935e579
[User] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2024-03-05T10:30:00.123450', 'updated_at': '2024-03-05T10:30:00.123567'}

(hbnb) update User b6a6e15c-c67d-4312-9a75-9d084935e579 name "John Doe"

(hbnb) show User b6a6e15c-c67d-4312-9a75-9d084935e579
[User] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2024-03-05T10:30:00.123450', 'updated_at': '2024-03-05T10:30:00.123567', 'name': 'John Doe'}

(hbnb) all User
["[User] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2024-03-05T10:30:00.123450', 'updated_at': '2024-03-05T10:30:00.123567', 'name': 'John Doe'}"]


##AUTHORS 👨‍💻

- Juman Hassan <jumanhassan47@gmail.com>