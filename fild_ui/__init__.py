import warnings

# pylint: disable=wrong-import-position
warnings.warn(
    "fild-ui is deprecated and will no longer be maintained. "
    "Migrate to surety-ui: pip install surety-ui. "
    "Replace 'from fild_ui import ...' with 'from surety.ui import ...'. "
    "See https://github.com/elenakulgavaya/surety-ui for details.",
    DeprecationWarning,
    stacklevel=2,
)

from .local_storage import LocalStorage
from .browser import Browser, Page
from .elements import (
    Checkbox, Container, Button, Label, Link, Select, Table, TableRow,
    TextInput,
)
