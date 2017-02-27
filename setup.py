# думаю стоит почитать какие статьи, как правильно это делать.  

from setuptools import setup
# Вероятно setuptools предварительно следует установить?

setup(
    name='mega-math', 
    # хотя пакет с подчеркиванием, пишется по традиции с дефисом.
    version='1.0.0'.
    descriptions='collection of mathematical formul',
    url='https://github/..',
    license='Apache License 2.0',
    author='username',
    author_email='username@gmail.com',
    packages=['mega_math'],
#   pymodules=[]
   #scripts=[]  # запускаемые из комстроки пути
   # install_requires=[
   #    'django>=1.10'
   #    'PyQt5
   # ] 
   # 

)
