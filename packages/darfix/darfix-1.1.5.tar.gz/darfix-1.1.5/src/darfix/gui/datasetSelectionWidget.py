__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "14/10/2021"

import logging
import os
from typing import Optional

from silx.gui import qt
from silx.io.url import DataUrl
from silx.gui.dialog.DataFileDialog import DataFileDialog

from darfix.core.data_selection import load_process_data
from darfix import dtypes

_logger = logging.getLogger(__file__)


class DatasetSelectionWidget(qt.QTabWidget):
    """
    Widget that creates a dataset from a list of files or from a single filename.
    It lets the user add the first filename of a directory of files, or to
    upload manually each of the files to be read.
    If both options are filled up, only the files in the list of filenames
    are read.
    """

    sigProgressChanged = qt.Signal(int)

    def __init__(self, parent=None):
        qt.QTabWidget.__init__(self, parent)

        self._ish5CB = qt.QCheckBox("Is hdf5?")

        # Raw data
        self._rawFilenameData = FilenameSelectionWidget(parent=self)
        self._rawFilesData = FilesSelectionWidget(parent=self)
        self._onDiskCB = qt.QCheckBox("Keep data on disk", self)
        titleWidget = qt.QWidget(self)
        titleLayout = qt.QHBoxLayout()
        titleLabel = qt.QLabel("Workflow title:")
        self._titleLE = qt.QLineEdit("")
        self._HDF5MedataPath = DataPathSelection(
            text="metadata data path:", parent=self
        )
        titleLayout.addWidget(titleLabel)
        titleLayout.addWidget(self._titleLE)
        titleWidget.setLayout(titleLayout)
        rawData = qt.QWidget(self)
        rawData.setLayout(qt.QVBoxLayout())
        rawData.layout().addWidget(titleWidget)
        rawData.layout().addWidget(self._ish5CB)
        rawData.layout().addWidget(self._rawFilenameData)
        rawData.layout().addWidget(self._rawFilesData)
        rawData.layout().addWidget(self._HDF5MedataPath)
        rawData.layout().addWidget(self._onDiskCB)
        rawData.layout().addWidget(titleWidget)
        spacer = qt.QWidget(parent=self)
        spacer.setSizePolicy(qt.QSizePolicy.Minimum, qt.QSizePolicy.Expanding)
        rawData.layout().addWidget(spacer)
        self.addTab(rawData, "raw data")

        self._isH5 = False
        self._onDisk = False
        self._HDF5MedataPath.setVisible(False)

        # Dark data
        self._darkFilenameData = FilenameSelectionWidget(parent=self)
        self.addTab(self._darkFilenameData, "dark data")

        # Treated data
        self._treatedDirData = DirSelectionWidget(parent=self)
        self.addTab(self._treatedDirData, "treated data")

        self._dataset = None
        self.bg_dataset = None
        self.indices = None
        self.bg_indices = None

        # connect signal / slot
        self._ish5CB.stateChanged.connect(self.__isH5)
        self._onDiskCB.stateChanged.connect(self.__onDisk)
        self._rawFilenameData.filenameChanged.connect(self._fileNameChanged)

        # expose API
        self.getRawFilenames = self._rawFilesData.getFiles
        self.getRawFilename = self._rawFilenameData.getFilename
        self.getDarkFilename = self._darkFilenameData.getFilename
        self.setRawFilenames = self._rawFilesData.setFiles
        self.setDarkFilename = self._darkFilenameData.setFilename
        self.getTreatedDir = self._treatedDirData.getDir
        self.setTreatedDir = self._treatedDirData.setDir

    def loadDataset(self) -> bool:
        """
        Loads the dataset from the filenames.
        """
        dark_filename = self._darkFilenameData.getFilename()
        if dark_filename == "":
            dark_filename = None
        root_dir = self._treatedDirData.getDir()
        filenames = self._rawFilesData.getFiles()
        if not filenames:
            filenames = self._rawFilenameData.getFilename()
        (
            self._dataset,
            self.indices,
            self.bg_indices,
            self.bg_dataset,
        ) = load_process_data(
            filenames,
            root_dir=root_dir,
            in_memory=not self._onDisk,
            dark_filename=dark_filename,
            isH5=self._isH5,
            title=self._titleLE.text(),
            metadata_url=self._HDF5MedataPath.getMetadataUrl(),
        )
        return self.dataset is not None and self.dataset.nframes != 0

    def _updateDataset(self, dataset):
        self._dataset = dataset

    def _fileNameChanged(self):
        self._HDF5MedataPath.setHDF5File(self.getRawFilename())

    @property
    def dataset(self):
        return self._dataset

    def getDataset(self, parent) -> dtypes.OWDataset:
        return dtypes.OWDataset(
            parent, self._dataset, self.indices, self.bg_indices, self.bg_dataset
        )

    def updateProgress(self, progress):
        self.sigProgressChanged.emit(progress)

    def setIsH5(self, isH5: bool):
        self._ish5CB.setChecked(isH5)

    def __isH5(self, isH5):
        self._isH5 = isH5
        # set file selection (either any file or HDF5 file + data path)
        for widget in (self._rawFilenameData, self._darkFilenameData):
            assert isinstance(widget, FilenameSelectionWidget)
            widget.isHDF5(isH5=isH5)
        # show / hide multi raw files selection
        if isH5:
            self._rawFilesData.hide()
        else:
            self._rawFilesData.show()
        self._HDF5MedataPath.setVisible(isH5)

    def __onDisk(self, onDisk):
        self._onDisk = bool(onDisk)

    def setMetadataUrl(self, url: str):
        self._HDF5MedataPath.setDataPath(url)

    def getMetadataUrl(self) -> str:
        return self._HDF5MedataPath.getMetadataUrl()

    def setRawFilename(self, filename):
        self._rawFilenameData.setFilename(filename=filename)
        self._HDF5MedataPath.setHDF5File(filename=filename)


