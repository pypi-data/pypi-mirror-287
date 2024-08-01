from setuptools import setup

setup(
    name='ryouDemo',
    version='0.0.1',
    description='A demo package for Ryou',
    packages=['ryouDemo'],#需要打包的包名
    py_modules=['Tool'],#需要打包的模块名
    author='Jeff Kafka',
    author_email='qaqnoname@163.com',
    long_description=open('./README.md').read(),
    url='https://space.bilibili.com/354814866?spm_id_from=333.1007.0.0',
    install_requires=[],
    license='MIT'
)
