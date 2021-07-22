from movie import Movie, get_movies
from PySide2 import QtCore, QtWidgets



class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setWindowTitle("Ciné Club")
        self.populate_movies()
        self.setup_connections()
        self.add_movie()
        self.setup_css()
        

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.box_text = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton("Ajouter un film")
        self.box_list = QtWidgets.QListWidget()
        self.box_list.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_delete = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.main_layout.addWidget(self.box_text)
        self.main_layout.addWidget(self.btn_add)
        self.main_layout.addWidget(self.box_list)
        self.main_layout.addWidget(self.btn_delete)
        
    def populate_movies(self):
        liste_movies = get_movies()
        
        for movie in liste_movies:
        #     self.box_list.addItem(movie.title)
            box_list_item = QtWidgets.QListWidgetItem(movie.title)
            box_list_item.setData(QtCore.Qt.UserRole, movie)
            self.box_list.addItem(box_list_item)


    def add_movie(self):
        new_movie = self.box_text.text()
        if not new_movie:
            return False

        m = Movie(title=new_movie)
        resultat = m.add_to_movies()
        if resultat:
            box_list_item = QtWidgets.QListWidgetItem(m.title)
            box_list_item.setData(QtCore.Qt.UserRole, m)
            self.box_list.addItem(box_list_item)
        
        self.box_text.setText("")

    def remove_movie(self):
        for selected_item in self.box_list.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.box_list.takeItem(self.box_list.row(selected_item))


    def setup_connections(self):
        self.box_text.returnPressed.connect(self.add_movie)
        self.btn_delete.clicked.connect(self.remove_movie)
        self.btn_add.clicked.connect(self.add_movie)
      

    def setup_css(self):
        self.setStyleSheet("""
        background-color: grey;
        color: white;
        border: none;
        """)
    

    

appli = QtWidgets.QApplication([])
win = App()
win.show()

appli.exec_()