from setuptools import setup

setup(
    name='sizescan',
    version='0.1.2',
    description="SizeScan is a script that displays the sizes of subfolders or files within a specified folder. It highlights items in red if they exceed a specified size limit.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='hasan',
    author_email='hasanfq818@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['tqdm==4.63.0', 'argparse==1.4.0'],
    entry_points={
        'console_scripts': [
            'sizescan=sizescan:main',
        ],
    },
)