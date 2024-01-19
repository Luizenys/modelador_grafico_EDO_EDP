from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from mycanvas import *
from mymodel import *
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # define tamanho da janela
        self.setGeometry(100,100,600,400)
        # define titulo da janela
        self.setWindowTitle("Luiza Drawer")
        # cria um objeto canvas que é um widget
        self.canvas = MyCanvas()
        # seta esse canvas para ser o widget central da janela
        self.setCentralWidget(self.canvas)
        # cria um objeto modelo e passa para o canvas
        self.model = MyModel()
        self.canvas.setModel(self.model)
        # cria a barra de ferramentas
        tb = self.addToolBar("File")
        # cria os botoes de fit e grade
        fit = QAction(QIcon("icons/fit.png"),"fit",self)
        grade = QAction(QIcon("icons/grade.png"),"grade",self)
        tb.addAction(fit)
        tb.addAction(grade)
        tb.actionTriggered[QAction].connect(self.tbpressed)

    def tbpressed(self,a):
        # checa se o botão pressionado foi o fit
        if a.text() == "fit":
            self.canvas.fitWorldToViewport()

        # checa se o botão pressionado foi o grade
        if a.text() == "grade":
            # abre um diálogo para inserir a informação do espaço entre os pontos
            espaco, valid = QInputDialog.getInt(self, 'Grade de Pontos', 'Digite o espaço entre os pontos da grade:')
            if valid:
                self.canvas.pointGrid(int(espaco))