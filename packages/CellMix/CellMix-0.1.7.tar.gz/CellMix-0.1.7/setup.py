from setuptools import setup, find_packages

setup(
    name='CellMix',  # The name of this package is CellMix
    version='0.1.7',  # 0.1.2 删除了库的需求中小于号的部分
    author='Tianyi Zhang, Zhiling Yan, Chunhui Li, Nan Ying, Yanli Lei, Shangqing Lyu, Yunlu Feng, Yu Zhao, '
           'Guanglei Zhang',
    author_email='zhang_tianyi@bii.a-star.edu.sg',  # Main Author Tianyi Zhang
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sagizty/CellMix',  # Github url
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python Version
    install_requires=[
        'torch>=1.9.0',
        'torchvision>=0.10.0',
        'numpy>=1.18.0',
        'scipy>=1.4.1',
        'matplotlib>=3.4.0',
        'Pillow>=8.0.0',
        'setuptools>=68.0.0'
        # All the requirements
    ],
)