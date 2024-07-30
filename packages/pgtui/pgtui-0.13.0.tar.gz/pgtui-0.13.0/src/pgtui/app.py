from functools import cached_property
from pathlib import Path
from typing import Iterable

from textual import on
from textual.app import App
from textual.binding import Binding
from textual.widgets import Footer, Header, TabbedContent, TabPane, Tabs

from pgtui import __version__
from pgtui.bindings import bindings
from pgtui.entities import DbContext
from pgtui.messages import ShowException
from pgtui.utils.file import pick_file
from pgtui.widgets.dialog import ConfirmationDialog, ErrorDialog, HelpDialog
from pgtui.widgets.pane import EditorPane
from pgtui.widgets.text_area import SqlTextArea


class PgTuiApp(App[None]):
    TITLE = "pgtui"
    SUB_TITLE = __version__
    CSS_PATH = "app.css"

    BINDINGS = [
        Binding(bindings.show_help, "help", "Help"),
        Binding(bindings.new_tab, "add_pane", "Add pane"),
        Binding(bindings.open_file, "open_file", "Open file"),
        Binding(bindings.exit, "exit", "Exit pgtui"),
        Binding(bindings.show_tab_1, "switch_tab(0)", show=False),
        Binding(bindings.show_tab_2, "switch_tab(1)", show=False),
        Binding(bindings.show_tab_3, "switch_tab(2)", show=False),
        Binding(bindings.show_tab_4, "switch_tab(3)", show=False),
        Binding(bindings.show_tab_5, "switch_tab(4)", show=False),
        Binding(bindings.show_tab_6, "switch_tab(5)", show=False),
        Binding(bindings.show_tab_7, "switch_tab(6)", show=False),
        Binding(bindings.show_tab_8, "switch_tab(7)", show=False),
        Binding(bindings.show_tab_9, "switch_tab(8)", show=False),
        Binding(bindings.show_tab_10, "switch_tab(9)", show=False),
        Binding(bindings.next_tab, "next_tab", show=False),
        Binding(bindings.prev_tab, "prev_tab", show=False),
    ]

    def __init__(self, ctx: DbContext, file_path: Path | None):
        super().__init__()
        self.ctx = ctx
        self.file_path = file_path
        self.animation_level = "none"

    def compose(self):
        yield Header()
        yield TabbedContent(id="editor_tabs")
        yield Footer()

    async def on_mount(self):
        await self.add_pane(self.file_path)

    def on_show_exception(self, message: ShowException):
        self.push_screen(ErrorDialog("Error", str(message.exception)))

    @on(EditorPane.Close)
    def on_pane_close(self, event: EditorPane.Close):
        if event.tab_pane.id is not None:
            self.tc.remove_pane(event.tab_pane.id)

    @on(EditorPane.Dirty)
    def on_pane_dirty(self, event: EditorPane.Dirty):
        label = event.file_path.name if event.file_path else "untitled"
        self.tc.get_tab(event.tab_pane).label = f"{label}*"

    @on(EditorPane.Saved)
    def on_pane_saved(self, event: EditorPane.Saved):
        self.tc.get_tab(event.tab_pane).label = event.file_path.name

    async def add_pane(self, file_path: Path | None = None):
        pane = EditorPane(self.ctx, file_path)
        await self.tc.add_pane(pane)
        self.activate_pane(pane)

    def activate_pane(self, pane: TabPane):
        assert pane.id is not None
        self.tc.active = pane.id

    @on(TabbedContent.TabActivated)
    def _on_tab_activated(self, event: TabbedContent.TabActivated):
        event.pane.query_one(SqlTextArea).focus()

    def action_help(self):
        self.app.push_screen(HelpDialog())

    async def action_add_pane(self):
        await self.add_pane()

    async def action_open_file(self):
        with self.suspend():
            path = await pick_file()
            if path:
                await self.add_pane(path)

    def action_switch_tab(self, no: int):
        panes = self.panes()
        if no < len(panes):
            self.activate_pane(panes[no])

    def action_next_tab(self):
        self.query_one(Tabs).action_next_tab()

    def action_prev_tab(self):
        self.query_one(Tabs).action_previous_tab()

    def action_exit(self):
        def on_dismiss(result: bool):
            if result:
                self.app.exit()

        screen = ConfirmationDialog(
            "Quit?",
            confirm_label="Quit",
            cancel_label="Cancel",
        )

        self.app.push_screen(screen, on_dismiss)

    @cached_property
    def tc(self):
        return self.query_one("#editor_tabs", TabbedContent)

    def panes(self):
        return self.tc.query(TabPane)

    def _active_index(self, panes: Iterable[TabPane]) -> int | None:
        if self.tc.active:
            for index, pane in enumerate(panes):
                if pane.id == self.tc.active:
                    return index
