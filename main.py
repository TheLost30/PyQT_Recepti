import sqlite3
import sys
from os import startfile
# файл со всеми UI
from setupUI import *
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QApplication, QMainWindow


class CancelledException(Exception):
    def __init__(self):
        super().__init__('process calcelled')


class CookingApp(QMainWindow, MainWindowGUI):
    def __init__(self):
        super().__init__()
        # установка интерфейса
        self.setupUi(self)
        self.name_ing_desc = None
        # соединение кнопки с функцией создания рецепта
        self.create_recipe_button.clicked.connect(self.create_recipe)
        # соединение кнопки с функцией просмотра рецептов
        self.all_recipes.clicked.connect(self.recipes_list)

    def keyPressEvent(self, pressed):
        if pressed.key() == 16777264:  # открытие справки на F1
            startfile(r"Data\help.txt")

    def recipes_list(self):
        # удаление сообщения со статусбара для красоты
        self.statusBar().showMessage('')
        # спрятать главное окно
        self.showMinimized()
        # инициализация окна с рецептами
        rec_d = RecipesListDialog()
        # отображение окна
        rec_d.showMinimized()
        rec_d.showNormal()

        # создание цикла - нужно, чтобы функция не продолжала работать, пока окно не закроется
        loop = QEventLoop()
        rec_d.destroyed.connect(loop.quit)
        loop.exec()

        if not rec_d.opened:  # если не нажата кнопка открыть
            # после закрытия отобразить главное окно
            self.showNormal()
            # создание ошибки, чтобы функция не продолжала работать
            raise CancelledException

        # сохранить выбранное навание рецепта
        chosen_item = rec_d.chosen_item

        # подключение библиотеки
        con = sqlite3.connect("Data/recipes.db")
        cur = con.cursor()
        # команда для сохранения данных со строки, где находится такое же имя
        que = f"SELECT * FROM recipes WHERE name = '{chosen_item}'"

        # сохранение данных со строки, где находится такое же имя
        result = [*cur.execute(que).fetchall()[0]]
        # акрытие библиотеки
        con.close()
        # разделение шагов, т.к. они хранятся в одной строке
        result[3:] = result[3].split('\U00013432')
        # создание словаря
        result = [result[0], {i + 1: result[i + 1] for i in range(len(result) - 1)}]
        # инициализация окна шагов
        s_dial = StepsDialog(steps=result)
        # отображение окна
        s_dial.showMinimized()
        s_dial.showNormal()
        # создание цикла
        s_dial.destroyed.connect(loop.quit)
        loop.exec()
        # после закрытия отобразить главное окно
        self.showNormal()

    def create_recipe(self):
        # удаление сообщения со статусбара для красоты
        self.statusBar().showMessage('')
        # спрятать главное окно
        self.showMinimized()
        # инициализация окна для создания рецепта
        dial = DialogForRecipe()
        # отображение окна
        dial.showMinimized()
        dial.showNormal()

        # создание цикла
        loop = QEventLoop()
        dial.destroyed.connect(loop.quit)
        loop.exec()

        # получение названия, ингридиентов и описание рецепта
        self.name_ing_desc = dial.name_ing_desc

        # создание строки для проверки данных
        line = ''.join(self.name_ing_desc)
        # если стока пустая, значит действие было отменено или окно было закрыто пользователем
        if line == '':
            # отображение главного окна
            self.showNormal()
            # сообщение в статурбаре, что действие было отменено
            self.statusBar().showMessage('Действие отменено')
            # создание ошибки, чтобы функция не продолжала работать
            raise CancelledException

        # инициализация окна для шагов
        s_dial = StepsDialog()
        # отправление данных рецепта в функцию (по другому не получилось)
        s_dial.get_data(self.name_ing_desc)

        # отображение окна
        s_dial.show()
        # создание цикла
        s_dial.destroyed.connect(loop.quit)
        loop.exec()
        # отображение главного окна
        self.showNormal()
        # проверка на заполнение шагов
        if any(s_dial.steps.values()):  # если есть хотя бы 1 заполненный шаг
            # сообщение на статусбаре "Добавлено"
            self.statusBar().showMessage('Добавлено')
        else:
            # сообщение на статусбаре "Дейстие отменено"
            self.statusBar().showMessage('Действие отменено')


