from setuptools import setup

setup(
    author='User',
    author_email='example@mail.com',
    name='limingggTEA',
    version='0.0.1',
    description='A simple package for https://app.tea.xyz/. Example tea-xyz1 - https://github.com/madest92/tea-xyz1 and tea-xyz2 - https://github.com/madest92/tea-xyz2',
    url='https://github.com/liminggg/tea',
    project_urls={
        'Homepage': 'https://github.com/liminggg/tea',
        'Source': 'https://github.com/liminggg/tea',
    },
    py_modules=['hi_tea'],
    entry_points={
        'console_scripts': [
            'hi-tea=hi_tea:hello_tea_xyz'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        'tea-xyz1',
        'tea-xyz2',
        # add your projects
    ],
)
