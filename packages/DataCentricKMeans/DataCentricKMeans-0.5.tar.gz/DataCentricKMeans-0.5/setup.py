from setuptools import setup, find_packages

setup(
    name='DataCentricKMeans',
    version='0.5', 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Gereken diğer paketler
    ],
    package_data={
        'DataCentricKMeans': ['DataCentricKMeans_universal.out','DataCentricKMeans_linux.out','DataCentricKMeans_windows.exe'],
    },
    entry_points={
        'console_scripts': [
            
        ],
    },
    author="Vasfi Tataroglu, Parichit Sharma, Hasan Kurban, and Mehmet M. Dalkilic",
    author_email="vtatarog@iu.edu",
    description="A package for running DataCentricKMeans.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/brainvs/DataCentricKMeansPython",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
