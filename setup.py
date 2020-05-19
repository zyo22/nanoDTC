VERSION = (0, 0, 0)
VERSION = '.'.join(map(str, VERSION))


DESCRIPTION = 'nanodemo'
CLASSIFIERS = [
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python',
]

REQUIREMENTS = []
with open("nanodemo/requirements.txt") as f:
    for line in f.readlines():
        line = line.partition('#')[0]
        line = line.rstrip()
        if not line:
            continue

        REQUIREMENTS.append(line)


PACKAGES = [
    'nanodemo',
]

DATA = {'nanodemo': ['requirements.txt', 'test.txt']}


def main():
    from setuptools import setup

    options = {
        'name': 'nanodemo',
        'version': VERSION,
        'author': 'Ryan',
        'author_email': 'rdg31@cam.ac.uk',
        'description': DESCRIPTION,
        'classifiers': CLASSIFIERS,
        'packages': PACKAGES,
        'entry_points': {
            'console_scripts': ['nanodtc=nanodemo.main:main']
        },
        'install_requires': REQUIREMENTS,
        'package_data': DATA,
    }

    setup(**options)


if __name__ == '__main__':
    main()
