from setuptools import setup
from Cython.Build import cythonize
import os

def run_setup():
    setup(
        name='seldetpacceshi',
        version='0.1.0',
        ext_modules=cythonize(["seldetpacceshi/main.pyx", "seldetpacceshi/timer.pyx"]),
        packages=['seldetpacceshi'],
        install_requires=[],
        entry_points={
            'console_scripts': [
                'self_deleting_package = seldetpacceshi.main:main',
            ],
        },
        author='Your Name',
        author_email='your.email@example.com',
        description='ue, and then uninstalls itself.',
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
