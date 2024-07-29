import setuptools

setuptools.setup(
    name='s1292013_learn',
    version='2024.7.29.1',
    author='Abeez Ur Rehman',
    author_email='',
    description='This software is being developed at the University of Aizu, Aizu-Wakamatsu, Fukushima, Japan',
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url='https://github.com/AbeezUrRehman/s1292013_learn',
    license='GPLv3',
    install_requires=[            # All necessary packages utilized by our PAMI software
        'psutil',
        'pandas',
        'plotly',
        'matplotlib',
        'resource',
        'validators',
        'urllib3',
        'Pillow',
        'numpy',
        'sphinx',
        'sphinx-rtd-theme',
        'validators',
        'discord.py',
        'networkx',
        'deprecated',
    ],
    extras_require={
        'gpu':  ['cupy', 'pycuda'],
        'spark': ['pyspark'],
        'dev': ['twine', 'setuptools', 'build'],
        'all': ['cupy', 'pycuda', 'pyspark', 'twine', 'setuptools', 'build']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)