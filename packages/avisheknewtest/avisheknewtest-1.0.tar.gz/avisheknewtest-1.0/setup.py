from setuptools import setup, find_packages
setup(
    name='avisheknewtest',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        #Add dependencies here.
        #'flask<=0.5',
    ],
    entry_points={
        "console_scripts": [
            "avisheknewtest = avisheknewtest:hello",
        ],
    },
)
