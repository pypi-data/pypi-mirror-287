from setuptools import setup, find_packages

setup(
    name='delshice2',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'delshice2 = delshice2:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package that waits for 5 minutes, returns a value, and uninstalls itself.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/self_deleting_package',  # 你的项目主页
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
