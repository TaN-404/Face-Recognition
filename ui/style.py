

def apply_green_button_style(button):
    button.setStyleSheet("""
        QPushButton {
            background-color: #ffffff;
            color: #052f57;
            font-size: 16px;
            border: 2px solid #6abe30;
            border-radius: 5px;
            padding: 10px;
        }

        QPushButton:hover {
            background-color: #6abe30;
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
    """)

def apply_red_button_style(button):
    button.setStyleSheet("""
        QPushButton {
            background-color: #ffffff;
            color: #052f57;
            font-size: 16px;
            border: 2px solid #ac3232;
            border-radius: 5px;
            padding: 10px;
        }

        QPushButton:hover {
            background-color: #ac3232;
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
    """)

