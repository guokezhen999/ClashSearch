import asyncio
import sys
from ClashSearch import ClashSearch
from PyQt6.QtWidgets import QApplication
from qasync import QEventLoop

if __name__ == '__main__':
    app = QApplication([])
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    clashSearch = ClashSearch()
    with loop:
        loop.run_forever()

    sys.exit(app.exec())