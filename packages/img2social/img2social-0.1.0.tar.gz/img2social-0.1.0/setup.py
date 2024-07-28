from setuptools import setup, find_packages

setup(
    name='img2social',
    version='0.1.0',
    description='Create engaging images for socials quicker.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='dodo',
    author_email='dodothedeveloper@gmail.com',
    url='https://github.com/dodothedeveloper/img2social',
    packages=find_packages(),  # Automatically find your packages
    install_requires=[ ],
    entry_points={
        'console_scripts': [
            'img2social=file:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
