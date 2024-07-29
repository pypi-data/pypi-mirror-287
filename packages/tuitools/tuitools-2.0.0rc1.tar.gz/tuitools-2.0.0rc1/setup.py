from setuptools import setup, find_packages

# 定义包的元信息
setup(
    name='tuitools',
    version='2.0.0.rc1',
    packages=find_packages(),
    author='Paddy Hong',
    author_email='1707262291@qq.com',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown'
)