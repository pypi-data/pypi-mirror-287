from __future__ import annotations

from typing import Protocol, cast, Final, Generator

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Footer, Header, TabbedContent, TabPane

from slurm_viewer.data.config import Config, Cluster
from slurm_viewer.data.models import Slurm
from slurm_viewer.data.slurm_local import SlurmLocal
from slurm_viewer.data.slurm_ssh import SlurmSsh
from slurm_viewer.widgets.nodes_widget import NodesWidget
from slurm_viewer.widgets.plot_widget import PlotWidget
# from slurm_viewer.widgets.priority_widget import PriorityWidget
from slurm_viewer.widgets.queue_widget import QueueWidget
from slurm_viewer.widgets.screens import SelectPartitionScreen

USE_PRIORITY_WIDGET: Final[bool] = False


class SlurmTabBase(Protocol):
    def copy_to_clipboard(self) -> None:
        ...


class SlurmViewer(App):
    CSS_PATH = 'widgets/slurm_viewer.tcss'

    BINDINGS = [
        Binding('f2', 'copy_to_clipboard', 'Copy to clipboard'),
        Binding('f5', 'reload_config', 'Reload config'),
        Binding('p', 'partitions', 'Select Partitions'),
        Binding('q', 'quit', 'Quit', show=False),
        Binding('f12', 'screenshot', 'Screenshot', show=False),
    ]

    config: reactive[Config] = reactive(Config.init, layout=True, always_update=True)

    def __init__(self) -> None:
        super().__init__()
        self.title = f'{self.__class__.__name__}'  # type: ignore
        if len(self.config.clusters) == 0:
            self.app.notify(title='No clusters defined',
                            message='The settings file does not contain any cluster definitions.', severity='error')

    @staticmethod
    def _create_slurm(_cluster: Cluster) -> Slurm:
        if _cluster.server is None:
            return SlurmLocal(_cluster)  # type: ignore

        return SlurmSsh(_cluster)  # type: ignore

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Vertical():
            with TabbedContent(id='cluster_tab'):
                for cluster in self.config.clusters:
                    with TabPane(cluster.name):
                        yield from self.compose_tab(self._create_slurm(cluster))
        yield Footer()

    @staticmethod
    def compose_tab(_slurm: Slurm) -> Generator[Widget, None, None]:
        with TabbedContent():
            with TabPane('Nodes'):
                yield NodesWidget(_slurm).data_bind(SlurmViewer.config)
            with TabPane('Queue'):
                yield QueueWidget(_slurm).data_bind(SlurmViewer.config)
            # if USE_PRIORITY_WIDGET:
            #     with TabPane('Priority'):
            #         yield PriorityWidget().data_bind(SlurmViewer.config)
            with TabPane('GPU usage'):
                yield PlotWidget(_slurm).data_bind(SlurmViewer.config)

    def action_reload_config(self) -> None:
        self.notify('Reloading configuration')
        self.config = Config.init()  # type: ignore

    def action_copy_to_clipboard(self) -> None:
        active_cluster_tab = self.query_one('#cluster_tab', TabbedContent).active_pane
        assert active_cluster_tab
        pane = active_cluster_tab.query_one(TabbedContent).active_pane
        assert pane

        children = pane.children
        assert len(children) == 1

        cast(SlurmTabBase, children[0]).copy_to_clipboard()

    async def action_partitions(self) -> None:
        def _update_partitions(selected: list[str] | None) -> None:
            if selected is None:
                return

            if active_cluster.partitions == selected:
                # selection has not changed, don't update the config to stop updating the widgets.
                return

            for cluster in self.config.clusters:
                if cluster.name == active_cluster.name:
                    cluster.partitions = selected
                    break

            self.mutate_reactive(SlurmViewer.config)

        active_pane = self.query_one('#cluster_tab', TabbedContent).active_pane
        assert active_pane
        nodes = active_pane.query_one(NodesWidget)
        assert nodes

        active_cluster = nodes.slurm.cluster()
        all_partitions = await nodes.slurm.partitions()
        screen = SelectPartitionScreen(all_partitions, active_cluster.partitions)
        await self.push_screen(screen, _update_partitions)


if __name__ == "__main__":
    app = SlurmViewer()
    app.run()
