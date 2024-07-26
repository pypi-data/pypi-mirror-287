from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='message_to_request',
    version='0.0.3',
    author='abirukov',
    author_email='abirukov2008@yandex.ru',
    description='Библиотека для упаковки текста в http запрос',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "httpx",
    ],
    classifiers=[
        'Programming Language :: Python :: 3.12',
    ],
    project_urls={
        'GitHub': 'https://github.com/abirukov/message_to_request'
    },
    python_requires='>=3.10'
)
