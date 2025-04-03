import os
import shutil

# Base directory (current directory)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define the directory structure
structure = {
    "src/superpower_passwords": ["__init__.py", "main.py", "generator.py", "gui.py"],
    "tests": ["__init__.py", "test_generator.py"],
    "docs": ["usage.md"],
    "examples": ["passphrases.txt"]
}

# Files that should be in the root directory
root_files = ["README.md", "LICENSE", "requirements.txt", "setup.py", ".gitignore"]

def create_structure():
    print(f"Creating project structure in {base_dir}")
    
    # Create directories and files
    for directory, files in structure.items():
        dir_path = os.path.join(base_dir, directory)
        
        # Create directory if it doesn't exist
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {directory}")
        
        # Create files in the directory
        for file in files:
            file_path = os.path.join(dir_path, file)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    if file == "passphrases.txt" and os.path.exists(os.path.join(base_dir, "passphrases.txt")):
                        # Copy existing passphrases.txt content if it exists
                        try:
                            with open(os.path.join(base_dir, "passphrases.txt"), 'r') as src:
                                f.write(src.read())
                        except:
                            pass
                    elif file == "main.py" and os.path.exists(os.path.join(base_dir, "main.py")):
                        # Copy existing main.py content to src directory
                        try:
                            with open(os.path.join(base_dir, "main.py"), 'r') as src:
                                f.write(src.read())
                        except:
                            pass
                print(f"Created file: {directory}/{file}")
    
    # Create root files if they don't exist
    for file in root_files:
        file_path = os.path.join(base_dir, file)
        if not os.path.exists(file_path) and file != "README.md" and file != "LICENSE":
            with open(file_path, 'w') as f:
                # Add content to specific files
                if file == "requirements.txt":
                    f.write("# Project dependencies\ntkinter\n")
                elif file == "setup.py":
                    f.write("""from setuptools import setup, find_packages

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
)""")
                elif file == ".gitignore":
                    f.write("""# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
dist/
build/
*.egg-info/

# Virtual environments
venv/
env/
.env/

# Editor specific files
.vscode/
.idea/
*.swp
*.swo

# OS specific files
.DS_Store
Thumbs.db
""")
            print(f"Created file: {file}")
        # Don't overwrite existing README.md or LICENSE
    
    print("\nProject structure created successfully!")
    print("\nNext steps:")
    print("1. Move your existing code from root/main.py to src/superpower_passwords/")
    print("2. Update imports in your code")
    print("3. Create a virtual environment and install dependencies")
    print("4. Run your project using 'python -m src.superpower_passwords.main'")

if __name__ == "__main__":
    create_structure()