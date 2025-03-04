import sys
from cx_Freeze import setup, Executable

# Include the obfuscated files
include_files = [
    ("bot_project/obfuscated", "obfuscated"),
    ("bot_project/obfuscated/util_py_files", "obfuscated/util_py_files")
]

build_exe_options = {
    "packages": [],
    "include_files": include_files,
    "excludes": ["tkinter", "unittest"]
}

bdist_msi_options = {
    "upgrade_code": "{12345678-ABCD-1234-ABCD-1234567890AB}",
    "add_to_path": False,
    "install_icon": None
}

target = Executable(
    script="bot_project/__main__.py",
    base="Console",
    target_name="bot_calculator.exe"
)

setup(
    name="Bot Calculator",
    version="1.0",
    description="A simple calculator with obfuscated logic",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options
    },
    executables=[target]
)
