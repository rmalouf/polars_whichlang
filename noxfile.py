import nox

nox.options.default_venv_backend = "uv" 

PYTHONS = ["3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]

@nox.session(python=PYTHONS)
@nox.parametrize("polars", ["1.0", "1.33"])
def tests(session, polars):
    session.install(f'pytest')
    session.install(f'polars=={polars}')
    session.install("target/wheels/polars_whichlang-0.1.0-cp39-abi3-macosx_11_0_arm64.whl")
    # session.run("python", "-c", "import polars ; print(polars.__version__)")
    session.run("pytest")