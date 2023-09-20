from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='StarClusterPlot',
    version='0.1.9',
    description='Python package for visualizing star clusters and their Hertzsprung-Russell diagrams',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Teerat Chanromyen',
    author_email='teerat.nahm@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Astronomy',
    packages=find_packages(),
    install_require=['matplotlib'],
    extras_require={
        "dev": ["twine>=4.2.0"],
    }
)