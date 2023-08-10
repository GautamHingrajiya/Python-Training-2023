from cx_Freeze import setup,Executable,sys
includefiles=['G.ico']
excludes=[]
packages=[]
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "Billing System",
     "TARGETDIR",
     "[TARGETDIR]\Billing_GUI.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="09.08.23",
    description="Billing System",
    author="faizan Khan",
    name="Billing System",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="Billing_GUI.py",
            base=base,
            icon='G.ico',
        )
    ]
)