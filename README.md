# LitePolis-router Template

This repository serves as a template for creating template modules for LitePolis.  It provides a basic structure and example code to guide you through the process.

> :warning: Keep the prefix "litepolis-router-" and "litepolis_router_" in the name of package and directories to ensure the LitePolis package manager will be able to recognize it during deployment.

## Getting Started

1. **Clone the Repository:** Start by cloning this repository to your local machine.

2. **Rename the Package:**  Update the package name in the following files:
    * **`setup.py`**: Change `name='litepolis-router-template'` to your desired package name (e.g., `litepolis-router-dashboard`).  Also, update the `version`, `description`, `author`, and `url` fields accordingly.
    * **`tests/test_core.py`**: Update the import statement to reflect your new package name. For example, change `from litepolis_router_template import *` to `from litepolis_router_dashboard import *`.
    * Rename the folder `litepolis_router_dashboard` to your new package name.

3. **Implement Database Logic:** Modify the `litepolis_router_template/core.py` file (renamed in the previous step) to interact with your specific database.  The provided example code includes a basic structure with example endpoints.  Replace these with your database operations.  Ensure you update the docstrings to accurately reflect the functionality of your endpoints.  These docstrings will be used to generate API documentation.

4. **Testing:** The `tests/test_core.py` file contains example tests.  Update these tests to cover your database module's functionality.  Ensure the tests run successfully after making changes.

## Key Files and Modifications

* **`setup.py`**:  This file contains metadata about your package.  **Crucially**, you need to change the `name` field to your package's unique name.  Also, update the `version`, `description`, `author`, and `url` fields as needed.

* **`litepolis_router_template/core.py`**: This file contains the core logic for your module. The template provides example endpoints (`/` and `/user`).  Replace these with your own endpoints and operations.  **Important:** Update the docstrings for API documentation generation.  Pay attention to the `ResponseMessage` model and adapt it if necessary to fit your data structures.

* **`tests/test_core.py`**: This file contains tests for your module.  Update the tests to reflect your changes in `core.py`.  Thorough testing is essential for ensuring the correctness of your module.

## Important Considerations

* **API Documentation:**  Well-documented code is crucial for maintainability and collaboration.  Ensure your endpoints in `core.py` have clear and comprehensive docstrings. These docstrings will be used to generate API documentation for LitePolis. For best practices and detailed examples, refer to this helpful resource: [How to Document an API for Python FastAPI](https://medium.com/codex/how-to-document-an-api-for-python-fastapi-best-practices-for-maintainable-and-readable-code-a183a3f7f036)

* **Testing:**  Write comprehensive tests to cover all aspects of your router module.  This will help catch errors early and ensure the stability of your code.

* **Dependencies:**  If your module requires external libraries, add them to the `install_requires` list in `setup.py`.

