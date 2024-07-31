# $Id: setup.py 7518 2023-05-16 13:24:46Z brideout $

from setuptools import setup

setup(name="madrigalWeb",
      version="1.0",
      description="Remote Madrigal Python API",
      author="Bill Rideout",\
      author_email="wrideout@haystack.mit.edu",
      url="http://www.haystack.mit.edu/~brideout/",
      packages=["madrigalWeb"],
      scripts=['downloadCedarAsciiGps.py'])