class DialogForRecipe(QMainWindow, DialogUI):
    def __init__(self):
        super().__init__()
        self.name_ing_desc = []
        # подключение библиотеки
        self.con = sqlite3.connect("Data/recipes.db").cursor()
        # командадля получения всех названий
        self.que = "SELECT name FROM recipes"
        # выполнение команды и перевод в список строк (т.к. по умолчанию это список кортежей)
        self.names_list = [str(i[0]) for i in self.con.execute(self.que).fetchall()]
        # установка интерфейса
        self.setupUi(self)
        # соединение кнопки с функцией закрытия окна
        self.cancel_button.clicked.connect(self.close)
        # соединение кнопки с функцией отображением результата
        self.ok_button.clicked.connect(self.result)

    def result(self):
        if not self.check_for_errors():  # если не было найдено ошибок
            # сохранение данных в список
            self.name_ing_desc = [self.name_text.text().replace("'", '"'),
                                  self.ingridients_text.toPlainText().replace("'", '"'),
                                  self.description_text.toPlainText().replace("'", '"')]
            # закрытие окна
            self.close()

    def check_for_errors(self):
        # флаг нужен для проверки на ошибки
        flag = 0
        if not self.name_text.text():  # если название не заполнено
            # отобжажение ошибки
            self.name_error.setText('Придумайте название')
            flag = 1
        elif self.name_text.text() in self.names_list:
            self.name_error.setText('Такое название уже есть, придумайте новое')
            flag = 1
        else:
            self.name_error.setText('')

        if not self.ingridients_text.toPlainText():  # если ингридиенты не заполнены
            # отобжажение ошибки
            self.ingridients_error.setText('Заполните ингридиенты')
            flag = 1
        else:
            self.ingridients_error.setText('')

        if not self.description_text.toPlainText():  # если описание не заполнено
            # отобжажение ошибки
            self.description_error.setText('Заполните описание')
            flag = 1
        else:
            self.description_error.setText('')
        # если ошибки были, то фукция вернёт правду
        return flag


class StepsDialog(QMainWindow, StepsDialogGUI):
    def __init__(self, steps=[]):
        super().__init__()
        # установка интерфейса
        self.setupUi(self)
        self.name_ing_desc = None
        # счетчик [на какой странице сейчас, всего страниц]
        self.count = [1, 1]
        # шаги
        self.steps = {}
        # режим программы
        self.mode = 'write'
        # соединение кнопки с функцией переворота страницы
        self.right_button.clicked.connect(self.turn_step)
        # соединение кнопки с функцией переворота страницы
        self.left_button.clicked.connect(self.turn_step)
        if steps:  # если при инициализации подаются шаги, то окно
            # переходит в режим чтения
            self.mode = 'read'
            # принимает шаги
            self.steps = steps[1]
            self.setWindowTitle(str(steps[0]))
            self.count = [1, len(self.steps.values())]
            # меняет кнопку сохранения на кнопку закрытия
            self.save_button.setText("Закрыть")
            self.save_button.clicked.connect(self.close)
            # ставит режим чтения
            self.step.setReadOnly(True)
            # выставляет значения из словаря
            self.step.setPlainText(str(self.steps[self.count[0]]))
            self.steps_counter.setText(f'{self.count[0]}/{self.count[1]}')
        else:  # если не словаря, то
            # оставляет функцию сохранения у кнопки сохранения
            self.save_button.clicked.connect(self.save)

    def turn_step(self):
        # сохранение прошлого шага
        self.steps[self.count[0]] = self.step.toPlainText()
        if self.sender().text() == 'forward':  # если нажимается кнопка вправо (на ней текст "вперед")
            if self.count[0] == self.count[1]:  # если нынешняя страница совпадает с последней
                if self.mode == 'write':
                    # кратко: если пользователь листает вперед в режиме редактирования, то страница добавляется
                    self.count = [self.count[0] + 1, self.count[1] + 1]
                    # и добавляется пустой шаг
                    self.steps[self.count[0]] = ''
                elif self.mode == 'read':
                    # но если пользователь листнет вперед в режиме чтения, то новые страницы не добавятся
                    pass
            else:  # если нынешняя страница не совпадает с последней
                # то перелистывается с нынешней на следующюю
                self.count[0] += 1
        # если нажимается кнопка влево (на ней текст "назад")
        elif self.sender().text() == 'back':
            # то страница листается назад, с условием, что она не может уйти ниже 1
            self.count[0] -= 1 if self.count[0] != 1 else 0
        # отображение шага в зависимости от страницы
        self.step.setPlainText(str(self.steps[self.count[0]]))
        # отображение номера страницы
        self.steps_counter.setText(f'{self.count[0]}/{self.count[1]}')

    def save(self):
        # сохранение последнего шага
        self.steps[self.count[0]] = self.step.toPlainText()
        # подключение библиотеки
        con = sqlite3.connect('Data/recipes.db')
        # перевод шагов из словаря в строку
        steps = '𓐲'.join([i.replace('𓐲', '') for i in self.steps.values() if i and not i.isspace()])

        name, ingridients, description = self.name_ing_desc
        # создание команды для добавления рецепта в базу
        command = f'INSERT INTO recipes (name,ingridients,description,steps)' \
                  f"VALUES ('{name}','{ingridients}','{description}','{steps}');"
        # выполнение команды
        con.cursor().execute(command)
        # сохранение изменений
        con.commit()
        # закрытие библиотеки
        con.close()
        # закрытие окна
        self.close()

    # получение данных
    def get_data(self, n):
        self.name_ing_desc = n


