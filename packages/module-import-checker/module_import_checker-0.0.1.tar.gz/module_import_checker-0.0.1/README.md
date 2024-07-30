# Modular Monolith Import Checker

## Overview

The Modular Monolith Import Checker is a Python utility designed to enforce modular boundaries within your codebase. It ensures that modules within a modular monolith architecture do not import each other inappropriately. This is useful for maintaining clear module boundaries and ensuring a clean architecture.

## Features

- **Detect Forbidden Imports:** Identifies cases where a module imports another module that it shouldn't.
- **Flexible Path Handling:** Supports both absolute and relative paths for specifying base directories.
- **Dynamic Module List:** Allows you to specify a list of modules to check.

## Installation

To use the module import checker, you need to have Python 3 installed. You can then pip install module_import_checker


## Usage

You can run the import checker from the command line or import it into your Python scripts.

### Command-Line Interface

You can run the script directly from the command line with various configurations:

1. **Modules at the Project Root:**
    import ModuleImportChecker
    module_import_checker = ModuleImportChecker()
    module_import_checker.run_module_checker()

   ```bash
   python your_script.py /path/to/project module1 module2 module3
   ```

   - `/path/to/project` is the base directory of your project.
   - `module1`, `module2`, `module3`, etc., are the names of the modules you want to check.

2. **Modules in the Current Directory:**

   ```bash
   python your_script.py . module1 module2 module3
   ```

   - Use `.` if you are running the script from the project root directory.

3. **Modules Inside a Subdirectory:**

   ```bash
   python your_script.py project_name module1 module2 module3
   ```

   - `project_name` is the name of the subdirectory containing your modules.

### Example

To check imports in a project located in `/home/user/myproject` where modules are named `auth`, `users`, and `payments`, run:

```bash
python your_script.py /home/user/myproject auth users payments
```

### Command-Line Help

For detailed usage information, run:

```bash
python your_script.py --help
```

### Example Output

```text
Checking base directory: /home/user/myproject
Checking module /home/user/myproject/auth/
Import check failed with errors
Forbidden import detected: 'users' imports 'auth' in /home/user/myproject/users/services.py
Import check failed with errors.
```


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Ensure that your code follows the existing style and includes tests for new features.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [abiolaadeshinaadedayo@gmail.com](mailto:abiolaadeshinaadedayo@gmail.com).
