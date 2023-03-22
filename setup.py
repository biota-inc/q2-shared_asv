from setuptools import setup, find_packages

setup(
    name='q2-shared-asv',
    version='0.2.0',
    packages=find_packages(),
    entry_points={
        'qiime2.plugins': ['q2-shared-asv=q2_shared_asv.plugin_setup:plugin']
    },
    install_requires=[
        'qiime2',
    ],
    author='Ryo NIWA',
    author_email='ryo.niwa@cira.kyoto-u.ac.jp',
    description='A QIIME 2 plugin for shared ASV analysis',
    license='BSD-3-Clause',
    url='https://github.com/biota-inc/q2-shared_asv',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    package_data={  
        'q2_shared_asv': ['q2_shared_asv/*']
    },
    zip_safe=False,
)
