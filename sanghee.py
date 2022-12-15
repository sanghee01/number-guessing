from PyQt5 import QtCore, QtGui, QtWidgets
import random


answer = random.randint(1, 100)  # 정답을 1에서 100 사이의 난수로 설정한다.
count = 0


class Ui_MainWindow(object):

    # 시도 버튼 - 추측 결과를 보여주는 함수
    def guessing(self):
        global count
        count += 1
        guess = int(self.basicLine.text())  # 입력값 가져옴
        # print(self.)
        if guess > answer:
            msg = "더 낮은 숫자입니다"
        elif guess < answer:
            msg = "더 높은 숫자입니다"
        else:
            msg = "정답입니다!"
        self.basicSpeak.setText(msg)  # 메시지를 출력한다.
        self.basicTryCount.setText(f"시도 횟수: {count}")
        self.basicLine.setText("")

    # 초기화 버튼 - 정답을 다시 설정
    def reset(self):
        global answer
        global count
        answer = random.randint(1, 100)
        count = 0
        self.basicSpeak.setText("다시 도전해봅시다")
        self.basicTryCount.setText(f"시도 횟수: {count}")
    # 힌트 버튼 - x-10 ~ x+10범위

    def hint(self):
        global answer
        # 메시지를 출력한다.
        self.basicSpeak.setText(f"{answer-10} ~ {answer+10}사이의 값입니다.")

    def setupUi(self, MainWindow):

        # 메인 오브젝트
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # 메인 화면
        self.centralwidget.setObjectName("centralwidget")
        self.main = QtWidgets.QWidget(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.main.setStyleSheet("background-color: white")
        self.main.setObjectName("main")

        # 메인 타이틀
        self.mainTitle = QtWidgets.QLabel(self.main)
        self.mainTitle.setGeometry(QtCore.QRect(310, 140, 421, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(50)
        self.mainTitle.setFont(font)
        self.mainTitle.setObjectName("mainTitle")

        # 메인 버튼 그리드
        self.gridLayoutWidget = QtWidgets.QWidget(self.main)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(370, 270, 251, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # 기본모드 버튼
        self.basicModeBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.basicModeBtn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(30)
        self.basicModeBtn.setFont(font)
        self.basicModeBtn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.basicModeBtn.setObjectName("basicModeBtn")
        self.gridLayout.addWidget(self.basicModeBtn, 1, 0, 1, 1)

        # 제한모드 버튼
        self.countModeBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(30)
        self.countModeBtn.setFont(font)
        self.countModeBtn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.countModeBtn.setObjectName("countModeBtn")
        self.gridLayout.addWidget(self.countModeBtn, 2, 0, 1, 1)

        # 시간모드 버튼
        self.clockModeBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(30)
        self.clockModeBtn.setFont(font)
        self.clockModeBtn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clockModeBtn.setObjectName("clockModeBtn")
        self.gridLayout.addWidget(self.clockModeBtn, 3, 0, 1, 1)

        # 기본모드 화면
        # 기본모드 제목 ??
        self.mainTitle_2 = QtWidgets.QLabel(self.main)
        self.mainTitle_2.setGeometry(QtCore.QRect(780, 730, 211, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.mainTitle_2.setFont(font)
        self.mainTitle_2.setObjectName("mainTitle_2")
        # 기본모드 화면설정
        self.basicMode = QtWidgets.QWidget(self.centralwidget)
        self.basicMode.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.basicMode.setStyleSheet("background-color: white")
        self.basicMode.setObjectName("basicMode")
        # 기본모드 뒤로가기 버튼
        self.basicBackBtn = QtWidgets.QPushButton(self.basicMode)
        self.basicBackBtn.setGeometry(QtCore.QRect(20, 20, 61, 61))
        self.basicBackBtn.setStyleSheet("\n"
                                        "background-image: url(뒤로가기.png);")
        self.basicBackBtn.setText("")
        self.basicBackBtn.setObjectName("basicBackBtn")
        # 기본모드 제목
        self.basicTitle = QtWidgets.QLabel(self.basicMode)
        self.basicTitle.setGeometry(QtCore.QRect(450, 20, 111, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(40)
        self.basicTitle.setFont(font)
        self.basicTitle.setObjectName("basicTitle")
        # 기본모드 사진
        self.basicImage = QtWidgets.QLabel(self.basicMode)
        self.basicImage.setGeometry(QtCore.QRect(130, 150, 341, 421))
        self.basicImage.setStyleSheet("image: url(교수.png);")
        self.basicImage.setText("")
        self.basicImage.setObjectName("basicImage")
        # 기본모드 진행 상황 설명글
        self.basicSpeak = QtWidgets.QLabel(self.basicMode)
        self.basicSpeak.setGeometry(QtCore.QRect(540, 220, 321, 191))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.basicSpeak.setFont(font)
        self.basicSpeak.setObjectName("basicSpeak")
        # 기본모드 입력란
        self.basicLine = QtWidgets.QLineEdit(self.basicMode)
        self.basicLine.setGeometry(QtCore.QRect(200, 580, 281, 71))
        self.basicLine.setObjectName("basicLine")
        # 기본모드 시도 버튼
        self.basicTryBtn = QtWidgets.QPushButton(self.basicMode)
        self.basicTryBtn.setGeometry(QtCore.QRect(490, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.basicTryBtn.setFont(font)
        self.basicTryBtn.setObjectName("basicTryBtn")
        self.basicTryBtn.clicked.connect(self.guessing)  # 시도 버튼 클릭 시
        # 기본모드 다시 버튼
        self.basicRetryBtn = QtWidgets.QPushButton(self.basicMode)
        self.basicRetryBtn.setGeometry(QtCore.QRect(580, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.basicRetryBtn.setFont(font)
        self.basicRetryBtn.setObjectName("basicRetryBtn")
        self.basicRetryBtn.clicked.connect(self.reset)  # 다시 버튼 클릭 시

        # 기본모드 힌트 버튼
        self.basicHintBtn = QtWidgets.QPushButton(self.basicMode)
        self.basicHintBtn.setGeometry(QtCore.QRect(670, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.basicHintBtn.setFont(font)
        self.basicHintBtn.setObjectName("basicHintBtn")
        self.basicHintBtn.clicked.connect(self.hint)  # 힌트 버튼 클릭 시

        # 기본모드 시도 횟수
        self.basicTryCount = QtWidgets.QLabel(self.basicMode)
        self.basicTryCount.setGeometry(QtCore.QRect(770, 590, 141, 51))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(20)
        self.basicTryCount.setFont(font)
        self.basicTryCount.setObjectName("basicTryCount")

        # 제한모드 화면
        self.countMode = QtWidgets.QWidget(self.centralwidget)
        self.countMode.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.countMode.setStyleSheet("background-color: white")
        self.countMode.setObjectName("countMode")
        self.countBackBtn = QtWidgets.QPushButton(self.countMode)
        self.countBackBtn.setGeometry(QtCore.QRect(20, 20, 61, 61))
        self.countBackBtn.setStyleSheet("\n"
                                        "background-image: url(뒤로가기.png);")
        self.countBackBtn.setText("")
        self.countBackBtn.setObjectName("countBackBtn")
        self.countTitle = QtWidgets.QLabel(self.countMode)
        self.countTitle.setGeometry(QtCore.QRect(450, 20, 131, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(40)
        self.countTitle.setFont(font)
        self.countTitle.setObjectName("countTitle")
        self.countImage = QtWidgets.QLabel(self.countMode)
        self.countImage.setGeometry(QtCore.QRect(130, 150, 341, 421))
        self.countImage.setStyleSheet("image: url(교수.png);")
        self.countImage.setText("")
        self.countImage.setObjectName("countImage")
        self.countSpeak = QtWidgets.QLabel(self.countMode)
        self.countSpeak.setGeometry(QtCore.QRect(540, 220, 321, 191))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.countSpeak.setFont(font)
        self.countSpeak.setObjectName("countSpeak")
        self.countLine = QtWidgets.QLineEdit(self.countMode)
        self.countLine.setGeometry(QtCore.QRect(280, 580, 281, 71))
        self.countLine.setObjectName("countLine")
        self.countTryBtn = QtWidgets.QPushButton(self.countMode)
        self.countTryBtn.setGeometry(QtCore.QRect(570, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.countTryBtn.setFont(font)
        self.countTryBtn.setObjectName("countTryBtn")
        self.countRetryBtn = QtWidgets.QPushButton(self.countMode)
        self.countRetryBtn.setGeometry(QtCore.QRect(660, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.countRetryBtn.setFont(font)
        self.countRetryBtn.setObjectName("countRetryBtn")
        self.countCount = QtWidgets.QLabel(self.countMode)
        self.countCount.setGeometry(QtCore.QRect(390, 90, 281, 91))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(50)
        self.countCount.setFont(font)
        self.countCount.setObjectName("countCount")

        # 시간모드 화면
        self.clockMode = QtWidgets.QWidget(self.centralwidget)
        self.clockMode.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.clockMode.setStyleSheet("background-color: white")
        self.clockMode.setObjectName("clockMode")
        self.clockBackBtn = QtWidgets.QPushButton(self.clockMode)
        self.clockBackBtn.setGeometry(QtCore.QRect(20, 20, 61, 61))
        self.clockBackBtn.setStyleSheet("\n"
                                        "background-image: url(뒤로가기.png);")
        self.clockBackBtn.setText("")
        self.clockBackBtn.setObjectName("clockBackBtn")
        self.clockTitle = QtWidgets.QLabel(self.clockMode)
        self.clockTitle.setGeometry(QtCore.QRect(450, 20, 111, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(40)
        self.clockTitle.setFont(font)
        self.clockTitle.setObjectName("clockTitle")
        self.clockImage = QtWidgets.QLabel(self.clockMode)
        self.clockImage.setGeometry(QtCore.QRect(130, 150, 341, 421))
        self.clockImage.setStyleSheet("image: url(교수.png);")
        self.clockImage.setText("")
        self.clockImage.setObjectName("clockImage")
        self.clockSpeak = QtWidgets.QLabel(self.clockMode)
        self.clockSpeak.setGeometry(QtCore.QRect(540, 220, 321, 191))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.clockSpeak.setFont(font)
        self.clockSpeak.setObjectName("clockSpeak")
        self.clockLine = QtWidgets.QLineEdit(self.clockMode)
        self.clockLine.setGeometry(QtCore.QRect(280, 580, 281, 71))
        self.clockLine.setObjectName("clockLine")
        self.clockTryBtn = QtWidgets.QPushButton(self.clockMode)
        self.clockTryBtn.setGeometry(QtCore.QRect(570, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.clockTryBtn.setFont(font)
        self.clockTryBtn.setObjectName("clockTryBtn")
        self.clockRetryBtn = QtWidgets.QPushButton(self.clockMode)
        self.clockRetryBtn.setGeometry(QtCore.QRect(660, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.clockRetryBtn.setFont(font)
        self.clockRetryBtn.setObjectName("clockRetryBtn")
        self.clockClock = QtWidgets.QLabel(self.clockMode)
        self.clockClock.setGeometry(QtCore.QRect(430, 100, 161, 91))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(60)
        self.clockClock.setFont(font)
        self.clockClock.setObjectName("clockClock")
        MainWindow.setCentralWidget(self.centralwidget)

        # retranslateUi 호출
        self.retranslateUi(MainWindow)

        # 기본모드 버튼 눌렀을 때
        self.basicModeBtn.clicked.connect(self.basicMode.show)  # 기본모드 화면 보임
        self.basicModeBtn.clicked.connect(self.main.hide)  # 메인 화면 가림
        self.basicModeBtn.clicked.connect(self.countMode.hide)  # 제한모드 화면 가림
        self.basicModeBtn.clicked.connect(self.clockMode.hide)  # 시간모드 화면 가림

        # 기본모드 뒤로가기 버튼 눌렀을 때
        self.basicBackBtn.clicked.connect(self.basicMode.hide)  # 기본모드 화면 가림
        self.basicBackBtn.clicked.connect(self.main.show)  # 메인 화면 보임

        # 제한모드 버튼 눌렀을 때
        self.countModeBtn.clicked.connect(self.countMode.show)  # 제한모드 화면 보임
        self.countModeBtn.clicked.connect(self.main.hide)  # 메인 화면 가림
        self.countModeBtn.clicked.connect(self.clockMode.hide)  # 시간모드 화면 가림
        self.countModeBtn.clicked.connect(self.basicMode.hide)  # 기본모드 화면 가림

        # 제한모드 뒤로가기 버튼 눌렀을 때
        self.countBackBtn.clicked.connect(self.countMode.hide)  # 기본모드 화면 가림
        self.countBackBtn.clicked.connect(self.main.show)  # 메인 화면 보임

        # 시간모드 버튼 눌렀을 때
        self.clockModeBtn.clicked.connect(self.clockMode.show)  # 시간모드 화면 보임
        self.clockModeBtn.clicked.connect(self.main.hide)  # 메인 화면 가림
        self.clockModeBtn.clicked.connect(self.countMode.hide)  # 제한모드 화면 가림
        self.clockModeBtn.clicked.connect(self.basicMode.hide)  # 기본모드 화면 가림

        # 시간모드 뒤로가기 버튼 눌렀을 때
        self.clockBackBtn.clicked.connect(self.clockMode.hide)  # 시간모드 화면 가림
        self.clockBackBtn.clicked.connect(self.main.show)  # 메인 화면 보임

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTitle.setText(_translate("MainWindow", "교수님이 생각하신 숫자는?"))
        self.basicModeBtn.setText(_translate("MainWindow", "기본 모드"))
        self.countModeBtn.setText(_translate("MainWindow", "제한 모드"))
        self.clockModeBtn.setText(_translate("MainWindow", "시간 모드"))
        self.mainTitle_2.setText(_translate("MainWindow", "03분반 20212195 이상희"))
        self.basicTitle.setText(_translate("MainWindow", "기본 모드"))
        self.basicSpeak.setText(_translate(
            "MainWindow", "1부터 100사이의 숫자를 맞춰보세요"))
        self.basicTryBtn.setText(_translate("MainWindow", "시도"))
        self.basicRetryBtn.setText(_translate("MainWindow", "다시"))
        self.basicHintBtn.setText(_translate("MainWindow", "힌트"))
        self.basicTryCount.setText(_translate("MainWindow", "시도 횟수 : 0"))
        self.countTitle.setText(_translate("MainWindow", "제한 모드"))
        self.countSpeak.setText(_translate(
            "MainWindow", "1부터 100사이의 숫자를 맞춰보세요"))
        self.countTryBtn.setText(_translate("MainWindow", "시도"))
        self.countRetryBtn.setText(_translate("MainWindow", "다시"))
        self.countCount.setText(_translate("MainWindow", "남은 기회 : 10"))
        self.clockTitle.setText(_translate("MainWindow", "시간 모드"))
        self.clockSpeak.setText(_translate(
            "MainWindow", "1부터 100사이의 숫자를 맞춰보세요"))
        self.clockTryBtn.setText(_translate("MainWindow", "시도"))
        self.clockRetryBtn.setText(_translate("MainWindow", "다시"))
        self.clockClock.setText(_translate("MainWindow", "00 : 20"))
        self.basicMode.setHidden(True)  # 기본모드 hide
        self.clockMode.setHidden(True)  # 시간모드 hide
        self.countMode.setHidden(True)  # 제한모드 hide


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
