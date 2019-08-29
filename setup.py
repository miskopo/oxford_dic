from setuptools import setup\n
setup(
    name='oxford_dic',
    version='0.0.1',
    packages=['oxford_dic'],
    entry_points={
        'console_scripts': [
            'oxford_dic = oxford_dic.__main__:main'
         ]
    })
