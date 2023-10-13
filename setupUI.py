from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class DialogUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 420)
        MainWindow.setMinimumSize(QtCore.QSize(330, 250))
        MainWindow.setAttribute(Qt.WA_DeleteOnClose)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Data/recipe_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1, 1))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setKerning(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setToolTip("")
        self.centralwidget.setStatusTip("")
        self.centralwidget.setWhatsThis("")
        self.centralwidget.setAccessibleName("")
        self.centralwidget.setAccessibleDescription("")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.ingLayout = QtWidgets.QHBoxLayout()
        self.ingLayout.setObjectName("ingLayout")
        self.ingridients = QtWidgets.QLabel(self.centralwidget)
        self.ingridients.setMinimumSize(QtCore.QSize(0, 0))
        self.ingridients.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ingridients.setSizeIncrement(QtCore.QSize(0, 0))
        self.ingridients.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.ingridients.setFont(font)
        self.ingridients.setMouseTracking(False)
        self.ingridients.setTabletTracking(False)
        self.ingridients.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ingridients.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.ingridients.setAcceptDrops(False)
        self.ingridients.setToolTip("")
        self.ingridients.setStatusTip("")
        self.ingridients.setWhatsThis("")
        self.ingridients.setAccessibleName("")
        self.ingridients.setAccessibleDescription("")
        self.ingridients.setObjectName("ingridients")
        self.ingLayout.addWidget(self.ingridients)
        self.ingridients_error = QtWidgets.QLabel(self.centralwidget)
        self.ingridients_error.setMinimumSize(QtCore.QSize(0, 0))
        self.ingridients_error.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ingridients_error.setSizeIncrement(QtCore.QSize(0, 0))
        self.ingridients_error.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.ingridients_error.setFont(font)
        self.ingridients_error.setMouseTracking(False)
        self.ingridients_error.setTabletTracking(False)
        self.ingridients_error.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ingridients_error.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.ingridients_error.setAcceptDrops(False)
        self.ingridients_error.setToolTip("")
        self.ingridients_error.setStatusTip("")
        self.ingridients_error.setWhatsThis("")
        self.ingridients_error.setAccessibleName("")
        self.ingridients_error.setAccessibleDescription("")
        self.ingridients_error.setStyleSheet("font-weight: bold; color: red")
        self.ingridients_error.setText("")
        self.ingridients_error.setTextFormat(QtCore.Qt.RichText)
        self.ingridients_error.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ingridients_error.setObjectName("ingridients_error")
        self.ingLayout.addWidget(self.ingridients_error)
        self.gridLayout.addLayout(self.ingLayout, 6, 1, 1, 2)
        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setMinimumSize(QtCore.QSize(0, 0))
        self.name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.name.setSizeIncrement(QtCore.QSize(0, 0))
        self.name.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.name.setFont(font)
        self.name.setMouseTracking(False)
        self.name.setTabletTracking(False)
        self.name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.name.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.name.setAcceptDrops(False)
        self.name.setToolTip("")
        self.name.setStatusTip("")
        self.name.setWhatsThis("")
        self.name.setAccessibleName("")
        self.name.setAccessibleDescription("")
        self.name.setObjectName("name")
        self.nameLayout.addWidget(self.name)
        self.name_error = QtWidgets.QLabel(self.centralwidget)
        self.name_error.setMinimumSize(QtCore.QSize(0, 0))
        self.name_error.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.name_error.setSizeIncrement(QtCore.QSize(0, 0))
        self.name_error.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.name_error.setFont(font)
        self.name_error.setMouseTracking(False)
        self.name_error.setTabletTracking(False)
        self.name_error.setFocusPolicy(QtCore.Qt.NoFocus)
        self.name_error.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.name_error.setAcceptDrops(False)
        self.name_error.setToolTip("")
        self.name_error.setStatusTip("")
        self.name_error.setWhatsThis("")
        self.name_error.setAccessibleName("")
        self.name_error.setAccessibleDescription("")
        self.name_error.setStyleSheet("font-weight: bold; color: red")
        self.name_error.setText("")
        self.name_error.setTextFormat(QtCore.Qt.RichText)
        self.name_error.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_error.setObjectName("name_error")
        self.nameLayout.addWidget(self.name_error)
        self.gridLayout.addLayout(self.nameLayout, 2, 1, 1, 2)
        self.ingridients_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ingridients_text.setObjectName("ingridients_text")
        self.gridLayout.addWidget(self.ingridients_text, 9, 1, 1, 2)
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 13, 1, 1, 1)
        self.description_text = QtWidgets.QTextEdit(self.centralwidget)
        self.description_text.setObjectName("description_text")
        self.gridLayout.addWidget(self.description_text, 12, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 10, 1)
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 13, 2, 1, 1)
        self.name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.name_text.setObjectName("name_text")
        self.gridLayout.addWidget(self.name_text, 5, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 3, 10, 1)
        self.descLayout = QtWidgets.QHBoxLayout()
        self.descLayout.setObjectName("descLayout")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setMinimumSize(QtCore.QSize(0, 0))
        self.description.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.description.setSizeIncrement(QtCore.QSize(0, 0))
        self.description.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.description.setFont(font)
        self.description.setMouseTracking(False)
        self.description.setTabletTracking(False)
        self.description.setFocusPolicy(QtCore.Qt.NoFocus)
        self.description.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.description.setAcceptDrops(False)
        self.description.setToolTip("")
        self.description.setStatusTip("")
        self.description.setWhatsThis("")
        self.description.setAccessibleName("")
        self.description.setAccessibleDescription("")
        self.description.setObjectName("description")
        self.descLayout.addWidget(self.description)
        self.description_error = QtWidgets.QLabel(self.centralwidget)
        self.description_error.setMinimumSize(QtCore.QSize(0, 0))
        self.description_error.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.description_error.setSizeIncrement(QtCore.QSize(0, 0))
        self.description_error.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.description_error.setFont(font)
        self.description_error.setMouseTracking(False)
        self.description_error.setTabletTracking(False)
        self.description_error.setFocusPolicy(QtCore.Qt.NoFocus)
        self.description_error.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.description_error.setAcceptDrops(False)
        self.description_error.setToolTip("")
        self.description_error.setStatusTip("")
        self.description_error.setWhatsThis("")
        self.description_error.setAccessibleName("")
        self.description_error.setAccessibleDescription("")
        self.description_error.setStyleSheet("font-weight: bold; color: red")
        self.description_error.setText("")
        self.description_error.setTextFormat(QtCore.Qt.RichText)
        self.description_error.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.description_error.setObjectName("description_error")
        self.descLayout.addWidget(self.description_error)
        self.gridLayout.addLayout(self.descLayout, 10, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Новый рецепт"))
        self.ingridients.setText(_translate("MainWindow", "Ингридиенты"))
        self.name.setText(_translate("MainWindow", "Название"))
        self.ok_button.setText(_translate("MainWindow", "Ок"))
        self.cancel_button.setText(_translate("MainWindow", "Отмена"))
        self.description.setText(_translate("MainWindow", "Описание"))


class MainWindowGUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 387)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Data/recipe_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setToolTip("")
        self.logo.setStatusTip("")
        self.logo.setWhatsThis("")
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.PlainText)
        self.logo.setPixmap(QtGui.QPixmap("Data/recipe book_logo.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setIndent(-1)
        self.logo.setOpenExternalLinks(False)
        self.logo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)
        self.all_recipes = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_recipes.sizePolicy().hasHeightForWidth())
        self.all_recipes.setSizePolicy(sizePolicy)
        self.all_recipes.setMinimumSize(QtCore.QSize(0, 0))
        self.all_recipes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.all_recipes.setSizeIncrement(QtCore.QSize(0, 0))
        self.all_recipes.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        self.all_recipes.setFont(font)
        self.all_recipes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.all_recipes.setMouseTracking(False)
        self.all_recipes.setTabletTracking(False)
        self.all_recipes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.all_recipes.setAcceptDrops(False)
        self.all_recipes.setToolTip("")
        self.all_recipes.setStatusTip("")
        self.all_recipes.setWhatsThis("")
        self.all_recipes.setAccessibleName("")
        self.all_recipes.setAccessibleDescription("")
        self.all_recipes.setCheckable(False)
        self.all_recipes.setAutoRepeat(False)
        self.all_recipes.setAutoExclusive(False)
        self.all_recipes.setAutoDefault(False)
        self.all_recipes.setDefault(False)
        self.all_recipes.setFlat(False)
        self.all_recipes.setObjectName("all_recipes")
        self.gridLayout.addWidget(self.all_recipes, 2, 0, 1, 1)
        self.create_recipe_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_recipe_button.sizePolicy().hasHeightForWidth())
        self.create_recipe_button.setSizePolicy(sizePolicy)
        self.create_recipe_button.setMinimumSize(QtCore.QSize(0, 0))
        self.create_recipe_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.create_recipe_button.setSizeIncrement(QtCore.QSize(0, 0))
        self.create_recipe_button.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        self.create_recipe_button.setFont(font)
        self.create_recipe_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_recipe_button.setMouseTracking(False)
        self.create_recipe_button.setTabletTracking(False)
        self.create_recipe_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.create_recipe_button.setAcceptDrops(False)
        self.create_recipe_button.setToolTip("")
        self.create_recipe_button.setStatusTip("")
        self.create_recipe_button.setWhatsThis("")
        self.create_recipe_button.setAccessibleName("")
        self.create_recipe_button.setAccessibleDescription("")
        self.create_recipe_button.setCheckable(False)
        self.create_recipe_button.setAutoRepeat(False)
        self.create_recipe_button.setAutoExclusive(False)
        self.create_recipe_button.setAutoDefault(False)
        self.create_recipe_button.setDefault(False)
        self.create_recipe_button.setFlat(False)
        self.create_recipe_button.setObjectName("create_recipe_button")
        self.gridLayout.addWidget(self.create_recipe_button, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кулинарное приложение"))
        self.all_recipes.setText(_translate("MainWindow", "Посмотреть свои рецепты"))
        self.create_recipe_button.setText(_translate("MainWindow", "Написать рецепт"))


class StepsDialogGUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 516)
        MainWindow.setAttribute(Qt.WA_DeleteOnClose)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Data/recipe_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.right_button = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_button.sizePolicy().hasHeightForWidth())
        self.right_button.setSizePolicy(sizePolicy)
        self.right_button.setMinimumSize(QtCore.QSize(70, 70))
        self.right_button.setArrowType(QtCore.Qt.RightArrow)
        self.right_button.setObjectName("right_button")
        self.gridLayout.addWidget(self.right_button, 4, 3, 1, 1)
        self.left_button = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_button.sizePolicy().hasHeightForWidth())
        self.left_button.setSizePolicy(sizePolicy)
        self.left_button.setMinimumSize(QtCore.QSize(70, 70))
        self.left_button.setArrowType(QtCore.Qt.LeftArrow)
        self.left_button.setObjectName("left_button")
        self.gridLayout.addWidget(self.left_button, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 5, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 5, 1)
        self.step = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.step.setObjectName("step")
        self.gridLayout.addWidget(self.step, 1, 1, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.steps_counter = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.steps_counter.sizePolicy().hasHeightForWidth())
        self.steps_counter.setSizePolicy(sizePolicy)
        self.steps_counter.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.steps_counter.setFont(font)
        self.steps_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.steps_counter.setObjectName("steps_counter")
        self.verticalLayout.addWidget(self.steps_counter)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)
        self.gridLayout.addLayout(self.verticalLayout, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шаги"))
        self.right_button.setText(_translate("MainWindow", "forward"))
        self.left_button.setText(_translate("MainWindow", "back"))
        self.steps_counter.setText(_translate("MainWindow", "1/1"))
        self.save_button.setText(_translate("MainWindow", "Сохранить"))


class RecipesListGUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 414)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setAttribute(Qt.WA_DeleteOnClose)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Data/recipe_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setObjectName("list")
        self.gridLayout.addWidget(self.list, 0, 2, 1, 3)
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setObjectName("open_button")
        self.gridLayout.addWidget(self.open_button, 1, 4, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Рецепты"))
        self.open_button.setText(_translate("MainWindow", "Открыть"))
        self.delete_button.setText(_translate("MainWindow", "Удалить"))