from setuptools import setup, find_packages

setup(
        name='cliologging', # How you named your package folder
        packages=find_packages(include=['cliologging']), # Chose the same as "name"
        version='1.0', # Start with a small number and increase it with every change you make
        license='None', # Chose a license from here: https://help.github.com/articles/licensing-a-repository
        description='Add-on to the official Python logging library.', # Give a short description about your library
        author='Julien BALDERIOTTI', # Type in your name
        author_email='julien.blt@outlook.com', # Type in your E-Mail
        url='https://github.com/julienbltt/cliologging.git', # Provide either the link to your github or to your website
        download_url='https://github.com/julienbltt/cliologging/archive/refs/tags/v1.0.tar.gz',
        keywords=['LOGGING', 'LOG', 'LOGGER'], # Keywords that define your package best
        install_requires=[],
        classifiers=[
                'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
                'Intended Audience :: Developers',      # Define that your audience are developers
                'Topic :: Software Development :: Build Tools',
                'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
                'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
                'Programming Language :: Python :: 3.9',
                'Programming Language :: Python :: 3.10',
                'Programming Language :: Python :: 3.11',
        ],

        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        test_suite='tests',
)
