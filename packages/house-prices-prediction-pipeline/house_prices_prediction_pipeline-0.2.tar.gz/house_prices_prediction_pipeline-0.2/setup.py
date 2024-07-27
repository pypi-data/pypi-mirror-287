from setuptools import setup, find_packages

setup(
    name='house_prices_prediction_pipeline',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'joblib',
        'scikit-learn'
    ],
    description='A package for house price prediction pipeline.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Saad Khalid',
    author_email='tosaadkhalid@gmail.com',
    url='https://github.com/saadkhalid-git/house_price_prediction_pipeline',
    license='MIT',
)