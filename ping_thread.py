#!/usr/bin/python


from PyQt4.QtCore import QThread, pyqtSignal
import subprocess, time



class ping_thread(QThread):


    ping_time = pyqtSignal(str)
    ping_status = pyqtSignal(str)
    ping_indicator = pyqtSignal(str)

    def __init__(self, address):
        QThread.__init(self, parent= None)
        self.address = address

        self.run()

    def ping_loop(self):

        while self.ping_status > 30:
            status = subprocess.check_output(["ping", "-c", "1", "-t", "1", str(self.address)])
            print status.split(" ")
            time.sleep(2)

    def run(self):
        print "Starting Ping Loop"
        self.ping_loop()


