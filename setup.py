from distutils.core import setup
setup(
  name = 'ImPSCAD',         
  packages = ['ImPSCAD'],  
  version = '0.2',      
  license='MIT',
  description = 'Create a unique csv file from a out file from PSCAD/EMTDC simulations', 
  author = 'Luis Arthur Novais Haddad',
  author_email = 'luis.novais@engenharia.ufjf.br',
  url = 'https://github.com/LuisArthurNH',
  download_url = 'https://github.com/LuisArthurNH/ImPSCAD/archive/ImPSCAD_v_02.tar.gz',
  keywords = ['PSCAD', 'Variables', 'Import','.CSV','python','MATLAB'],
  install_requires=[            
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.8',
  ],
)