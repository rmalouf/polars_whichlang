SHELL=/bin/bash

venv:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

install:
	unset CARGO_TARGET_DIR && \
	source .venv/bin/activate && maturin develop

install-release:
	unset CARGO_TARGET_DIR && \
	source .venv/bin/activate && maturin develop --release

build:
	unset CARGO_TARGET_DIR && \
	source .venv/bin/activate && maturin build

build-release:
	unset CARGO_TARGET_DIR && \
	source .venv/bin/activate && maturin build --release

pre-commit:
	cargo +nightly fmt --all && cargo clippy --all-features
	.venv/bin/python -m ruff check . --fix --exit-non-zero-on-fix
	.venv/bin/python -m ruff check . --select I --fix
	.venv/bin/python -m ruff format polars_whichlang tests
	.venv/bin/python -m mypy polars_whichlang tests

test:
	.venv/bin/python -m pytest tests

run: install
	source .venv/bin/activate && python run.py

run-release: install-release
	source .venv/bin/activate && python run.py

nox: venv build-release
	source .venv/bin/activate && nox

clean:
	/bin/rm -rf .venv .nox target
