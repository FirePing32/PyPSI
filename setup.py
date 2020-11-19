from setuptools import setup

setup(
    name="PyPSI",
    version='1.0.0',
    description='CLI + API for Google PageSpeed Insights',
    url='https://github.com/prakhargurunani/PyPSI',
    author='Prakhar Gurunani',
    author_email='prakhargurunani@gmail.com',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='cli, google, python, seo, page-speed-insights, performance, google-apis',
    python_requires='>=3.5, <4',
    py_modules=['psi'],
    install_requires=[
        'click',
        'urllib3'
    ],
    entry_points='''
        [console_scripts]
        psi=main:psi
    ''',
)