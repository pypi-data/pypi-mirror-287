from setuptools import setup,find_packages

setup(
    name='BL_TTS',
    version='0.1',
    author='Broken Leaf',
    description='This is a very advanced Text To Speech program created by Broken Leaf...',
)
packages = find_packages()
install_requires = ['requests', 'playsound', 'tempfile', 'os', 'typing']