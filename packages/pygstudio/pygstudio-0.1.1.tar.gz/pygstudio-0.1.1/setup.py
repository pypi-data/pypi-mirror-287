from setuptools import setup, find_packages

setup(
    name='pygstudio',
    version='0.1.1',
    author='flamfrosticboio',
    author_email='ffe.jhexe@gmail.com',
    description='A tool to help build games easily with pygame.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/flamfrosticboio/pygstudio',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "pygstudio": ['template.zip']
    },
    py_modules=['pygstudio'],
    install_requires=[
        'pygame',
        # may need to add more
    ],
    entry_points={
        'console_scripts': [
            'pygstudio = pygstudio.__main__:main',
        ],
    },
    classifiers=[
        # 'Programming Language :: Python :: 3',
        # 'License :: OSI Approved :: MIT License',   # disabled for now
        # 'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
