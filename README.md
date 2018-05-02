# aguaclara_research

[![Build Status](https://travis-ci.org/AguaClara/aguaclara_research.svg?branch=master)](https://travis-ci.org/AguaClara/aguaclara_research)
[![codecov.io](https://codecov.io/github/hbetts/orbitalpy/coverage.svg?branch=master)](https://codecov.io/github/AguaClara/aguaclara_research?branch=master)

This project contains code helpful to those conducting research for AguaClara. The functions included help to parse data from ProCoDA files and then analyze it. Additional scripts help to determine the correct stock concentrations, tubing, and other useful information for experimental setup.

## Installation

### Pip
You will probably want to install from pip, where we host the latest production package. If you downloaded Anaconda, you'll already have pip installed. The following is how to install with pip:
- If you'd like to install across your whole machine, you can open the cmd (Windows) or teminal (mac) and type ```$pip install aguaclara_research``` (where $ signifies the beginning of the command.) If you get a permission denied error, you probably want to install it instead to your particular user with ```$pip install aguaclara_research -U```.
- Once you've installed the package once, you can simply use: ```$pip install --upgrade aguaclara_research```. And if you don't want to update dependencies then use: ```$pip install --upgrade aguaclara_research --no-deps```.

### Installing as a developer
If you want to be able to edit the source code, you need to clone this repo with git, then go into the top level directory with pip: ```pip install . -U```. Now you should be able to import your local version of aguaclara_research into python: ```import aguaclara_research```.

## Contributing

Read [CONTRIBUTING](CONTRIBUTING.md).