class FilesSelectionWidget(qt.QWidget):
    """
    Widget used to get one or more files from the computer and add them to a list.
    """

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self._files = []

        self.setLayout(qt.QVBoxLayout())
        self._table = self._init_table()
        self._addButton = qt.QPushButton("Add")
        self._rmButton = qt.QPushButton("Remove")
        self.layout().addWidget(self._table)
        self.layout().addWidget(self._addButton)
        self.layout().addWidget(self._rmButton)
        self._addButton.clicked.connect(self._addFiles)
        self._rmButton.clicked.connect(self._removeFiles)

    def _init_table(self):
        table = qt.QTableWidget(0, 1, parent=self)
        table.horizontalHeader().hide()
        # Resize horizontal header to fill all the column size
        if hasattr(table.horizontalHeader(), "setSectionResizeMode"):  # Qt5
            table.horizontalHeader().setSectionResizeMode(0, qt.QHeaderView.Stretch)
        else:  # Qt4
            table.horizontalHeader().setResizeMode(0, qt.QHeaderView.Stretch)

        return table

    def _addFiles(self):
        """
        Opens the file dialog and let's the user choose one or more files.
        """
        dialog = qt.QFileDialog(self)
        dialog.setFileMode(qt.QFileDialog.ExistingFiles)

        if not dialog.exec_():
            dialog.close()
            return

        for file in dialog.selectedFiles():
            self.addFile(file)

    def _removeFiles(self):
        """
        Removes the selected items from the table.
        """
        selectedItems = self._table.selectedItems()
        if selectedItems is not None:
            for item in selectedItems:
                self._files.remove(item.text())
                self._table.removeRow(item.row())

    def addFile(self, file):
        """
        Adds a file to the table.

        :param str file: filepath to add to the table.
        """
        if not os.path.isfile(file):
            raise FileNotFoundError(file)
        item = qt.QTableWidgetItem()
        item.setText(file)
        row = self._table.rowCount()
        self._table.setRowCount(row + 1)
        self._table.setItem(row, 0, item)
        self._files.append(file)

    def getFiles(self):
        return self._files

    def setFiles(self, files):
        """
        Adds a list of files to the table.

        :param array_like files: List to add
        """
        for file in files:
            self.addFile(file)

    def getDir(self):
        if len(self._files):
            return os.path.dirname(self._files[0])
        return None


