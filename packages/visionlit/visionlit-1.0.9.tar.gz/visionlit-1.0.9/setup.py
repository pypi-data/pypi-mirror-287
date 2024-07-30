from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

import os

# Define extensions to compile using absolute paths
base_path = os.path.abspath(os.path.dirname(__file__))
extensions = [
    Extension("visionlit.main", [ "visionlit/main.c"]),
    Extension("visionlit.utils.utils", [ "visionlit/utils/utils.c"]),
]


setup(
    name='visionlit',
    version='1.0.9',
    author='Jessica Nono',
    author_email='jessicanono@filparty.com',
    description='A Python library implementing Visionlit computer vision methods with model access.',
    long_description=open('README.md').read(),
    ext_modules=cythonize(extensions),
    packages=find_packages(),
    zip_safe=False,
    package_data={
        'visionlit': ['*.so', '*.pyd', '__init__.py'],
        'visionlit.utils': ['__init__.py'],
        # Include other directories if necessary
    },
    long_description_content_type='text/markdown',
    url='https://github.com/jessicaNono/visionlitpy',
    include_package_data=True,
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
      "console_scripts":[
           'visionlit=visionlit.main:main'
      ],
    },
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/jessicaNono/visionlitpy/docs',
        'Source': 'https://github.com/jessicaNono/visionlitpy',
    },
)

