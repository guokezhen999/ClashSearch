from ShowForms import *
from UI.ShowFiguresForm import Ui_ShowFiguresForm

class ShowFiguresForm(Ui_ShowFiguresForm, QDialog):
    def __init__(self, filePaths: list[str]):
        super().__init__()
        self.files = filePaths
        self.setupUi(self)
        self.showForm()

    def showForm(self):
        gridLayout = QGridLayout()
        figureSize = QSize(800, 350)
        scale = 0.625
        for i, file in enumerate(self.files):
            verticalLayout = QVBoxLayout()
            verticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
            info = (file.split('/')[-1]).split('_')[0]
            label = QLabel(info)
            label.setMaximumSize(QSize(10000, 40))
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            graphicsView = QGraphicsView()
            graphicsView.setMinimumSize(figureSize)
            graphicsView.setMaximumSize(figureSize)
            item = QGraphicsPixmapItem(QPixmap(file))
            item.setScale(scale)
            scene = QGraphicsScene()
            scene.addItem(item)
            graphicsView.setScene(scene)
            verticalLayout.addWidget(label)
            verticalLayout.addWidget(graphicsView)
            gridLayout.addLayout(verticalLayout, i, 0, 1, 1)
        self.scrollAreaWidgetContents.setLayout(gridLayout)


