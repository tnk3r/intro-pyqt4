#!/usr/bin/python


class fontlib():

    def __init__(self):

        self.alert_text = "font-family: Helvetica; background: black; font-size: 30px;" \
                          "color: yellow; border: 5px solid yellow;"

        self.alert_ok = "background: Black; " \
                        "font-family: Helvetica; " \
                        "color: White;" \
                        " font-size: 40px; " \
                        "border: 6px solid red; " \
                        "border-radius: 16px;" \
                        "qproperty-alignment: AlignCenter;"

    def italic_style(self, color, size):
        style = "background: Black; " \
                "font-family: Helvetica; " \
                "font-style: italic;" \
                "color: "+color+";" \
                " font-size: "+str(size)+"px; " \
                "qproperty-alignment: AlignCenter; "

        return style

