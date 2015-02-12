from setuptools import setup

dependecies = [
	"feedparser",
    "beautifulsoup4",
    "requests"
]

setup(
	name = "scavenge",
	verison = "0.0.1",
	install_requires=dependecies
)