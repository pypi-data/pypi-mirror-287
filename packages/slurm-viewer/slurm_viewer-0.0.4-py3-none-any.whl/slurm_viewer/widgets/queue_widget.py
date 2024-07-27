from __future__ import annotations

import csv
import datetime
from io import StringIO
from typing import Any

from textual import work, on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.css.query import NoMatches
from textual.reactive import reactive
from textual.widgets import Static, Label, Button, Checkbox

from slurm_viewer.data.config import Config
from slurm_viewer.data.models import Queue, JobStateCodes, Slurm, SlurmError
from slurm_viewer.widgets.loading import Loading
from slurm_viewer.widgets.screens import SelectColumnsScreen
from slurm_viewer.widgets.sortable_data_table import SortableDataTable


class QueueWidget(Static):
    CSS_PATH = 'slurm_viewer.tcss'

    BINDINGS = [
        Binding('c', 'columns', 'Select Columns'),
        Binding('shift+left', 'move_left', 'Column Left'),
        Binding('shift+right', 'move_right', 'Column Right')
    ]

    config: reactive[Config] = reactive(Config, layout=True, always_update=True)

    def __init__(self, _slurm: Slurm, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.slurm = _slurm
        self.queue_info: list[Queue] = []
        self.partitions: list[str] = []

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal(id='queue_horizontal'):
                yield Label(id='queue_label')
                yield Button(label='Refresh', id='queue_refresh')
            with ScrollableContainer(id='queue_scrollable_container'):
                yield SortableDataTable(id='queue_running_table')
                yield SortableDataTable(id='queue_pending_table')

    @work(name='queue_widget_watch_config')
    async def watch_config(self, _: Config, __: Config) -> None:
        try:
            self.query_one('#queue_scrollable_container', ScrollableContainer)
        except NoMatches:
            return

        with Loading(self):
            try:
                self.queue_info = await self.slurm.queue()
                self.query_one('#queue_label', Label).update(f'Last update: {datetime.datetime.now().strftime("%H:%M:%S")}')
                await self._update_table()
            except SlurmError as e:
                self.app.notify(title='Error retrieving data from cluster', message=str(e), severity='error')

    async def on_mount(self) -> None:
        try:
            self.queue_info = await self.slurm.queue()
            self.partitions = await self.slurm.partitions()
            await self._update_table()
        except SlurmError as e:
            self.app.notify(title='Error retrieving data from cluster', message=str(e), severity='error')

    def copy_to_clipboard(self) -> None:
        with StringIO() as fp:
            fieldnames = list(self.queue_info[0].model_dump().keys())
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writeheader()
            for node in self.queue_info:
                writer.writerow(node.model_dump())

            self.app.copy_to_clipboard(fp.getvalue())
            self.app.notify('Copied queues to clipboard')

    async def _update_table(self) -> None:
        if not self.is_mounted:
            return

        table = self.query_one('#queue_running_table', SortableDataTable)

        jobs = [x for x in self.queue_info if x.state == JobStateCodes.RUNNING]
        table.border_title = f'Running Jobs ({len(jobs)})'
        self._queue_data_table(jobs, table)

        table = self.query_one('#queue_pending_table', SortableDataTable)

        jobs = [x for x in self.queue_info if x.state == JobStateCodes.PENDING]
        table.border_title = f'Pending Jobs ({len(jobs)})'
        self._queue_data_table(jobs, table)

        self.query_one('#queue_label', Label).update(f'Last update: {datetime.datetime.now().strftime("%H:%M:%S")}')

    def _queue_data_table(self, queue: list[Queue], data_table: SortableDataTable) -> None:
        data_table.cursor_type = 'row'
        data_table.clear(columns=True)
        data_table.zebra_stripes = True
        data_table.add_columns(*self.config.ui.queue_columns)

        for row in queue:
            data = [getattr(row, key) for key in self.config.ui.queue_columns]
            data_table.add_row(*data)

    @work(name='queue_widget_refresh_info')
    @on(Button.Pressed, '#queue_refresh')
    async def refresh_info(self, _: Checkbox.Changed) -> None:
        await self._update_table()

    async def action_columns(self) -> None:
        async def check_result(selected: list[str] | None) -> None:
            if selected is None:
                return

            self.config.ui.queue_columns = selected
            await self._update_table()

        current_columns = [x.label.plain for x in self.query_one('#queue_running_table', SortableDataTable).columns.values()]
        all_columns = list(Queue.model_fields.keys())
        all_columns.extend([name for name, value in vars(Queue).items() if isinstance(value, property)])
        remaining_columns = sorted(set(all_columns) - set(current_columns))

        await self.app.push_screen(SelectColumnsScreen(current_columns, remaining_columns), check_result)

    async def action_move_left(self) -> None:
        table = self.query_one('#queue_running_table', SortableDataTable)
        if table.cursor_column == 0:
            return

        self.config.ui.queue_columns.insert(table.cursor_column - 1, self.config.ui.queue_columns.pop(table.cursor_column))
        old_pos = table.cursor_coordinate

        await self._update_table()

        table.cursor_coordinate = old_pos.left()

    async def action_move_right(self) -> None:
        tables = self.query(SortableDataTable)
        focus_table = None
        for table in tables:
            if table.has_focus:
                focus_table = table
                break

        if focus_table is None:
            return

        self.config.ui.queue_columns.insert(focus_table.cursor_column + 1,
                                            self.config.ui.queue_columns.pop(focus_table.cursor_column))
        old_pos = focus_table.cursor_coordinate

        await self._update_table()

        for table in tables:
            table.cursor_coordinate = old_pos.right()
