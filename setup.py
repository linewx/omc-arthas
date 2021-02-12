from setuptools import setup, find_packages
install_requires = [
    'omc>0.0.15'
]


setup(
    name='omc-arthas',
    version="0.0.1",
    description='ssh plugin for omc',
    license='MIT',
    author='Lu Ganlin',
    author_email='linewx1981@gmail.com',
    url='https://github.com/linewx/omc-arthas',
    packages=find_packages(),
    # package_data={'omc.config': ['*.yaml'], 'omc.lib': ['**', '**/*', '**/**/*']},
    install_requires=install_requires,
)