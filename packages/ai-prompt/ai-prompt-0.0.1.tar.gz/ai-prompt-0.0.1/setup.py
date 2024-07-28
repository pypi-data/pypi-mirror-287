from setuptools import setup

setup(
    name='ai-prompt',
    version='0.0.1',
    description='An Ai for command line',
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
    install_requires=['requests==2.32.3', 'prompt_toolkit==3.0.43', 'prompt_toolkit==3.0.43'],
    entry_points={
        'console_scripts': [
            'ai-prompt=ai:main',
        ],
    },
)
