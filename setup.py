from setuptools import setup
setup(
    name='spring_struct',
    version='0.0.1',
    packages=['spring_struct'],
    entry_points={
        'console_scripts': [
            'spring_struct=spring_struct.spring_struct:main'
        ]
    },
    install_requires=['docopt']
    
)
