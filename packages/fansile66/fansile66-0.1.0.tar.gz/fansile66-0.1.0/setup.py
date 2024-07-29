from setuptools import setup, find_packages

setup(
    name='fansile66',
    version='0.1.0',
    author='你的名字',
    author_email='你的邮箱@example.com',
    description='一个描述你的包的简短说明',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mypackage',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
