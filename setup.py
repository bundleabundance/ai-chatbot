from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
        'flask',
        'Flask-SQLAlchemy',
        'flask-cors',
        'openai', 
        'python-dotenv'

        # other dependencies
    ],
    entry_points={
        'console_scripts': [
            'my_project=my_project.main:main_function',
        ],
    },
    author='Alper Gül',
    author_email='alpergul_99@hotmail.com',
    description='A basic ai-chatbot for aiding customers on a SAAS project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
