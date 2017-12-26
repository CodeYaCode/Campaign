# __init__.py

import sys

sys.path.append('..')

from src.ui.widget.ControlWidget   import ControlWidget
from src.ui.widget.HeaderWidget    import HeaderWidget
from src.ui.widget.ContainerWidget import ContainerWidget
from src.ui.widget.FooterLayout    import FooterLayout

ControlWidget   = ControlWidget
HeaderWidget    = HeaderWidget
FooterLayout    = FooterLayout
ContainerWidget = ContainerWidget