from distutils.core import setup
setup(
  name = 'kingdroid',         # How you named your package folder (MyLib)
  packages = ['kingdroid'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'You can use all services of tts using this library in android',   # Give a short description about your library
  author = 'KING',                   # Type in your name
  author_email = 'mohitnarwani673@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/KINGMOHIT',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/KINGMOHIT/kingdroid',    # I explain this later on
  keywords = ['tts', 'android', 'python'],   # Keywords that define your package best
  
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3'
  ],
)
