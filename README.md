# clipboard-monitor
This Python script monitors the system clipboard in real time. It shows the new text copied to the terminal, as well as the date and time of the copy. The script also provides the ability to save all copies of text during execution to a file in TXT format.

[![Python Version](https://img.shields.io/badge/python-3.9.7-blue.svg)](https://www.python.org/downloads/release/python-3.9.7/)

## Features
- Displays new copied texts in real time in the terminal.
- Saves all text copies during execution to a TXT file.

---

## How to use it ?

### Clone the repository :
```bash
git clone https://github.com/mselek/clipboard-monitor.git  
```

### Navigate to the project directory :
```bash
cd clipboard-monitor
```

### Install dependencies :
```bash
pip install -r requirements.txt
```

### Run the script : 
```bash
python main.py
```

---

## FAQ

### Why is the newly copied text not displayed in my terminal ?
New copies may not appear directly in the terminal.
Make sure **NOTHING** is selected in the terminal when copying the new text and that **no cursor** from clicking in this window is present in the terminal.
If you encounter this problem, give focus to the terminal by clicking on the window and pressing the "Esc" key, the text will display again in the terminal.


### On which system can I use this script ?
Currently this script works on Windows only

---

## Demo
![GIF](https://github.com/mselek/clipboard-monitor/blob/main/demo.gif)
> Font used in terminal : Consolas, 14pt, bold text

---

## Authors
- [@mselek](https://www.github.com/mselek)