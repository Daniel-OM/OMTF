from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'One Made\'s custom trading framework'
LONG_DESCRIPTION = 'This is a custom framework with all the code created by One Made for trading purposes.'

# Setting up
setup(
        name="tradingframework", 
        version=VERSION,
        author="One Made",
        author_email="dcaronm@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'trading'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)