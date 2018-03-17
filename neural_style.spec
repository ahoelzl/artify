# -*- mode: python -*-

block_cipher = None


a = Analysis(['neural_style.py'],
             pathex=['/home/radhuslanteg/programming/dapp-challenge/artify/neural-style-tf'],
             binaries=[],
             datas=[],
             hiddenimports=['tensorflow.contrib', 'scipy._lib.messagestream', 'scipy.misc.doccer', 'scipy', 'scipy.io' ,'scipy.io.loadmat'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='neural_style',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='neural_style')
