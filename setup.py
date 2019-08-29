from setuptools import setup
setup(
    name='oxford_dic',
    version='0.0.1',
    packages=['oxford_dic'],
    author="Michal Polovka",
    entry_points={
        'console_scripts': [
            'oxford_dic = oxford_dic.__main__:main'
         ]
    })
