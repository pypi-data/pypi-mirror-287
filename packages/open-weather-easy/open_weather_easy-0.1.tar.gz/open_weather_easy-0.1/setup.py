from setuptools import setup, find_packages

setup(
    name='open_weather_easy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Radin Abdorazaghi',
    author_email='your_email@example.com',
    description='A simple library to use OpenWeatherMap API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/open_weather_easy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
