#uv run src/main.py
#cd public && uv run -m http.server 8888

cd /home/liras/workspace/Github.com/Nongrenost/Static-Site-Generator
uv run -m src.main
cd docs && uv run -m http.server 8888