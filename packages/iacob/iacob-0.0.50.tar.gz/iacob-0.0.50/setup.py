from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="iacob",
    version="0.0.50",

    description="Development of an interactive brain connectivity data mining tool",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Thibaud SCRIBE, Enzo CREUZET",
    author_email="thibaud.scribe@etu.univ-tours.fr, enzo.creuzet@etu.univ-tours.fr",
    url="https://scm.univ-tours.fr/projetspublics/lifat/iacob",
    
    python_requires='>=3.8, <=3.12',
    install_requires=[
        'PyQt5>=5.15.10,<5.16.0',
        'matplotlib>=3.6.0,<=3.9.1',
        'networkx>=3.0,<=3.3.0',
        'scipy>=1.9.0,<=1.14.0',
        'pyqtgraph>=0.13.0,<0.14.0',
        
    ],

    packages=find_packages(),
    include_package_data=True,
    package_data={
        'iacob': ["resources/*", 
                  "resources/images/*"],
        '': ["requirements.txt"],
    },
    
    entry_points={
        'console_scripts': [
            'iacob-app=iacob.src.IACOB:run_app',
        ],
    },
)