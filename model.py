from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt5.QtGui import QColor, QBrush
import numpy as np
import pandas as pd
from algorithms import vald, bayes, savidge, gurvits

class GameModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._data = np.zeros((2, 2))
        self.result = None
        self._strategys = ["Стратегия 1", "Стратегия 2"]
        self._states = ["Состояние 1", "Состояние 2"]
        self._probabilities = [0, 0]


    def rowCount(self, parent: QModelIndex = ...) -> int:
        r, c = self._data.shape
        return r

    def columnCount(self, parent: QModelIndex = ...) -> int:
        r, c = self._data.shape
        return c

    def setData(self, index: QModelIndex, value, role: int = ...) -> bool:
        i = index.row()
        j = index.column()
        if role == Qt.EditRole or role == Qt.DisplayRole:
            try:
                self._data[i, j] = float(value)
            except Exception:
                value = float(value.replace(',', '.'))
                self._data[i, j] = float(value)
            self.dataChanged.emit(index, index)
            return True
        return False

    def data(self, index: QModelIndex, role: int = ...):
        i = index.row()
        j = index.column()
        if role == Qt.EditRole or role == Qt.DisplayRole:
           return float(self._data[i, j])

        if role == Qt.BackgroundColorRole:
            if i % 2 == 0:
                return QBrush(QColor('#c5e6bc'))
            else:
                # deffde
                return QBrush(QColor('#f0ffeb'))

        return QVariant()

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if orientation == Qt.Horizontal:
                return self._states[section]
            else:
                return self._strategys[section]
        return QVariant()

    def setHeaderData(self, section: int, orientation: Qt.Orientation, value, role: int = ...) -> bool:
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if orientation == Qt.Horizontal:
                self._states[section] = str(value)
            else:
                self._strategys[section] = str(value)
            self.headerDataChanged.emit(orientation, section, section)
            return True
        return False

    def insertRow(self, row: int, parent: QModelIndex = ...) -> bool:
        try:
            self.beginInsertRows(parent, row, row)
            self._data = np.vstack((self._data, np.zeros((1, self.columnCount()))))
            self._strategys.append(f'Стратегия {row + 1}')
            self.endInsertRows()
            return True
        except Exception:
            return False

    def removeRow(self, row: int, parent: QModelIndex = ...) -> bool:
        try:
            self.beginRemoveRows(parent, row, row)
            self._data = np.delete(self._data, row, axis=0)
            self._strategys = self._strategys[:row] + self._strategys[row+1:]
            self.endRemoveRows()
            return True
        except Exception:
            return False

    def addStrategy(self):
        self.insertRow(self.rowCount(), QModelIndex())

    def deleteStrategy(self):
        if self.rowCount() > 1:
            self.removeRow(self.rowCount()-1, QModelIndex())

    def insertColumn(self, column: int, parent: QModelIndex = ...) -> bool:
        try:
            self.beginInsertColumns(parent, column, column)
            self._data = np.hstack((self._data, np.zeros((self.rowCount(), 1))))
            self._states.append(f'Состояние {column+1}')
            self._probabilities.append(0)
            self.endInsertColumns()
            return True
        except Exception:
            return False

    def removeColumn(self, column: int, parent: QModelIndex = ...) -> bool:
        try:
            self.beginRemoveColumns(parent, column, column)
            self._data = np.delete(self._data, column, axis=1)
            self._states = self._states[:column] + self._states[column+1:]
            self._probabilities = self._probabilities[:column] + self._probabilities[column + 1:]
            self.endRemoveColumns()
            return True
        except Exception:
            return False

    def addState(self):
        self.insertColumn(self.columnCount(), QModelIndex())

    def deleteState(self):
        if self.columnCount() > 1:
            self.removeColumn(self.columnCount()-1, QModelIndex())

    def copy(self):
        copy = GameModel()
        copy._data = self._data.copy()
        copy._states = self._states.copy()
        copy._strategys = self._strategys.copy()
        copy._probabilities = self._probabilities.copy()
        return copy

    def setfromObj(self, model):
        self.beginResetModel()
        self._data = model._data
        self._strategys = model._strategys
        self._states = model._states
        self._probabilities = model._probabilities
        self.endResetModel()

    def solve(self, criterion, weight=None):
        if criterion == 'vald':
            return vald(self._data, self._strategys, self._states)
        elif criterion == 'bayes':
            if sum(self._probabilities) > 1 or sum(self._probabilities) < 0.99:
                return 'Ошибка'
            return bayes(self._data, self._strategys, self._states, self._probabilities)
        elif criterion == 'savidge':
            return savidge(self._data, self._strategys, self._states)
        elif criterion == 'gurvits':
            if weight is None:
                return gurvits(self._data, self._strategys, self._states, 0.5)
            else:
                return gurvits(self._data, self._strategys, self._states, weight)

    def saveGame(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\
                        <html><head><meta name="qrichtext" content="1" /><style type="text/css">\
                        p, li { white-space: pre-wrap; }\
                        </style></head><body style=" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;">\r\n')
            file.write('<h2>Матрица решений:</h2>\r\n')
            data = pd.DataFrame(self._data, index=self._strategys, columns=self._states)
            data.loc['Вероятность'] = self._probabilities
            file.write(data.to_html())

    def loadGame(self, filename):
        self.beginResetModel()
        data = pd.read_html(filename, encoding='utf-8', index_col=0)[0]
        self._data = data[:-1].values
        self._states = list(data.columns.values)
        self._strategys = list(data.index.values)[:-1]
        self._probabilities = list(data.values[-1].astype('float64'))
        self.endResetModel()

class GamePropertiesModel(QAbstractTableModel):
    def __init__(self, parentGame:GameModel):
        super().__init__()
        self.game = parentGame
        self.game.columnsInserted.connect(self.addColumns)
        self.game.columnsRemoved.connect(self.deleteColumns)
        self.game.modelReset.connect(self.update)
        self.game.headerDataChanged.connect(self.updateHeader)


    def rowCount(self, parent: QModelIndex = ...) -> int:
        return 1

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self.game.columnCount()

    def setData(self, index: QModelIndex, value, role: int = ...) -> bool:
        j = index.column()
        if role == Qt.EditRole or role == Qt.DisplayRole:
            try:
                if float(value) <= 1 and float(value) >=0:
                    self.game._probabilities[j] = float(value)
            except Exception:
                value = float(value.replace(',', '.'))
                if float(value) <= 1 and float(value) >=0:
                    self.game._probabilities[j] = float(value)
            self.dataChanged.emit(index, index)
            return True
        return False

    def data(self, index: QModelIndex, role: int = ...):
        j = index.column()
        if role == Qt.EditRole or role == Qt.DisplayRole:
           return float(self.game._probabilities[j])

        if role == Qt.BackgroundColorRole:
           return QBrush(QColor('#f0ffeb'))
        return QVariant()

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if orientation == Qt.Horizontal:
                return self.game._states[section]
            else:
                return 'Вероятность'
        return QVariant()

    def addColumns(self, parent, first, last):
        self.beginInsertColumns(parent, first, last)
        self.endInsertColumns()

    def deleteColumns(self, parent, first, last):
        self.beginRemoveColumns(parent, first, last)
        self.endRemoveColumns()

    def update(self):
        self.beginResetModel()
        self.endResetModel()

    def updateHeader(self,  section: int, orientation: Qt.Orientation, value, role: int = ...):
        self.headerDataChanged.emit(orientation, section, section)
