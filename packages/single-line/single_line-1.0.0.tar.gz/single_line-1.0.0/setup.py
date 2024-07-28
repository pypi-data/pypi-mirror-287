#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'single-line',
        version = '1.0.0',
        description = 'A context manager to facilitate printing messages to the same line',
        long_description = "# single-line\n[![build](https://github.com/soda480/single-line/actions/workflows/main.yml/badge.svg)](https://github.com/soda480/single-line/actions/workflows/main.yml)\n[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://pybuilder.io/)\n[![complexity](https://img.shields.io/badge/complexity-A-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)\n[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)\n[![python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-teal)](https://www.python.org/downloads/)\n\nA context manager to facilitate printing messages to the same line. \n\n## Installation\n```bash\npip install single-line\n```\n\n## Usage\n\nUsing the `SingleLine` context manager all calls to its `print` method will print the message to the same line. A common use case will be to use it in conjuction with a for loop as follows.\n\n```Python\nfrom time import sleep\nfrom faker import Faker\nfrom single_line import SingleLine\n\nwith SingleLine() as line:\n    for _ in range(25):\n        line.print(Faker().sentence())\n        sleep(.15)\n```\n\n![example1](https://raw.githubusercontent.com/soda480/single-line/main/docs/images/example1.gif)\n\n\nSetting `message_when_done` parameter will print a prescribed message when the context is done. The `print` method also supports printing colored messages via the [colorama](https://pypi.org/project/colorama/) module, just pass the method an optional `color` parameter consiting of a dictionary describing the `fore`, `back` and `style` you wish to the message to be printed with.\n\n```Python\nfrom time import sleep\nfrom faker import Faker\nfrom colorama import Fore\nfrom single_line import SingleLine\n\nwith SingleLine(message_when_done='done') as line:\n    for _ in range(25):\n        line.print(Faker().sentence(), color={'fore': Fore.YELLOW})\n        sleep(.15)\n\n```\n\n![example2](https://raw.githubusercontent.com/soda480/single-line/main/docs/images/example2.gif)\n\nBy default messages will be printed out to `sys.stdout` but you can print to any object with a write(string) method. This example also shows the extent of using colors when printing messages.\n\n```Python\nimport sys\nimport random\nfrom time import sleep\nfrom faker import Faker\nfrom single_line import SingleLine\nfrom colorama import Fore, Back, Style\n\ndef get_random_fore():\n    return random.choice([Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])\n\ndef get_random_back():\n    return random.choice([Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE])\n\ndef get_random_style():\n    return random.choice([Style.NORMAL, Style.DIM, Style.BRIGHT])\n\nwith SingleLine(stream=sys.stderr) as line:\n    for _ in range(25):\n        line.print(Faker().sentence(), color={'fore': get_random_fore(), 'back': get_random_back(), 'style': get_random_style()})\n        sleep(.15)\n```\n\n![example3](https://raw.githubusercontent.com/soda480/single-line/main/docs/images/example3.gif)\n\nYou can also use the `SingleLine` context manager to display messages when executing [asyncio](https://docs.python.org/3/library/asyncio.html) methods.\n\n```Python\nimport asyncio\nimport random\nfrom faker import Faker\nfrom single_line import SingleLine\n\nasync def do_some_work(worker, fake, line):\n    for index in range(random.randint(10, 35)):\n        await asyncio.sleep(random.choice([.5, .1, .25]))\n        line.print(f'worker{worker} {fake.sentence()}')\n\nasync def run(line):\n    await asyncio.gather(*(do_some_work(worker, Faker(), line) for worker in range(5)))\n\nwith SingleLine(message_when_done='done with asyncio') as line:\n    asyncio.run(run(line))\n```\n\n![example4](https://raw.githubusercontent.com/soda480/single-line/main/docs/images/example4.gif)\n\n## Development\n\nClone the repository and ensure the latest version of Docker is installed on your development server.\n\nBuild the Docker image:\n```sh\ndocker image build \\\n-t single-line:latest .\n```\n\nRun the Docker container:\n```sh\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\nsingle-line:latest \\\nbash\n```\n\nExecute the build:\n```sh\npyb -X\n```\n",
        long_description_content_type = 'text/markdown',
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12'
        ],
        keywords = '',

        author = 'Emilio Reyes',
        author_email = 'soda480@gmail.com',
        maintainer = '',
        maintainer_email = '',

        license = 'Apache License, Version 2.0',

        url = 'https://github.com/soda480/single-line',
        project_urls = {},

        scripts = [],
        packages = ['single_line'],
        namespace_packages = [],
        py_modules = [],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'colorama',
            'cursor'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
