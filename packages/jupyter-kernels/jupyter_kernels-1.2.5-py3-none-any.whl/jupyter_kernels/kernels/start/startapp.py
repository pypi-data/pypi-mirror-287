# Copyright (c) 2023-2024 Datalayer, Inc.
#
# Datalayer License

from datalayer.application import NoStart

from ...application_base import JupyterKernelsBaseApp


class KernelStartApp(JupyterKernelsBaseApp):
    """Kernel Start application."""

    description = """
      An application to start a Kernel.
    """

    def start(self):
        try:
            super().start()
            self.log.info(f"Kernel Start - not implemented.")
        except NoStart:
            pass
        self.exit(0)
