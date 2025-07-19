# Agent Development Guide

## Commands
- Install dependencies: `uv sync`
- Run function call tests: `uv run python test_api_function_calls.py`
- Format code: `uv run ruff format .`
- Lint code: `uv run ruff check .`
- Type check: `uv run mypy .`

## Code Style
- THIS IS NOT A DEMO THIS IS THE ADK IMPLEMENTATION DO NOT SKIP FEATURES AND SAY WE WILL IMPLEMENT IT IN THE REAL ONE
- Imports: Standard lib, third-party, local; one per line
- Types: Use type hints (PEP484); include return types
- Naming: snake_case for vars/functions; PascalCase for classes; UPPER_SNAKE_CASE for constants
- Formatting:4 spaces;79 char line limit; blank lines between classes/functions
- Error Handling: Specific exceptions; log with context; never expose sensitive data
- Docstrings: Google style; include args/returns/examples
- DO NOT MODIFY THE `__init__.py` file
