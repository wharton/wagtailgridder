from setuptools import setup, find_packages

setup(
    name='wagtailgridder',
    version="0.9.4",
    description='Gridder layout for the Django CMS Wagtail.',
    long_description='',
    author='Timothy Allen',
    author_email='tallen@wharton.upenn.edu',
    url='https://github.com/wharton/wagtailgridder',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'wagtail>=1.9,<1.10',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