class DataPathSelection(qt.QWidget):
    """
    Widget to select a data path from a file path
    """

    def __init__(self, parent=None, text="data path") -> None:
        super().__init__(parent)
        self.__filePath = None

        self.setLayout(qt.QHBoxLayout())
        self._label = qt.QLabel(text, self)
        self.layout().addWidget(self._label)
        self._dataPathQLE = qt.QLineEdit("", self)
        self.layout().addWidget(self._dataPathQLE)
        self._selectPB = qt.QPushButton("select", self)
        self.layout().addWidget(self._selectPB)

        # connect signal / slot
        self._selectPB.released.connect(self._selectDataPath)

    def getDataPath(self):
        return self._dataPathQLE.text()

    def setDataPath(self, dataPath: str):
        try:
            url = DataUrl(path=dataPath)
        except Exception:
            self._dataPathQLE.setText(str(dataPath))
        else:
            self._dataPathQLE.setText(url.data_path())

    def setHDF5File(self, filename: str):
        """
        set file name. Warning according to existing architecture the file name
        can either be the file name directly or a DataUrl as a str
        """
        try:
            # handle case getRawFilename return the url and not the file path only
            url = DataUrl(path=filename)
        except Exception:
            pass
        else:
            filename = url.file_path()
        self.__filePath = filename

    def _selectDataPath(self):
        """callback when want to select a data path"""
        if self.__filePath is None:
            msg = qt.QMessageBox()
            msg.setIcon(qt.QMessageBox.Critical)
            msg.setText("Please select the HDF5 file containing data first")
            msg.setStandardButtons(qt.QMessageBox.Ok)
            msg.exec_()
        else:
            from silx.gui.dialog.GroupDialog import GroupDialog

            dialog = GroupDialog(parent=self)
            dialog.addFile(self.__filePath)
            dialog.setMode(GroupDialog.LoadMode)
            if dialog.exec_():
                selectedUrl = dialog.getSelectedDataUrl()
                if selectedUrl is not None:
                    self._dataPathQLE.setText(selectedUrl.data_path())

    def getMetadataUrl(self) -> Optional[DataUrl]:
        """
        Return the path to the data url
        """
        if self.getDataPath() == "":
            return None
        else:
            return DataUrl(
                file_path=self.__filePath,
                data_path=self.getDataPath(),
                scheme="silx",
            )


class DirSelectionWidget(qt.QWidget):
    """
    Widget used to obtain a filename (manually or from a file)
    """

    dirChanged = qt.Signal()

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self._dir = qt.QLineEdit("", parent=self)
        self._dir.editingFinished.connect(self.dirChanged)
        self._addButton = qt.QPushButton("Upload directory", parent=self)
        # self._okButton =  qt.QPushButton("Ok", parent=self)
        self._addButton.pressed.connect(self._uploadDir)
        # self._okButton.pressed.connect(self.close)
        self.setLayout(qt.QHBoxLayout())

        self.layout().addWidget(self._dir)
        self.layout().addWidget(self._addButton)
        # self.layout().addWidget(self._okButton)

    def _uploadDir(self):
        """
        Loads the file from a FileDialog.
        """
        fileDialog = qt.QFileDialog()
        fileDialog.setOption(qt.QFileDialog.ShowDirsOnly)
        fileDialog.setFileMode(qt.QFileDialog.Directory)
        if fileDialog.exec_():
            self._dir.setText(fileDialog.directory().absolutePath())
            self.dirChanged.emit()
        else:
            _logger.warning("Could not open directory")

    def getDir(self):
        return str(self._dir.text())

    def setDir(self, _dir):
        self._dir.setText(str(_dir))


class FilenameSelectionWidget(qt.QWidget):
    """
    Widget used to obtain a filename (manually or from a file)
    """

    filenameChanged = qt.Signal()

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)
        self._isH5 = False
        self._filename = None
        self._filenameLE = qt.QLineEdit("", parent=self)
        self._addButton = qt.QPushButton("Upload data", parent=self)
        # self._okButton =  qt.QPushButton("Ok", parent=self)
        self._addButton.pressed.connect(self._uploadFilename)
        # self._okButton.pressed.connect(self.close)
        self.setLayout(qt.QHBoxLayout())

        self.layout().addWidget(self._filenameLE)
        self.layout().addWidget(self._addButton)
        # self.layout().addWidget(self._okButton)

    def isHDF5(self, isH5):
        self._isH5 = isH5

    def _uploadFilename(self):
        """
        Loads the file from a FileDialog.
        """
        if self._isH5:
            fileDialog = DataFileDialog()
            fileDialog.setFilterMode(DataFileDialog.FilterMode.ExistingDataset)
            if self._filename:
                fileDialog.selectUrl(self._filename)
            if fileDialog.exec_():
                self._filename = fileDialog.selectedDataUrl().path()
                self._filenameLE.setText(self._filename)
                self.filenameChanged.emit()
            else:
                _logger.warning("Could not open file")
        else:
            fileDialog = qt.QFileDialog()
            fileDialog.setFileMode(qt.QFileDialog.ExistingFile)
            if self._filename:
                fileDialog.selectFile(self._filename)
            if fileDialog.exec_():
                self._filenameLE.setText(fileDialog.selectedFiles()[0])
                self._filename = fileDialog.selectedFiles()[0]
                self.filenameChanged.emit()
            else:
                _logger.warning("Could not open file")

    def getFilename(self):
        return str(self._filenameLE.text())

    def setFilename(self, filename):
        self._filename = filename
        self._filenameLE.setText(str(filename))