class RecipesListDialog(QMainWindow, RecipesListGUI):
    def __init__(self):
        super().__init__()
        # установка интерфейса
        self.setupUi(self)
        # подключение библиотеки
        self.con = sqlite3.connect("Data/recipes.db")
        self.cur = self.con.cursor()
        self.refresh_list()
        # соединение кнопки с функцией
        self.open_button.clicked.connect(self.open_recipe)
        # соединение выбора элемента в списке с функцией
        self.list.itemClicked.connect(self.item_choose)
        self.delete_button.clicked.connect(self.delete_recipe)
        # выбранный рецепт
        self.chosen_item = None
        self.opened = 0

    def refresh_list(self):
        # командадля получения всех названий
        self.que = "SELECT name FROM recipes"
        # выполнение команды и перевод в список строк (т.к. по умолчанию это список кортежей)
        self.result = [str(i[0]) for i in self.cur.execute(self.que).fetchall()]
        # очистка листа
        self.list.clear()
        # вставка всех названий в лист
        self.list.insertItems(len(self.result) + 1, self.result)

    def item_choose(self, item):
        # получение выбранного рецепта
        self.chosen_item = item.text()

    def open_recipe(self):
        if self.chosen_item:  # если рецепт выбран
            self.con.close()  # библиотека закрывается
            self.opened = 1
            self.close()  # окно закрывается
        else:  # если рецепт не выбран
            # отображение сообщения, что рецепт не выбран
            self.statusBar().showMessage('Выберите рецепт')

    def delete_recipe(self):
        if self.chosen_item:  # если рецепт выбран
            # команда для библиотеки
            self.que = f"DELETE FROM recipes WHERE name = {self.chosen_item};"
            # выполнение команды в библиотеке
            self.cur.execute(self.que)
            # сохранение изменений
            self.con.commit()
            # обновление листа
            self.chosen_item = None
            self.refresh_list()
        else:  # если рецепт не выбран
            # отображение сообщения, что рецепт не выбран
            self.statusBar().showMessage('Выберите рецепт')


# функция для отображения ошибок
def exception_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    # инициализациализация класса
    C_app = CookingApp
    # какие-то строки из учебника (я надеюсь это не плагиат?)
    _exe = QApplication(sys.argv)
    # открытие окна
    window = C_app()
    window.show()
    # отображение ошибок в коде
    sys.excepthook = exception_hook
    # ещё одна важная строка из учебника
    sys.exit(_exe.exec_())
