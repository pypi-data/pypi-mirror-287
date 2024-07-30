from setuptools import setup, find_packages

setup(
    name='rsyslog_client_assistant',
    version='0.1.4',
    description='Generate client-side configuration for rsyslog',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Titas Majumder',
    author_email='titas20031996@gmail.com',
    url='https://github.com/titas2003/rsyslog_client_assist.git', 
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        # Add any dependencies here
    ],
    include_package_data=True,
)
