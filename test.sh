#uv run python -m unittest discover -s src/tests
#uv run python -m doctest -v $(fd . -e py)
uv run pytest
