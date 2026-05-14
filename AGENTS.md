# AGENTS.md - AI Agent Guide for pythonProject

This guide helps AI agents contribute effectively to this Python project by understanding its structure, conventions, and development workflows.

## Project Overview

**pythonProject** is a Python-based project with the following characteristics:
- Python 3.13+ environment (via `.venv`)
- Dependencies: pandas, requests, numpy, pytz, and other data/networking libraries
- IDE: PyCharm (configuration in `.idea/`)

## Quick Setup for AI Agents

### Environment
- Virtual environment located at `.venv/`
- Activate before running: `source .venv/bin/activate`
- Python version: 3.13+

### Key Installed Packages
- `pandas`: Data manipulation and analysis
- `numpy`: Numerical computing
- `requests`: HTTP client library
- `pytz`: Timezone support
- `tzdata`: Timezone database

## Project Structure (To Be Established)

Recommended structure for new features:
```
pythonProject/
├── src/               # Main source code
│   └── project/       # Main package
├── tests/             # Unit and integration tests
├── requirements.txt   # Project dependencies
├── setup.py          # Package configuration
├── .env.example      # Environment template
└── AGENTS.md         # This file
```

## Development Workflows

### Running Code
```bash
# Activate environment
source .venv/bin/activate

# Run a Python script
python script_name.py

# Run tests (once test framework is established)
pytest tests/
```

### Adding Dependencies
1. Activate `.venv`: `source .venv/bin/activate`
2. Install: `pip install package_name`
3. Update `requirements.txt`: `pip freeze > requirements.txt`

### Code Quality Standards
- **Linting**: Use `pylint` or `flake8` (to be configured)
- **Formatting**: Use `black` for code formatting (to be configured)
- **Type hints**: Use Python type hints for better IDE support
- **Docstrings**: Follow Google or NumPy docstring style

## Common Patterns & Conventions

### Python Best Practices
- Use `if __name__ == "__main__":` guard for executable scripts
- Organize imports: stdlib → third-party → local
- Use context managers (`with` statements) for file/resource handling
- Follow PEP 8 naming: `snake_case` for functions/variables, `PascalCase` for classes

### Data Processing (pandas/numpy)
When working with data:
- Load data with `pd.read_csv()`, `pd.read_json()`, etc.
- Use vectorized operations over loops
- Handle missing values explicitly with `.fillna()` or `.dropna()`
- Use dtype specifications during data loading for performance

### API/Network Requests
When using `requests` library:
```python
import requests

response = requests.get(url, timeout=10)
response.raise_for_status()  # Raise exception for bad status
data = response.json()
```

## Integration Points

### External Dependencies
- **Data processing**: pandas, numpy
- **HTTP requests**: requests
- **Timezone handling**: pytz, tzdata
- **IDE**: PyCharm (configured via `.idea/`)

### File I/O Patterns
- Use relative paths for data files: `Path(__file__).parent / "data/file.csv"`
- Store configuration in `.env` files (use `python-dotenv` if needed)

## Testing Strategy (To Be Established)

Once testing framework is set up:
- Unit tests in `tests/` directory
- Test file naming: `test_*.py` or `*_test.py`
- Use `pytest` framework (recommended for Python projects)
- Aim for >80% code coverage

## Documentation Standards

- Add docstrings to all functions and classes
- Update this AGENTS.md when establishing new patterns
- Include comments for complex logic
- Keep README.md updated with high-level project info

## AI Agent Constraints & Tips

### Do's
✓ Maintain consistency with existing code style
✓ Run tests before finalizing changes
✓ Use type hints and docstrings
✓ Follow PEP 8 conventions
✓ Activate `.venv` before running any Python code

### Don'ts
✗ Modify `.venv/` directly - use pip install instead
✗ Commit `.venv/`, `__pycache__/`, `.pyc` files
✗ Mix tabs and spaces (use 4 spaces)
✗ Ignore errors - handle exceptions explicitly

## Getting Help

- Check PyCharm's built-in documentation and type hints
- Refer to library documentation: pandas docs, requests docs
- Use semantic search to find existing implementations before creating new ones
- When in doubt, add explicit error handling with informative messages

---

**Last Updated**: May 14, 2026  
**Project Root**: `/Users/anjalijaiswal/PycharmProjects/pythonProject`

