# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['jarvis.py'],
             pathex=['G:\\Shivam\\Coding\\Python\\Projects\\Jarvis'],
             binaries=[],
             datas=[('C:\\Users\\dell\\AppData\\Roaming\\Python\\Python37\\site-packages\\eel\\eel.js', 'eel'), ('GUI', 'GUI'), ('Resources', 'Resources'), ('GUI', 'GUI')],
             hiddenimports=['bottle_websocket', 'pyttsx3.drivers', 'pyttsx3.drivers.dummy', 'pyttsx3.drivers.espeak', 'pyttsx3.drivers.nsss', 'pyttsx3.drivers.sapi5'],
             hookspath=[],
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
          name='jarvis',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='G:\\Icons\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='jarvis')
