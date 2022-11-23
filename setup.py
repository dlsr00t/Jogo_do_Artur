import cx_Freeze

executables = [cx_Freeze.Executable('labirinto1.py')]

cx_Freeze.setup(
    name="labirinto",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['assets', 'variaveis.py']}},

    executables = executables
    
)