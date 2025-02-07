from PyQt6.QtWidgets import QVBoxLayout, QToolButton, QHBoxLayout, QCheckBox, QSpacerItem, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt, QSize

class CreateUI:
    @staticmethod
    def createToolButtonsVbox(cols: int, all: int) -> tuple[list[QToolButton], list[QHBoxLayout], QVBoxLayout]:
        rows = all // cols + 1
        vboxLayout = QVBoxLayout()
        hboxLayouts = [QHBoxLayout() for i in range(rows)]
        toolButtons = [QToolButton() for i in range(all)]
        for i in range(rows - 1):
            for j in range(cols):
                toolButtons[i * cols + j].setMinimumSize(0, 30)
                hboxLayouts[i].addWidget(toolButtons[i * cols + j])
            hboxLayouts[i].setAlignment(Qt.AlignmentFlag.AlignLeft)
            vboxLayout.addLayout(hboxLayouts[i])
        for button in toolButtons[(rows - 1) * cols:]:
            hboxLayouts[rows - 1].addWidget(button)
            hboxLayouts[rows - 1].setAlignment(Qt.AlignmentFlag.AlignLeft)
        vboxLayout.addLayout(hboxLayouts[rows - 1])
        vboxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        return toolButtons, hboxLayouts, vboxLayout

    @staticmethod
    def createCheckboxesVbox(cols: int, all: int) -> tuple[list[QCheckBox], list[QHBoxLayout], QVBoxLayout]:
        rows = all // cols + 1
        vboxLayout = QVBoxLayout()
        hboxLayouts = [QHBoxLayout() for i in range(rows)]
        checkboxes = [QCheckBox() for i in range(all)]
        for i in range(rows - 1):
            for j in range(cols):
                checkboxes[i * cols + j].setMinimumSize(0, 30)
                hboxLayouts[i].addWidget(checkboxes[i * cols + j])
            hboxLayouts[i].setAlignment(Qt.AlignmentFlag.AlignLeft)
            vboxLayout.addLayout(hboxLayouts[i])
        for button in checkboxes[(rows - 1) * cols:]:
            hboxLayouts[rows - 1].addWidget(button)
            hboxLayouts[rows - 1].setAlignment(Qt.AlignmentFlag.AlignLeft)
        vboxLayout.addLayout(hboxLayouts[rows - 1])
        vboxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        return checkboxes, hboxLayouts, vboxLayout

    @staticmethod
    def createSelectButton() -> tuple[QHBoxLayout, QPushButton, QPushButton]:
        horizontalLayoutButtons = QHBoxLayout()
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        pushButton1 = QPushButton()
        pushButton1.setText("全选")
        pushButton1.setMinimumSize(QSize(120, 0))
        pushButton1.setDefault(False)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        pushButton2 = QPushButton()
        pushButton2.setText("反选")
        pushButton2.setMinimumSize(QSize(120, 0))
        pushButton2.setDefault(False)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        horizontalLayoutButtons.addSpacerItem(spacerItem1)
        horizontalLayoutButtons.addWidget(pushButton1)
        horizontalLayoutButtons.addSpacerItem(spacerItem2)
        horizontalLayoutButtons.addWidget(pushButton2)
        horizontalLayoutButtons.addSpacerItem(spacerItem3)
        return horizontalLayoutButtons, pushButton1, pushButton2

