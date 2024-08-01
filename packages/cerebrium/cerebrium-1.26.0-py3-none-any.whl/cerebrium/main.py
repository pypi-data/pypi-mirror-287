import os

import bugsnag

from cerebrium import __version__ as cerebrium_version
from cerebrium.commands.app import app
from cerebrium.commands.auth import login, save_auth_config
from cerebrium.commands.cortex import deploy, init
from cerebrium.commands.project import project_app
from cerebrium.core import cli
from cerebrium.utils.bugsnag_setup import init_bugsnag

bugsnag.configure(
    api_key="606044c1e243e11958763fb42cb751c4",
    project_root=os.path.dirname(os.path.abspath(__file__)),
    release_stage=os.getenv("ENV", "prod"),
    app_version=cerebrium_version,
    auto_capture_sessions=True,
)

init_bugsnag()

cli.add_typer(
    app,
    name="app",
    help="Manage your apps. See a list of your apps, their details and scale them",
)
cli.add_typer(project_app, name="project", help="Manage all functionality around your projects")


@cli.command()
def version():
    """
    Print the version of the Cerebrium CLI
    """
    print(cerebrium_version)


# Add commands directly to the CLI
cli.command()(login)
cli.command()(save_auth_config)
cli.command()(init)
cli.command()(deploy)

if __name__ == "__main__":
    cli()
