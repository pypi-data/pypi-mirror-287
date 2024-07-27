import setuptools

setuptools.setup(
    name='weekly-customer-metrics',
    version='1.0',
    url='https://gitlab.com/landsend/dpe/analytics/weekly_customer_metrics',
    author='LEINTERNAL\nmdeshi',
    author_email='neeraj.deshingkar@landsend.com',
    description='This project contains code related to weekly-customer-metrics.',
    packages=setuptools.find_packages(exclude=['*tests*']),
    python_requires='~=3.10',
    zip_safe=False,
    include_package_data=True
    )
