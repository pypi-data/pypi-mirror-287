from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
	Extension(
		"imagingai.ImagingAI",  # Module name
		["imagingai/ImagingAI.c"],  # Source file
	)
]

cythonize_options = {
	'compiler_directives': {
		'language_level': 3,
		'emit_code_comments': False,
	}
}

setup(
	name='imagingai',
	version='2.96',
	description='EKY Imaging AI Package',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='ImagingAI',
	author_email='license@mit.edu',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
	python_requires='>=3.6',
	install_requires=[
		'requests',
		'cryptography',
	],
	ext_modules=cythonize(extensions, **cythonize_options),
	packages=['imagingai'],
	include_package_data=True,
	package_data={
		'imagingai': [
			'extensions/*.so',  # Placeholder for any .so files in the future
		],
	},
)