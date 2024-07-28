from setuptools import setup, find_packages

setup(
    name='packag66e',
    version='0.1.0',
    packages=find_packages(include=['packag66e', 'packag66e.*']),
    install_requires=[],
    url='https://github.com/yourusername/packag66e',  # 替换为实际的URL
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple example package named packag66e',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.7',
)
