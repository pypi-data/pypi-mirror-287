from setuptools import setup

setup(
    name='PMAR_Breakdowns',
    version='1.0',
    py_modules=['PMAR_Breakdowns'],
    install_requires=[
        'pandas',
        'matplotlib',
        'numpy'
    ],
    author='Timothy Colledge',
    author_email='timothy.colledge@invesco.com',
    description='This Library serves as a support file for IVZ python scipts. It contains functions and classes that are utilized in data processing for PMAR FI analytics.',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mylibrary',  # Optional: URL of your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
