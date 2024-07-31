from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as description:
    long_description: str = description.read()

setup(
    name="async-sqlalchemy-bridge",
    version="1.0.0",
    author="MSNLP",
    description="The async library for easy connect to postgres database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["__pycache__"]),
    install_requires=[
        "asyncpg>=0.29.0,<=1.0.0",
        "greenlet>=3.0.3,<=4.0.0",
        "pydantic>=2.6.1,<=3.0.0",
        "SQLAlchemy>=2.0.27,<=3.0.0",
    ],
    python_requires=">=3.8",
)
