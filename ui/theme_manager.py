

light_theme = """
QWidget {
    background-color: #ffffff;
    color: #000000;
}

QPushButton {
    background-color: #ffffff;
    color: #052f57;
    font-size: 16px;
    border: 2px solid #6fb8fc;
    border-radius: 5px;
    padding: 10px;
}

QPushButton:hover{
    background-color: #6fb8fc;
    color: white;
    border: 2px solid #ffffff;

}

QPushButton:disabled {
    background-color: #f0f0f0;
    color: #aaaaaa;
    font-size: 16px;
    border: 2px solid #cccccc;
    border-radius: 5px;
    padding: 10px;
}

QLabel {
    font-family: "Segoe UI";
    font-size: 14px;
}
"""

dark_theme = """
QWidget {
    background-color: #121212;
    color: #eeeeee;
}

QPushButton {
    background-color: #333333;
    color: #ffffff;
    font-size: 16px;
    border: 2px solid #6fb8fc;
    border-radius: 5px;
    padding: 10px;
}

QPushButton:hover{
    background-color: #6fb8fc;
    color: white;
    border: 2px solid #ffffff;

}

QPushButton:disabled {
    background-color: #f0f0f0;
    color: #aaaaaa;
    font-size: 16px;
    border: 2px solid #cccccc;
    border-radius: 5px;
    padding: 10px;
}

QLabel {
    font-family: "Segoe UI";
    font-size: 14px;
}
"""

def apply_theme(app, theme_name):
    if theme_name == "light":
        app.setStyleSheet(light_theme)
    elif theme_name == "dark":
        app.setStyleSheet(dark_theme)
