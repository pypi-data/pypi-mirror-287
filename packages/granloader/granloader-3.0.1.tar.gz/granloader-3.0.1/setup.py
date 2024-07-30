from setuptools import setup, find_packages

setup(
	name='granloader',
    version='3.0.1',
	packages=find_packages(),
	install_requires=[
		'yt-dlp==2023.12.30',
		'ffmpeg-python==0.2.0',
		'ffmpeg==1.4',
    'requests',
	],
	entry_points={
        'console_scripts': [
            'granloader=fast_downloads.app:main'
		]
	}
)