# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['pyaes256/__main__.py'],
             pathex=['/home/crocop/projects/The-Crocop/pyhashing'],
             binaries=[],
             datas=[('pyaes256/templates/*', 'pyaes256/templates' )],
             hiddenimports=["tinycss2", "cairocffi", "weasyprint", "pyphen", "cairosvg"],
             hookspath=["pyinstaller_hooks"],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='pyaes256',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='__main__')
