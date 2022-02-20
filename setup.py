#---[Metadata]------------------------------------------------------#
#  Filename: setup.py                          [Update: 20-02-2022] #
#---[Info]----------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL} #
#                                                                   #
#  The setup of ODST                                                #
#  Language  ~  Python3                                             #
#---[Author]--------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                   #
#-------------------------------------------------------------------#


from setuptools import setup, find_packages
from time import sleep
print()
print("""
  /$$$$$$              /$$                      /$$$$$$$$                  /$$
 /$$__  $$            | $$                     |__  $$__/                 | $$
| $$  \__/  /$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$ | $$  /$$$$$$   /$$$$$$ | $$
|  $$$$$$  /$$__  $$|_  $$_/  | $$  | $$ /$$__  $$| $$ /$$__  $$ /$$__  $$| $$
 \____  $$| $$$$$$$$  | $$    | $$  | $$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$
 /$$  \ $$| $$_____/  | $$ /$$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$
|  $$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$/| $$$$$$$/| $$|  $$$$$$/|  $$$$$$/| $$
 \______/  \_______/   \___/   \______/ | $$____/ |__/ \______/  \______/ |__/
                                        | $$                                  
                                        | $$                                  
                                        |__/
""",end="")
print("========================= Welcome to the ODST setuptool. =========================")
sleep(1.2)
print()

requirements = ["requests"]

setup_requirements = ["requests"]

test_requirements = ["requests"]

setup(classifiers=[
        "Development Status                 :: 2 - Production/Stable",
        "Natural Language                   :: English (little french)",
        "Environment                        :: Console",
        "Intended Audience                  :: Developers",
        "License                            :: GNU-GPL-3.0",
        "Programming Language               :: Python :: 3.10",
        "Programming Language compatible    :: Python :: 3.2-3.10",
    ],
    name='OmegaDSToolkit',
    keywords="omegadstoolkit",
    description='A massive penetration testing toolkit',
    url='https://github.com/MyMeepSQL/OmegaDSToolkit',
    author='MyMeepSQL',
    author_email='thomas.pellissier@outlook.com',
    license='GNU-GPL-3.0',
    version='0.0.0.6',
    python_requires='>=3.3.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'progress', 'colored', 'nslookup', 'keyboard',
        'pythonping'
    ],
    zip_safe=False
)

print()
print("<=========================================================================================================================>")
print(' Done! All modules are install, now go to the OmegaDSTookit folder and start it with "python3 OmegaDSToolkit[v0.0.0.6].py"')
print("<=========================================================================================================================>")
