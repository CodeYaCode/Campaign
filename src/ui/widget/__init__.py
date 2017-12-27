# __init__.py

import sys

sys.path.append('..')

from src.ui.widget.ControlWidget   import ControlWidget
from src.ui.widget.HeaderWidget    import HeaderWidget
from src.ui.widget.ContainerWidget import ContainerWidget
from src.ui.widget.FooterWidget    import FooterWidget
from src.ui.widget.DetailDialog import DetailDialog

ControlWidget   = ControlWidget
HeaderWidget    = HeaderWidget
FooterWidget    = FooterWidget
ContainerWidget = ContainerWidget
DetailDialog    = DetailDialog