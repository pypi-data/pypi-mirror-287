from setuptools import setup, find_packages

setup(
    name='vridgeai',
    version='0.0.4',
    description='vridgeai python package',
    author='byungchan',
    author_email='bgk@vazilcompany.com',
    url='https://git.vazil.me/byungchan/vridgeai-python-package.git',
    install_requires=['numpy', 'tensorflow', 'matplotlib'],
    packages=find_packages(exclude=['tensorflow']),
    keywords=['vazil', 'vazilcompany', 'vridge', 'vridgeai'],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
