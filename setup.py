from setuptools import setup 
setup(name='Mymacroprocessor',
      version='0.0.1',
      description='python file macro processor',
      author='nufeng',
      author_email='18478162@qq.com',
      requires= ['re'],
      url='https://github.com/nufeng1999/Mymacroprocessor/',
      download_url='https://github.com/nufeng1999/Mymacroprocessor/tarball/0.0.1',
      packages=['Mymacroprocessor'],
      keywords=['python', 'macro', 'processor', 'if','ifdef','ifndef','elif','else','endif','defined','define','undef'],
      license="apache 3.0",
      include_package_data=True
      )
