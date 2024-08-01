from setuptools import setup, find_packages

setup(
    name='ai_controller',
    version='0.1.0',
    author='Tanay Sharma',
    author_email='tanaysharmaajmer@gmail.com',
    description='AI-Agent (Auto-Code Executor) is a Python module that dynamically executes Python functions based on textual input. It leverages a language model (LLM) to match the input text with function descriptions and then executes the corresponding function from a specified file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Tanay-Sharma-01/ai_controller/tree/develop',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>3.10',
)