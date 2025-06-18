from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Button, Select, DataTable, Label
from textual import events

class RunningProgramView(Vertical):
    def __init__(self, ur):
        super().__init__()
        self.ur = ur

        self.warning_label = Label("SFTP et Dashboard doivent être activés pour lister les programmes")
        self.warning_label.visible = False  # caché par défaut

        self.program_select = Select(options=[])

        self.btn_run = Button("Run", id="btn_run")
        self.btn_pause = Button("Pause", id="btn_pause")
        self.btn_stop = Button("Stop", id="btn_stop")

        self.variables_table = DataTable(zebra_stripes=True)
        self.variables_table.add_columns("Name", "Type", "Value")

        self.threads_table = DataTable(zebra_stripes=True)
        self.threads_table.add_columns("Line Number", "Line Name")

    def compose(self):
        yield Static("Running program and variables", classes="view-title")
        yield self.warning_label
        with Horizontal():
            yield self.program_select
            yield self.btn_run
            yield self.btn_pause
            yield self.btn_stop
        yield Static("Global Variables")
        yield self.variables_table
        yield Static("Program Threads")
        yield self.threads_table

    async def on_mount(self):
        self.update_controls_enabled()
        await self.load_programs()

    def update_controls_enabled(self):
        sftp_connected = False
        if hasattr(self.ur.sftp, 'connected'):
            sftp_connected = self.ur.sftp.connected
        elif callable(getattr(self.ur.sftp, 'is_connected', None)):
            sftp_connected = self.ur.sftp.is_connected()

        dashboard_initialized = getattr(self.ur.dashboard, 'initialized', False)

        enabled = sftp_connected and dashboard_initialized

        self.btn_run.disabled = not enabled
        self.btn_pause.disabled = not enabled
        self.btn_stop.disabled = not enabled
        self.program_select.disabled = not enabled
        self.warning_label.visible = not enabled

    async def load_programs(self):
        sftp_connected = False
        if hasattr(self.ur.sftp, 'connected'):
            sftp_connected = self.ur.sftp.connected
        elif callable(getattr(self.ur.sftp, 'is_connected', None)):
            sftp_connected = self.ur.sftp.is_connected()

        dashboard_initialized = getattr(self.ur.dashboard, 'initialized', False)

        if sftp_connected and dashboard_initialized:
            try:
                programs = self.ur.sftp.enumerate_programs()
                self.program_select.options = [(p, p) for p in programs]
                self.warning_label.update("")
            except Exception as e:
                self.warning_label.update(f"Erreur chargement programmes : {e}")
        else:
            self.warning_label.update("Activer SFTP et Dashboard pour lister les programmes")

    def periodic_update(self):
        self.update_controls_enabled()

        variables = []
        if self.ur.primary_interface and self.ur.primary_interface.global_variables:
            variables = self.ur.primary_interface.global_variables.get_all()

        self.update_table(self.variables_table, variables, lambda v: (v.name, str(v.type), str(v)))

        threads = None
        if self.ur.primary_interface and self.ur.primary_interface.program_threads:
            threads = self.ur.primary_interface.program_threads.threads

        if threads:
            self.update_table(self.threads_table, threads, lambda t: (str(t.line_number), t.line_name))

    def update_table(self, table, items, map_fn):
        table.clear()
        if not items:
            return
        for item in items:
            table.add_row(*map_fn(item))

    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "btn_run":
            program_name = self.program_select.value
            if not program_name:
                return
            result = self.ur.dashboard.load_program(program_name)
            if not result.succeed:
                raise Exception(result.message)
            result = self.ur.dashboard.play()
            if not result.succeed:
                raise Exception(result.message)

        elif event.button.id == "btn_pause":
            self.ur.dashboard.pause()

        elif event.button.id == "btn_stop":
            self.ur.dashboard.stop()
