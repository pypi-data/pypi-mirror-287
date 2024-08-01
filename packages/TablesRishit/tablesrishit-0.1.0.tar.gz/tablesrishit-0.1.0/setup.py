from setuptools import setup, find_packages

setup(
    name='TablesRishit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # List any dependencies your package needs here
    author='Rishit',
    author_email='dhimanrishit215@gmail.com',
    description='A module for creating tables.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/TablesRishit',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
