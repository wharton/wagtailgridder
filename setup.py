from setuptools import setup, find_packages

setup(
    name='wagtailgridder',
    version="0.9",
    description='Gridder layout for the Django CMS Wagtail.',
    long_description='',
    author='Timothy Allen',
    author_email='tallen@wharton.upenn.edu',
    url='https://stash.wharton.upenn.edu/projects/WRDSWEB/repos/django-backtester/browse',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'wagtail>=1.8,<1.9',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)
