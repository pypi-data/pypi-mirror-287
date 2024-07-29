from setuptools import setup, find_packages

setup(
    name="envsync",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'envsync=envsync.cli:main',
        ],
    },
    author="Pak Kin LAU",
    author_email="pakkinlau.general@gmail.com",
    description="A tool to set up Git hooks for your target local git repo, that automatically synchronize and updates for requirements.txt and virtual environments, streamlining the process of managing development environment for projects.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/pakkinlau/envsync",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)