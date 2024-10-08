
---

# School Class Information Program

## Overview

This Python program defines a `school` class that stores and manages information about a school class, including the branch, teacher, department, and the number of available students. It also provides methods to display the class information and retrieve the teacher's name.

## Features

- **`show_info()`**: Displays detailed information about a specific class, including branch, teacher, department, and available students.
- **`teacher_name()`**: Prints only the teacher's name for a specific class.

## Code Structure

The `school` class includes:
- **Attributes**:
  - `branch`: Represents the class branch (e.g., "12-A", "12-B").
  - `teacher`: Represents the name of the teacher responsible for the class.
  - `department`: Represents the department the class belongs to (e.g., "SE" for Software Engineering, "CE" for Civil Engineering).
  - `available`: Represents the number of available students in the class.

- **Methods**:
  - `show_info()`: Prints out all the details about the class.
  - `teacher_name()`: Prints out only the name of the teacher.

## Usage Example

### Creating Objects

Two class objects are created: `first_class` and `second_class`. Each object represents a school class with its own attributes.

```python
first_class = school("12-A", "Emre", "SE", "25")
second_class = school("12-B", "Ahmet", "CE", "56")
```

### Displaying Information

You can call the `show_info()` method on any class object to display its details:

```python
first_class.show_info()
```

Output:
```
---------------------------------------------
Branch: 12-A
Teacher: Emre
Department: SE
Avaliable Student: 25
---------------------------------------------
```

Similarly, for the second class:
```python
second_class.show_info()
```

### Displaying Teacher's Name

To display only the teacher's name, call the `teacher_name()` method:

```python
second_class.teacher_name()
```

Output:
```
Teacher name: Ahmet
```

## Running the Code

1. Copy the code into a Python file, for example, `school.py`.
2. Run the file using Python 3.x:

```bash
python school.py
```

Ensure you have Python 3.x installed on your system.

## Future Improvements

- Add functionality to update class information (e.g., change the teacher or the number of available students).
- Implement input validation to ensure the correct format of data is entered.

---

