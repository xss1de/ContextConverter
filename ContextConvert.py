def ToPNG(filenames, params):
    import ctypes
    from PIL import Image
    import os

    for file in filenames:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp')):
            img = Image.open(file)

            dir = os.path.dirname(file)
            namew = os.path.basename(file)
            name = os.path.splitext(namew)[0]

            img.save(dir + '\\' + name + '.png')
        else:
            ctypes.windll.user32.MessageBoxW(0, f"The file is not an image.\n({file})", "Error", 1)

def ToJPEG(filenames, params):
    import ctypes
    from PIL import Image
    import os

    for file in filenames:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp')):
            img = Image.open(file)

            dir = os.path.dirname(file)
            namew = os.path.basename(file)
            name = os.path.splitext(namew)[0]

            img.save(dir + '\\' + name + '.jpeg')
        else:
            ctypes.windll.user32.MessageBoxW(0, f"The file is not an image.\n({file})", "Error", 1)

def ToSVG(filenames, params):
    import ctypes
    from PIL import Image
    import os

    for file in filenames:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp')):
            img = Image.open(file)

            dir = os.path.dirname(file)
            namew = os.path.basename(file)
            name = os.path.splitext(namew)[0]

            img.save(dir + '\\' + name + '.svg')
        else:
            ctypes.windll.user32.MessageBoxW(0, f"The file is not an image.\n({file})", "Error", 1)

def ToWEBP(filenames, params):
    import ctypes
    from PIL import Image
    import os

    for file in filenames:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp')):
            img = Image.open(file)

            dir = os.path.dirname(file)
            namew = os.path.basename(file)
            name = os.path.splitext(namew)[0]

            img.save(dir + '\\' + name + '.webp')
        else:
            ctypes.windll.user32.MessageBoxW(0, f"The file is not an image.\n({file})", "Error", 1)

if __name__ == '__main__':
    from context_menu import menus
    cm = menus.ContextMenu('Конвертировать', type='FILES')

    cm.add_items([
        menus.ContextCommand('PNG', python=ToPNG),
        menus.ContextCommand('JPEG', python=ToJPEG),
        menus.ContextCommand('SVG', python=ToSVG),
        menus.ContextCommand('WEBP', python=ToWEBP)
    ])
    cm.compile()