from PyQt5 import QtCore, QtGui, QtWidgets
import random

answer = random.randint(1, 100)  # 정답을 1에서 100 사이의 난수로 설정

count = 0  # 시도 횟수

count_count = 10  # 제한 모드 - 남은 기회

timer = 20  # 시간 모드 - 타이머
clock_win = 0  # 시간 모드 - 정답 맞췄을때 1로 설정하여 타이머 멈춤


class Ui_MainWindow(object):

    # 기본모드 함수 ----------

    # 시도 버튼 - 추측 결과를 보여주는 함수
    def basic_guessing(self):
        global count  # 시도 횟수
        count += 1  # 시도 횟수 + 1
        guess = int(self.basicLine.text())  # 입력값 가져옴
        if guess > answer:  # 추측 값 > 정답 값
            msg = "더 낮은 숫자입니다"
        elif guess < answer:  # 추측 값 < 정답 값
            msg = "더 높은 숫자입니다"
        else:  # 정답일 때
            msg = "정답입니다!"
            self.basicImage.setStyleSheet("image: url(정답.png);")  # 정답 표정으로 바뀜
        self.basicSpeak.setText(msg)  # 추측 결과 메시지 출력
        self.basicTryCount.setText(f"시도 횟수: {count}")  # 시도 횟수 메시지 출력
        self.basicLine.setText("")  # 입력란 비우기

    # 초기화 버튼
    def basic_reset(self):
        global answer
        global count
        answer = random.randint(1, 100)  # 정답 다시 설정
        count = 0  # 카운트 0으로 설정
        self.basicImage.setStyleSheet("image: url(기본.png);")  # 기본 표정으로 바뀜
        self.basicSpeak.setText("다시 도전해봅시다")
        self.basicTryCount.setText(f"시도 횟수: {count}")

    # 힌트 버튼 - x-10 ~ x+10범위
    def basic_hint(self):
        global answer
        self.basicSpeak.setText(f"{answer-10} ~ {answer+10}사이의 값입니다.")

    # 뒤로가기 버튼
    def basic_back(self):
        global answer
        global count
        answer = random.randint(1, 100)  # 정답 다시 설정
        count = 0  # 카운트 0으로 설정
        self.basicSpeak.setText("1부터 100사이의 숫자를 맞춰보세요")
        self.basicTryCount.setText(f"시도 횟수: {count}")
        self.basicImage.setStyleSheet("image: url(기본.png);")  # 기본 표정으로 바뀜

    # 제한모드 함수 ------------

    # 시도 버튼 - 추측 결과를 보여주는 함수
    def count_guessing(self):
        global count_count
        count_count -= 1  # 남은 횟수가 1씩 줄어듦
        if count_count < 0:  # 남은 횟수가 없으면 return
            return
        guess = int(self.countLine.text())  # 입력값 가져옴
        if guess > answer:
            msg = "더 낮은 숫자입니다"
        elif guess < answer:
            msg = "더 높은 숫자입니다"
        else:
            msg = "정답입니다!"
            self.countImage.setStyleSheet("image: url(정답.png);")

        self.countSpeak.setText(msg)  # 메시지를 출력한다.
        self.countCount.setText(f"남은 기회 : {count_count}")
        self.countLine.setText("")
        if count_count == 0:  # 남은 횟수가 0이면
            self.countSpeak.setText(
                "숫자를 맞추지 못했습니다. \n재도전하고 싶으면\n'다시' 버튼을 눌러주세요")
            self.countImage.setStyleSheet("image: url(실패.png);")

    # 초기화 버튼 - 정답을 다시 설정
    def count_reset(self):
        global count_count
        global answer
        count_count = 10  # 남은 횟수 10으로 초기화
        answer = random.randint(1, 100)
        self.countImage.setStyleSheet("image: url(기본.png);")
        self.countSpeak.setText("다시 도전해봅시다")
        self.countCount.setText(f"남은 기회 : {count_count}")
        self.countLine.setText("")

    # 뒤로가기 버튼
    def count_back(self):
        global answer
        global count_count
        answer = random.randint(1, 100)
        count_count = 10
        self.countImage.setStyleSheet("image: url(기본.png);")
        self.countSpeak.setText("1부터 100사이의 숫자를 맞춰보세요")
        self.countCount.setText(f"남은 기회 : {count_count}")
        self.countLine.setText("")

    # 시간모드 함수 ---------------------
    # 타이머 시작 함수
    def startTimer(self):
        self.myTimer.timeout.connect(self.timerTimeout)  # 해당 함수 호출
        self.myTimer.start(1000)  # 1초 간격으로 실행

    # 타이머 돌아가는 함수
    def timerTimeout(self):
        global timer
        global clock_win

        if clock_win == 1:  # 정답 맞추면 타이머 정지
            self.myTimer.stop()

        timer -= 1  # 타이머 1초씩 줄어듦

        if timer == 0:  # 타이머가 0이면
            self.myTimer.stop()  # 타이머 정지
            self.clockImage.setStyleSheet("image: url(실패.png);")
            self.clockSpeak.setText(
                "숫자를 맞추지 못했습니다. \n재도전하고 싶으면\n'다시' 버튼을 눌러주세요")

        self.update_gui()  # 타이머 gui 업데이트 함수 호출

    def update_gui(self):
        # 화면에 타이머 메세지 보이도록
        # 한자리 숫자면 앞에 0 붙이기
        if timer >= 10:
            self.clockClock.setText(f"00 : {str(timer)}")
        else:
            self.clockClock.setText(f"00 : {'0'+str(timer)}")

    # 시도 버튼 - 추측 결과를 보여주는 함수
    def clock_guessing(self):
        global clock_win

        guess = int(self.clockLine.text())  # 입력값 가져옴
        if guess > answer:
            msg = "더 낮은 숫자입니다"
        elif guess < answer:
            msg = "더 높은 숫자입니다"
        else:
            clock_win = 1  # 정답이면 clock_win = 1
            msg = "정답입니다!"
            self.clockImage.setStyleSheet("image: url(정답.png);")

        self.clockSpeak.setText(msg)  # 메시지를 출력한다.
        self.clockLine.setText("")

    # 초기화 버튼 - 정답을 다시 설정
    def clock_reset(self):
        global answer
        global timer
        global clock_win
        answer = random.randint(1, 100)
        timer = 20
        clock_win = 0
        self.clockImage.setStyleSheet("image: url(기본.png);")
        self.clockSpeak.setText("다시 도전해봅시다")
        self.clockLine.setText("")
        self.myTimer.start(1000)

    # 뒤로가기 버튼
    def clock_back(self):
        global answer
        global timer
        global clock_win
        answer = random.randint(1, 100)
        timer = 20
        clock_win = 0
        self.clockImage.setStyleSheet("image: url(기본.png);")
        self.clockSpeak.setText("1부터 100사이의 숫자를 맞춰보세요")
        self.clockLine.setText("")

    # ======= GUI 부분 ========

    def setupUi(self, MainWindow):

        # 메인 오브젝트
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # 메인 화면 --------------
        self.centralwidget.setObjectName("centralwidget")
        self.main = QtWidgets.QWidget(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.main.setStyleSheet("background-color: white")
        self.main.setObjectName("main")

        # 메인 타이틀
        self.mainTitle = QtWidgets.QLabel(self.main)
        self.mainTitle.setGeometry(QtCore.QRect(300, 140, 421, 71))
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
        self.basicModeBtn.setFixedSize(180, 60)
        self.basicModeBtn.setStyleSheet("color: rgb(58, 134, 255);"
                                        "background-color: white;"
                                        "border: 2px solid rgb(58, 134, 255);"
                                        "border-radius: 5px;")
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
        self.countModeBtn.setFixedSize(180, 60)
        self.countModeBtn.setStyleSheet("color: rgb(58, 134, 255);"
                                        "background-color: white;"
                                        "border: 2px solid rgb(58, 134, 255);"
                                        "border-radius: 5px;")
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
        self.clockModeBtn.setFixedSize(180, 60)
        self.clockModeBtn.setStyleSheet("color: rgb(58, 134, 255);"
                                        "background-color: white;"
                                        "border: 2px solid rgb(58, 134, 255);"
                                        "border-radius: 5px;")
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(30)
        self.clockModeBtn.setFont(font)
        self.clockModeBtn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clockModeBtn.setObjectName("clockModeBtn")
        self.gridLayout.addWidget(self.clockModeBtn, 3, 0, 1, 1)

        # 분반 학번 이름
        self.mainTitle_2 = QtWidgets.QLabel(self.main)
        self.mainTitle_2.setGeometry(QtCore.QRect(790, 760, 211, 41))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.mainTitle_2.setFont(font)
        self.mainTitle_2.setObjectName("mainTitle_2")
        self.mainTitle_2.setStyleSheet(
            "background-color:rgb(120, 226, 108);" "color:rgb(36, 107, 28);")

        # 기본모드 화면 ---------------
        # 기본모드 화면설정
        self.basicMode = QtWidgets.QWidget(self.centralwidget)
        self.basicMode.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.basicMode.setStyleSheet("background-color: white")
        self.basicMode.setObjectName("basicMode")
        # 기본모드 뒤로가기 버튼
        self.basicBackBtn = QtWidgets.QPushButton(self.basicMode)
        self.basicBackBtn.setGeometry(QtCore.QRect(15, 15, 55, 55))
        self.basicBackBtn.setStyleSheet("border: none;"
                                        "background-image: url(뒤로가기.png);")
        self.basicBackBtn.setText("")
        self.basicBackBtn.setObjectName("basicBackBtn")
        self.basicBackBtn.clicked.connect(self.basic_back)  # 뒤로가기 버튼 클릭 시

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
        self.basicImage.setGeometry(QtCore.QRect(70, 80, 550, 600))
        self.basicImage.setStyleSheet("image: url(기본.png);")
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
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(30)
        self.basicLine.setFont(font)
        self.basicLine.setStyleSheet("border: 2px solid black;"
                                     "border-radius: 5px;")
        # 기본모드 시도 버튼
        self.basicTryBtn = QtWidgets.QPushButton(self.basicMode)
        self.basicTryBtn.setGeometry(QtCore.QRect(490, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.basicTryBtn.setFont(font)
        self.basicTryBtn.setObjectName("basicTryBtn")
        self.basicTryBtn.clicked.connect(self.basic_guessing)  # 시도 버튼 클릭 시
        self.basicTryBtn.setStyleSheet("color: white;"
                                       "background-color: rgb(20, 173, 3);"
                                       "border: 3px solid rgb(28, 89, 21);"
                                       "border-radius: 5px;")
        # 기본모드 다시 버튼
        self.basicRetryBtn = QtWidgets.QPushButton(self.basicMode)
        self.basicRetryBtn.setGeometry(QtCore.QRect(580, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.basicRetryBtn.setFont(font)
        self.basicRetryBtn.setObjectName("basicRetryBtn")
        self.basicRetryBtn.clicked.connect(self.basic_reset)  # 다시 버튼 클릭 시
        self.basicRetryBtn.setStyleSheet("color: white;"
                                         "background-color: rgb(236, 32, 37);"
                                         "border: 3px solid rgb(107, 20, 21);"
                                         "border-radius: 5px;")

        # 기본모드 힌트 버튼
        self.basicHintBtn = QtWidgets.QPushButton(self.basicMode)
        self.basicHintBtn.setGeometry(QtCore.QRect(670, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.basicHintBtn.setFont(font)
        self.basicHintBtn.setObjectName("basicHintBtn")
        self.basicHintBtn.clicked.connect(self.basic_hint)  # 힌트 버튼 클릭 시
        self.basicHintBtn.setStyleSheet("color: white;"
                                        "background-color: rgb(58, 134, 255);"
                                        "border: 3px solid rgb(18, 55, 109);"
                                        "border-radius: 5px;")

        # 기본모드 시도 횟수
        self.basicTryCount = QtWidgets.QLabel(self.basicMode)
        self.basicTryCount.setGeometry(QtCore.QRect(770, 590, 141, 51))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(20)
        self.basicTryCount.setFont(font)
        self.basicTryCount.setObjectName("basicTryCount")

        # 제한모드 화면 ----------------
        # 제한모드 화면설정
        self.countMode = QtWidgets.QWidget(self.centralwidget)
        self.countMode.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.countMode.setStyleSheet("background-color: white")
        self.countMode.setObjectName("countMode")
        # 제한모드 뒤로가기 버튼
        self.countBackBtn = QtWidgets.QPushButton(self.countMode)
        self.countBackBtn.setGeometry(QtCore.QRect(15, 15, 55, 55))
        self.countBackBtn.setStyleSheet("border: none;"
                                        "background-image: url(뒤로가기.png);")
        self.countBackBtn.setText("")
        self.countBackBtn.setObjectName("countBackBtn")
        self.countBackBtn.clicked.connect(self.count_back)  # 뒤로가기 버튼 클릭 시

        # 제한모드 제목
        self.countTitle = QtWidgets.QLabel(self.countMode)
        self.countTitle.setGeometry(QtCore.QRect(450, 20, 131, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(40)
        self.countTitle.setFont(font)
        self.countTitle.setObjectName("countTitle")
        # 제한모드 사진
        self.countImage = QtWidgets.QLabel(self.countMode)
        self.countImage.setGeometry(QtCore.QRect(70, 80, 550, 600))
        self.countImage.setStyleSheet("image: url(기본.png);")
        self.countImage.setText("")
        self.countImage.setObjectName("countImage")
        # 제한모드 진행 상황 설명글
        self.countSpeak = QtWidgets.QLabel(self.countMode)
        self.countSpeak.setGeometry(QtCore.QRect(540, 220, 321, 191))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.countSpeak.setFont(font)
        self.countSpeak.setObjectName("countSpeak")
        # 제한모드 입력란
        self.countLine = QtWidgets.QLineEdit(self.countMode)
        self.countLine.setGeometry(QtCore.QRect(280, 580, 281, 71))
        self.countLine.setObjectName("countLine")
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(30)
        self.countLine.setFont(font)
        self.countLine.setStyleSheet("border: 2px solid black;"
                                     "border-radius: 5px;")
        # 제한모드 시도 버튼
        self.countTryBtn = QtWidgets.QPushButton(self.countMode)
        self.countTryBtn.setGeometry(QtCore.QRect(570, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.countTryBtn.setFont(font)
        self.countTryBtn.setObjectName("countTryBtn")
        self.countTryBtn.clicked.connect(self.count_guessing)  # 시도 버튼 클릭 시
        self.countTryBtn.setStyleSheet("color: white;"
                                       "background-color: rgb(20, 173, 3);"
                                       "border: 3px solid rgb(28, 89, 21);"
                                       "border-radius: 5px;")

        # 제한모드 다시 버튼
        self.countRetryBtn = QtWidgets.QPushButton(self.countMode)
        self.countRetryBtn.setGeometry(QtCore.QRect(660, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.countRetryBtn.setFont(font)
        self.countRetryBtn.setObjectName("countRetryBtn")
        self.countRetryBtn.clicked.connect(self.count_reset)  # 다시 버튼 클릭 시
        self.countRetryBtn.setStyleSheet("color: white;"
                                         "background-color: rgb(236, 32, 37);"
                                         "border: 3px solid rgb(107, 20, 21);"
                                         "border-radius: 5px;")

        # 제한모드 카운트
        self.countCount = QtWidgets.QLabel(self.countMode)
        self.countCount.setGeometry(QtCore.QRect(390, 90, 281, 91))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(50)
        self.countCount.setFont(font)
        self.countCount.setObjectName("countCount")
        MainWindow.setCentralWidget(self.centralwidget)

        # 시간모드 화면 ------------------
        # 시간모드 화면설정
        self.clockMode = QtWidgets.QWidget(self.centralwidget)
        self.clockMode.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.clockMode.setStyleSheet("background-color: white")
        self.clockMode.setObjectName("clockMode")
        # 시간모드 뒤로가기 버튼
        self.clockBackBtn = QtWidgets.QPushButton(self.clockMode)
        self.clockBackBtn.setGeometry(QtCore.QRect(15, 15, 55, 55))
        self.clockBackBtn.setStyleSheet("border: none;"
                                        "background-image: url(뒤로가기.png);")
        self.clockBackBtn.setText("")
        self.clockBackBtn.setObjectName("clockBackBtn")
        self.clockBackBtn.clicked.connect(self.clock_back)  # 뒤로가기 버튼 클릭 시

        # 시간모드 제목
        self.clockTitle = QtWidgets.QLabel(self.clockMode)
        self.clockTitle.setGeometry(QtCore.QRect(450, 20, 111, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(40)
        self.clockTitle.setFont(font)
        self.clockTitle.setObjectName("clockTitle")
        # 시간모드 사진
        self.clockImage = QtWidgets.QLabel(self.clockMode)
        self.clockImage.setGeometry(QtCore.QRect(70, 80, 550, 600))
        self.clockImage.setStyleSheet("image: url(기본.png);")
        self.clockImage.setText("")
        self.clockImage.setObjectName("clockImage")
        # 시간모드 진행 상황 설명글
        self.clockSpeak = QtWidgets.QLabel(self.clockMode)
        self.clockSpeak.setGeometry(QtCore.QRect(540, 220, 321, 191))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.clockSpeak.setFont(font)
        self.clockSpeak.setObjectName("clockSpeak")
        # 시간모드 입력란
        self.clockLine = QtWidgets.QLineEdit(self.clockMode)
        self.clockLine.setGeometry(QtCore.QRect(280, 580, 281, 71))
        self.clockLine.setObjectName("clockLine")
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(30)
        self.clockLine.setFont(font)
        self.clockLine.setStyleSheet("border: 2px solid black;"
                                     "border-radius: 5px;")
        # 시간모드 시도 버튼
        self.clockTryBtn = QtWidgets.QPushButton(self.clockMode)
        self.clockTryBtn.setGeometry(QtCore.QRect(570, 580, 81, 71))
        self.clockTryBtn.setStyleSheet("color: white;"
                                       "background-color: rgb(20, 173, 3);"
                                       "border: 3px solid rgb(28, 89, 21);"
                                       "border-radius: 5px;")
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.clockTryBtn.setFont(font)
        self.clockTryBtn.setObjectName("clockTryBtn")
        self.clockTryBtn.clicked.connect(self.clock_guessing)  # 시도 버튼 클릭 시

        # 시간모드 다시 버튼
        self.clockRetryBtn = QtWidgets.QPushButton(self.clockMode)
        self.clockRetryBtn.setGeometry(QtCore.QRect(660, 580, 81, 71))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(25)
        self.clockRetryBtn.setFont(font)
        self.clockRetryBtn.setObjectName("clockRetryBtn")
        self.clockRetryBtn.setStyleSheet("color: white;"
                                         "background-color: rgb(236, 32, 37);"
                                         "border: 3px solid rgb(107, 20, 21);"
                                         "border-radius: 5px;")
        self.clockRetryBtn.clicked.connect(self.clock_reset)  # 시도 버튼 클릭 시

        # 시간모드 타이머
        self.clockClock = QtWidgets.QLabel(self.clockMode)
        self.clockClock.setGeometry(QtCore.QRect(430, 100, 161, 91))
        font = QtGui.QFont()
        font.setFamily("온글잎 의연체")
        font.setPointSize(60)
        self.clockClock.setFont(font)
        self.clockClock.setObjectName("clockClock")
        self.myTimer = QtCore.QTimer(self.clockMode)

        # retranslateUi 호출
        self.retranslateUi(MainWindow)

        # === 화면 전환 방법 ===
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
        self.clockModeBtn.clicked.connect(self.startTimer)  # 타이머 실행

        # 시간모드 뒤로가기 버튼 눌렀을 때
        self.clockBackBtn.clicked.connect(self.clockMode.hide)  # 시간모드 화면 가림
        self.clockBackBtn.clicked.connect(self.main.show)  # 메인 화면 보임

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # === 셋팅 ===
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "교수님이 생각하신 숫자는?"))
        self.mainTitle.setText(_translate("MainWindow", "교수님이 생각하신 숫자는?"))
        self.basicModeBtn.setText(_translate("MainWindow", "기본 모드"))
        self.countModeBtn.setText(_translate("MainWindow", "제한 모드"))
        self.clockModeBtn.setText(_translate("MainWindow", "시간 모드"))
        self.mainTitle_2.setText(_translate(
            "MainWindow", " 03분반 20212195 이상희"))
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
        # 처음 실행했을 때
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
