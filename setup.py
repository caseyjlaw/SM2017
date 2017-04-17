from distutils.core import setup

setup(name='SM2017',
      version='0.0',
      description='Scattering',
      author='Paul Hancock',
      author_email='hancock@physics.usyd.edu.au',
      packages=['SM2017'],
      data_files=[('include', ['data/Halpha_map.fits', 'data/Halpha_error.fits'])]
     )
