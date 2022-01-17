#---[Metadata]-----------------------------------------------------#
#  Filename: setup.py                         [Update: 17-01-2022] #
#---[Info]---------------------------------------------------------#
#  The setup for had all modules that the ODST use                 #
#  Language      - Python3                                         #
#---[Author]-------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                  #
#------------------------------------------------------------------#

from setuptools import setup, find_packages
from time import sleep
print()
print("""  /$$$$$$              /$$                      /$$$$$$$$                  /$$
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
print("================== Welcome to the ODST modules verification. ==================")
sleep(1.2)
print("                 Checking if the ODST modules are installed...    ")
sleep(0.6)
print()
setup(name='OmegaDSToolkit',
      version='0.0.0.6',
      description='A massive penetration testing toolkit',
      url='https://github.com/MyMeepSQL/OmegaDSToolkit',
      author='MyMeepSQL',
      author_email='thomas.pellissier@outlook.com',
      license='GNU-GPL-3.0',
      python_requires='>=3.3.0',
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          "console_scripts": [
                "odst = OmegaDSToolkit:main"
          ]
      },
      install_requires=[
          'progress', 'colored', 'nslookup', 'keyboard',
          'pythonping'
      ],
      zip_safe=False
)
print()
print("<========================================================================================================================>")
print(' Done! All modules are install, now go to the OmegaDSTookit folder and start it with "python OmegaDSToolkit[v0.0.0.6].py"')
print("<========================================================================================================================>")
input("Press [ENTER] key to continue")
