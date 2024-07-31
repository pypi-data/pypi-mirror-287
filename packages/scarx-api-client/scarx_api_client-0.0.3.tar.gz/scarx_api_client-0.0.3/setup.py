from setuptools import setup

setup(
   name='scarx_api_client',
   version='0.0.3',
   description='Client for Scarx API',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   author='Scartz',
   author_email='github@scarx.net',
   packages=['scarx_api_client'],
   install_requires=['grpclib', 'betterproto'],
)
