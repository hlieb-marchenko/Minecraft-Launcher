import sys, webbrowser, sqlite3, hashlib
from PyQt5 import QtCore,QtGui,QtWidgets

db = sqlite3.connect("data.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users(
            username TEXT,
            password TEXT
)
""")
db.commit()

def login():
    password = hashlib.md5("12345".encode()).hexdigest()
    username = "admin"
    sql.execute(f"SELECT username, password FROM users WHERE password = '{password}' AND username = '{username}'")
    if sql.fetchone():
        print("Welcome")
    else:
        print("Register first")
def register():
    password = hashlib.md5("12345".encode()).hexdigest()
    username = "admin"
    sql.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")
    print(password)
    login()
# register()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # f = open('/Users/admin/Documents/WEB/Launcher/css/style.css','r')
        # self.styleData = f.read()
        # f.close()

        self.isShowed = False
        self.friendsIsShowed = False

        names = ["Alex", "Ben", "Hello"]
        # -------------------------
        for name in names:
            exec(f"self.friendsListWidgetItem{name} = QtWidgets.QListWidgetItem()") 
            exec(f"self.friendsListWidgetItemWidget{name} = QtWidgets.QWidget()")

            self.itemIcon = QtWidgets.QLabel(parent=self)
            self.itemIcon.setFixedSize(17,15)
            self.itemIcon.setStyleSheet("border-image: url('') 0 0 0 0; background: white; margin-right: 2px; border-radius: 7px")

            self.itemText = QtWidgets.QLabel(f"{name}{(14-len(name))*" "}")
            self.itemText.setStyleSheet("color: white; font-size: 10px")

            self.itemStatus = QtWidgets.QLabel("Active Status", parent=self)
            self.itemStatus.setStyleSheet("color: green; font-size: 10px; ")

            self.itemBox = QtWidgets.QHBoxLayout()
            self.itemBox.addWidget(self.itemIcon)
            self.itemBox.addWidget(self.itemText)
            self.itemBox.addWidget(self.itemStatus)

            self.itemBox.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            exec(f"self.friendsListWidgetItemWidget{name}.setLayout(self.itemBox)") 
            exec(f"self.friendsListWidgetItem{name}.setSizeHint(self.friendsListWidgetItemWidget{name}.sizeHint())") 
        # -------------------------


        def openDiscord():
            webbrowser.open_new_tab("https://www.youtube.com")
        def showMore():
            if self.isShowed == False:
                self.friendsButton.show()
                self.leaderboardButton.show()
                self.rulesButton.show()
                self.teamButton.show()
                self.settingsButton.show()

                self.moreButton.setText("   More  ▼")
                self.isShowed = True
            else:
                self.friendsButton.hide()
                self.leaderboardButton.hide()
                self.rulesButton.hide()
                self.teamButton.hide()
                self.settingsButton.hide()
                self.friendsList.hide()
                self.friendsMenu.hide()
                self.friendsMenuLabel.hide()

                self.moreButton.setText("   More  ▲")
                self.friendsIsShowed = False
                self.isShowed = False
        def showMoreFriends():
            if self.friendsIsShowed == False:
                self.friendsList.show()
                self.friendsMenu.show()
                self.friendsMenuLabel.show()

                self.friendsIsShowed = True
            else:
                self.friendsList.hide()
                self.friendsMenu.hide()
                self.friendsMenuLabel.hide()

                self.friendsIsShowed = False
        
        self.setWindowTitle("Genesis Arkanum")
        # self.setGeometry(0,0,800,400)
        self.setFixedSize(800,400)

        self.background = QtWidgets.QLabel(parent = self)
        self.background.setStyleSheet('''border-image: url('/Users/admin/Documents/WEB/Launcher/img/Frame 4.png') 0 0 0 0 stretch stretch;''')
        self.background.setFixedSize(800,400)
        
        self.accountIcon = QtWidgets.QPushButton(parent = self)
        self.accountIcon.setStyleSheet("background: #D9D9D9; border-radius: 10px;")
        self.accountIcon.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.accountIcon.setFixedSize(22,22)
        self.accountIcon.move(693,7)

        self.accountButton = QtWidgets.QPushButton("Account",parent = self)
        self.accountButton.setStyleSheet('''QPushButton{background: #3B3A3A; border-radius: 6px; color: white; font-size: 9px;}
                                         QPushButton:hover{background: #000000}''')
        self.accountButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.accountButton.setFixedSize(74,12)
        self.accountButton.move(719,6)

        self.moreButton = QtWidgets.QPushButton("   More  ▲",parent = self)
        self.moreButton.setStyleSheet('''QPushButton{background: #DBC9C9;border-radius: 6px;color: #000;font-size: 9px;}
                                      QPushButton:hover{background: #545151}''')
        self.moreButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.moreButton.setFixedSize(58,12)
        self.moreButton.clicked.connect(showMore)
        self.moreButton.move(727,23)
        
        # ------------MORE------------------
        self.friendsButton = QtWidgets.QPushButton(parent=self)
        self.friendsButton.setStyleSheet('''QPushButton{border-image: url(/Users/admin/Documents/WEB/Launcher/img/friends.1.jpg) 0 0 0 0}
                                         QPushButton:hover{border-image: url(/Users/admin/Documents/WEB/Launcher/img/friends.2.jpg) 0 0 0 0}''')
        self.friendsButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.friendsButton.setFixedSize(78,31)
        self.friendsButton.clicked.connect(showMoreFriends)
        self.friendsButton.hide()
        self.friendsButton.move(717,50)

        self.friendsMenu = QtWidgets.QLabel(parent=self)
        self.friendsMenu.setStyleSheet("background: black")
        self.friendsMenu.setFixedSize(220, 110)
        self.friendsMenu.move(495,50)
        self.friendsMenu.hide()

        self.friendsMenuLabel = QtWidgets.QLabel("Friends", parent=self)
        self.friendsMenuLabel.setStyleSheet("background: rgba(51, 49, 49); color: lightblue; border-radius: 6; font-size: 10px;")
        self.friendsMenuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.friendsMenuLabel.setFixedSize(75,12)
        self.friendsMenuLabel.move(567, 52)
        self.friendsMenuLabel.hide()

        self.friendsList = QtWidgets.QListWidget(parent=self)
        self.friendsList.setStyleSheet('''QListWidget{background: black; color: white; font-size: 10px;}
                                       QListWidget::item{background: rgba(51, 49, 49); margin-bottom: 5px;border-radius: 10px}''')
        self.friendsList.setFixedSize(200, 60)
        self.friendsList.move(505, 70)
        for name in names:
            exec(f"self.friendsList.addItem(self.friendsListWidgetItem{name})")
            exec(f"self.friendsList.setItemWidget(self.friendsListWidgetItem{name}, self.friendsListWidgetItemWidget{name})")
        self.friendsList.hide()


        


        self.leaderboardButton = QtWidgets.QPushButton(parent=self)
        self.leaderboardButton.setStyleSheet('''QPushButton{border-image: url(/Users/admin/Documents/WEB/Launcher/img/leaderboard.1.jpg) 0 0 0 0}
                                         QPushButton:hover{border-image: url(/Users/admin/Documents/WEB/Launcher/img/leaderboard.2.jpg) 0 0 0 0}''')
        self.leaderboardButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.leaderboardButton.setFixedSize(78,23)
        self.leaderboardButton.hide()
        self.leaderboardButton.move(717,83)

        self.rulesButton = QtWidgets.QPushButton(parent=self)
        self.rulesButton.setStyleSheet('''QPushButton{border-image: url(/Users/admin/Documents/WEB/Launcher/img/rules.1.jpg) 0 0 0 0}
                                         QPushButton:hover{border-image: url(/Users/admin/Documents/WEB/Launcher/img/rules.2.jpg) 0 0 0 0}''')
        self.rulesButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.rulesButton.setFixedSize(78,24)
        self.rulesButton.hide()
        self.rulesButton.move(717,108)

        self.teamButton = QtWidgets.QPushButton(parent=self)
        self.teamButton.setStyleSheet('''QPushButton{border-image: url(/Users/admin/Documents/WEB/Launcher/img/team.2.jpg) 0 0 0 0}
                                         QPushButton:hover{border-image: url(/Users/admin/Documents/WEB/Launcher/img/team.2.jpg) 0 0 0 0}''')
        self.teamButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.teamButton.setFixedSize(78,25)
        self.teamButton.hide()
        self.teamButton.move(717,134)

        self.settingsButton = QtWidgets.QPushButton(parent=self)
        self.settingsButton.setStyleSheet('''QPushButton{border-image: url('/Users/admin/Documents/WEB/Launcher/img/settings.1.jpg') 0 0 0 0}
                                      QPushButton:hover{border-image: url('/Users/admin/Documents/WEB/Launcher/img/settings.2.jpg') 0 0 0 0}''')
        self.settingsButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.settingsButton.setFixedSize(78, 25)
        self.settingsButton.hide()
        self.settingsButton.move(717, 161)
        # ----------------------------------

        self.findUsInRectangle = QtWidgets.QLabel(parent = self)
        self.findUsInRectangle.setStyleSheet("border-image: url(/Users/admin/Documents/WEB/Launcher/img/Group 10.png) 0 0 0 0")
        self.findUsInRectangle.setFixedSize(123,44)
        self.findUsInRectangle.move(677,356)

        self.findUsInDiscord = QtWidgets.QPushButton(parent = self)
        self.findUsInDiscord.setStyleSheet('''QPushButton{border-image: url('/Users/admin/Documents/WEB/Launcher/img/discord_1.png') 0 0 0 0; border-radius: 11px;}
                                           QPushButton:hover{border-image: url('/Users/admin/Documents/WEB/Launcher/img/discord_2.png') 0 0 0 0;}''')
        self.findUsInDiscord.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.findUsInDiscord.setFixedSize(22,21)
        self.findUsInDiscord.move(677,377)
        self.findUsInDiscord.clicked.connect(openDiscord)

        # ----------------------------------

        self.battlePassRectangle = QtWidgets.QLabel(parent = self)
        self.battlePassRectangle.setStyleSheet("border-image: url('/Users/admin/Documents/WEB/Launcher/img/Group 6.png') 0 0 0 0")
        self.battlePassRectangle.setFixedSize(196,44)
        self.battlePassRectangle.move(0, 356)

        # MODES -------------------------------------------------------------------

        # Arcanum mythical battles
        self.firstBorder = QtWidgets.QLabel(parent=self)
        self.firstBorder.setStyleSheet("background: rgba(51, 49, 49, 0.70);")
        self.firstBorder.setFixedSize(227, 121)
        self.firstBorder.move(15, 66)

        self.firstImg = QtWidgets.QLabel(parent=self)
        self.firstImg.setStyleSheet("background: rgba(0, 0, 0, 0.55);")
        self.firstImg.setFixedSize(213,81)
        self.firstImg.move(25,74)

        self.firstButton = QtWidgets.QPushButton("download",parent=self)
        self.firstButton.setStyleSheet('''QPushButton{background: #211F91; border-radius: 5px;color: #FFF;font-size: 8px;font-family: Aclonica;}
                                        QPushButton:hover{background: #0C0C23}''')
        # self.firstButton.setText("Open")
        # self.firstButton.setStyleSheet('''QPushButton{background: #1F9123; border-radius: 5px;color: #FFF;font-size: 8px;font-family: Aclonica;}
        #                                QPushButton:hover{background: #1D4F1F}''')
        self.firstButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.firstButton.setFixedSize(43,10)
        self.firstButton.move(194,167)

        # Coming soon

        self.show()

class Loading(QtWidgets.QSplashScreen):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Genesis Arkanum")
        self.setGeometry(0,0,800,400)
        self.setPixmap(QtGui.QPixmap("/Users/admin/Documents/WEB/Launcher/img/Loading.png").scaled(800,400))
        self.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    l = Loading()   
    l.showMessage("<h1 style='color: #FFF;font-weight: 800;'>LOADING</h1>",QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    for i in range(1):      
        QtCore.QThread.msleep(500)
        l.showMessage("<h1 style='color: #FFF;font-weight: 800;'>LOADING.</h1>",QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        QtCore.QThread.msleep(500)
        l.showMessage("<h1 style='color: #FFF;font-weight: 800'>LOADING..</h1>",QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        QtCore.QThread.msleep(500)
        l.showMessage("<h1 style='color: #FFF;font-weight: 800;'>LOADING...</h1>",QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    # QtCore.QThread.msleep(5000)

    w = MainWindow()
    l.finish(w)

    sys.exit(app.exec_())
