from setuptools import setup

setup(
    name="tt",
    packages=["tt"],
    version="0.1",
    description="Tools for producing turn taking datasets from recordings of group discussions",
    author="Szymon Talaga",
    install_requires=[
        "numpy",
        "scipy",
        "pandas>=2.0",
        "tqdm"
    ]
)
