import tkinter as tk
import tkinter.filedialog as fd
import os

root = tk.Tk()
files = list(fd.askopenfilenames(parent=root, title='Choose files'))

working_dir = os.path.dirname(os.path.realpath(__file__))
for d in files:
    with open(d, 'r') as f:
        content = f.readlines()
    d = d.split('.')[0]
    with open(f'{d}.txt', 'w') as w:
        w.writelines(content)
    os.system(f'java -jar plantuml-1.2025.4.jar -tpdf {d}.txt')
    os.system(f'rm {d}.txt')
    filename = d.split('/')[-1]
    #os.system(f'mv {d}.pdf {working_dir}/{filename}.pdf')
