from setuptools import setup, find_packages

setup(
    name='KN_TTS',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'KN_TTS': [
            '2nd.html',
            'static/*.js',
        ],
    },
    install_requires=[
        'selenium',
        'webdriver-manager',
    ],
    entry_points={
        'console_scripts': [
            'kn_tts=KN_TTS.__init__:listen',
        ],
    },
    author='Koushik Nath',
    author_email='koushiknath003@gmail.com',
    description='This is a Speech to Text package Created by Koushik Nath',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11.4',
)
