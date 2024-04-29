from cx_Freeze import setup, Executable

setup(
    name='shake',
    version='1.0',
    description='check earthquake',
    executables=[Executable('main.py')]
)
