from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Django rest framework token authentication'
LONG_DESCRIPTION = 'An open source project created by a group of three just in case you want custom tokens'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="MM-JWT", 
        version=VERSION,
        author="Mahdi Musa Semnani, Mohammad Mahdi Nejati, Omidreza Nabavi",
        author_email="mahdi.2000musa@gmail.com, mmehdi2022@gmail.com, omidrezanabavi@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        # packages=find_packages(),
        install_requires=['pytz', 'djangorestframework', 'django'], # add any additional packages that 

        keywords=['django', 'rest framework', 'token', 'authentication'],
)