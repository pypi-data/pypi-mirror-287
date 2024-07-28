from setuptools import setup, find_packages

setup(
    name='packag88e',
    version='0.1.0',
    packages=find_packages(include=['packag88e', 'packag88e.*']),
    install_requires=[],
    url='https://github.com/yourusername/packag88e',  # 替换为实际的URL
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple example package named packag88e',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.7',
)
