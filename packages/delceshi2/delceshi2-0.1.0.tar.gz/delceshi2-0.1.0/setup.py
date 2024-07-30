from setuptools import setup
from Cython.Build import cythonize
import os

def run_setup():
    setup(
        name='delceshi2',
        version='0.1.0',
        ext_modules=cythonize(["delceshi2/main.pyx", "delceshi2/timer.pyx"]),
        packages=['delceshi2'],
        install_requires=[],
        entry_points={
            'console_scripts': [
                'delceshi2 = delceshi2.main:main',
            ],
        },
        author='Your Name',
        author_email='your.email@example.com',
        description='A package that returns 0.01 and uninstalls itself after 3 minutes.',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/yourusername/self_deleting_package',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.6',
    )

if __name__ == "__main__":
    run_setup()
