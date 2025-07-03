SHELL=/bin/bash

venv:
	uv venv
	uv pip install -r requirements.txt

install:
	source .venv/bin/activate && maturin develop

install-release:
	source .venv/bin/activate && maturin develop --release

pre-commit:
	cargo +nightly fmt --all && cargo clippy --all-features
	ruff check . --fix --exit-non-zero-on-fix
	ruff check . --select I --fix
	ruff format polars_whichlang tests
	ty check polars_whichlang tests

test:
	.venv/bin/python -m pytest tests

run: install
	source .venv/bin/activate && python run.py

run-release: install-release
	source .venv/bin/activate && python run.py

