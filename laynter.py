import json


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


settings = {}
def read_data():
    global settings
    try:
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    except:
        settings ={
                "skin": "img.png",
                "money": 0
            }
def write_data():
    global settings
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)
    read_data()


app = QApplication([])

window = QWidget()
main_line = QVBoxLayout()
start_btn = QPushButton("Старт")
change_btn = QPushButton("Change")
skin_1 = QLabel("Картинка")
skin_1_img = QPixmap("optimys_prime/ufo.png")
skin_1_img = skin_1_img.scaledToWidth(64)
skin_1.setPixmap(skin_1_img)
buy_skin_1_btn = QPushButton("Купити скін")
line_edit = QLineEdit()

main_line = QVBoxLayout()
main_line.addWidget(line_edit)
main_line.addWidget(change_btn)
main_line.addWidget(start_btn)
main_line.addWidget(skin_1)

main_line.addWidget(start_btn)
main_line.addWidget(buy_skin_1_btn)

def buy_skin_1():
    read_data()
    if settings["money"] >=7:
        settings["money"] -= 7
        settings["skin"] = "asteroid.png"
        write_data()
    else:
        print("Грочей не хватає")

buy_skin_1_btn.clicked.connect(buy_skin_1)

def change_data():
    settings["skin"] = line_edit.text()
    write_data()

window.show()
app.exec()
