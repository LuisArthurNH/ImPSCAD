from distutils.core import setup
setup(
  name = 'ImPSCAD',         
  packages = ['ImPSCAD'],  
  version = '0.1',      
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Import variables from a PSCAD/EMTDC simulation', 
  author = 'Luis Arthur Novais Haddad',
  author_email = 'luis.novais@engenharia.ufjf.br',
  url = 'https://github.com/LuisArthurNH',
  download_url = 'https://github.com/LuisArthurNH/ImPSCAD/archive/v_01.tar.gz',
  keywords = ['PSCAD', 'Variables', 'Import','.CSV','python','MATLAB'],
  install_requires=[            
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.8',
  ],
)