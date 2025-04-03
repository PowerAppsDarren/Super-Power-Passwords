from setuptools import setup, find_packages

setup(
    name="superpower_passwords",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Darren Neese",
    author_email="example@example.com",
    description="Password generator that creates memorable passphrases",
    keywords="passwords, security, generator",
    python_requires=">=3.6",
)