from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Button, SelectionList
from textual.widgets.selection_list import Selection

from slurm_viewer.widgets.column_selector import ColumnSelection


class SelectColumnsScreen(ModalScreen):
    DEFAULT_CSS = """
    SelectColumnsScreen {
        align: center middle;
        width: auto;
        height: auto;
    }
    
    SelectColumnsScreen SelectionOrderList {
        align: center middle;
        height: auto;
        width: 100%;
    }
    
    SelectColumnsScreen Vertical {
        height: auto;
        width: 45;
    }
    
    SelectColumnsScreen Horizontal {
        width: auto;
        height: auto;
    }
    
    SelectColumnsScreen Button {
        width: 23;
    }
    """

    def __init__(self, selected_columns: list[str], remaining_columns: list[str]) -> None:
        super().__init__()
        self.selected_columns = selected_columns
        self.remaining_columns = remaining_columns

    def compose(self) -> ComposeResult:
        with Vertical():
            selections = [Selection(x, x, True) for x in self.selected_columns]
            selections.extend([Selection(x, x, False) for x in self.remaining_columns])

            yield SelectionList[str](*selections)
            with Horizontal():
                yield Button('Ok', variant='success', id='ok')
                yield Button('Cancel', variant='warning', id='cancel')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'ok':
            self.dismiss(self.result())
        else:
            self.dismiss(None)

    def result(self) -> list[str]:
        data: list[str] = self.query_one(SelectionList).selected
        return data


class SelectPartitionScreen(ModalScreen):
    DEFAULT_CSS = """
    SelectPartitionScreen {
        align: center middle;
        width: auto;
        height: auto;
    }
    
    SelectPartitionScreen Vertical {
        height: auto;
        width: auto;
    }
    
    SelectPartitionScreen Horizontal {
        width: auto;
        height: auto;
    }
    
    SelectPartitionScreen Horizontal Button {
        margin: 2;
        width: 10;
    }
    """

    def __init__(self, partitions: list[str], selected_partitions: list[str]) -> None:
        super().__init__()
        self.partitions = partitions
        self.selected_partitions = selected_partitions

    def compose(self) -> ComposeResult:
        with Vertical():
            yield ColumnSelection(self.partitions, self.selected_partitions, id='partitions')
            with Horizontal():
                yield Button('Ok', variant='success', id='ok')
                yield Button('Cancel', variant='warning', id='cancel')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'ok':
            self.dismiss(self.result())
        else:
            self.dismiss(None)

    def result(self) -> list[str]:
        data: list[str] = self.query_one(ColumnSelection).selected_columns()
        return data
