# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='school_management',
    version=version,
    description='Manages schools on QuickPay - students, dorms, classes, library, teachers',
    author='QuickPay',
    author_email='info@quickpay.co.ke',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
