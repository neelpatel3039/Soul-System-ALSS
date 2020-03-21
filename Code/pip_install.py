def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

def main():
    install_and_import('transliterate')
    install_and_import('numpy')
    install_and_import('autoit')
    install_and_import('subprocess')
    install_and_import('time')
    install_and_import('os')
    install_and_import('cv2')
    install_and_import('openpyxl')
    install_and_import('PIL')
    install_and_import('tkinter')
    install_and_import('png')
    install_and_import('pyotp')
    install_and_import('threading')
    install_and_import('math')
    install_and_import('scipy.ndimage')
    install_and_import('scipy')


if __name__ == "__main__":
    main()

