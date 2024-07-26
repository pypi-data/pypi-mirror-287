from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='spider_cloud_cos',
    version='5.1.9.32',
    description='文件云存储连接',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
    author='xfc',
    packages=find_packages(),
    url='https://gitlab.zhuanspirit.com/xiefengcheng/spider_cloud_cos',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7',
)