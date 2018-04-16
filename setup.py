from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='wagtailgridder',
    version="0.9.28",
    description='Gridder layout for the Django CMS Wagtail.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Timothy Allen',
    author_email='tallen@wharton.upenn.edu',
    url='https://github.com/wharton/wagtailgridder',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'wagtail>=1.9',
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
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
