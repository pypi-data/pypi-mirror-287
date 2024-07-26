import os
import pprint

import click
from click.core import Context as ClickContext
from gable.cli.options import global_options
from loguru import logger


@click.group(hidden=True)
def debug():
    """Debug commands for the cli"""


@debug.command(
    # Disable help, we re-add it in global_options()
    add_help_option=False,
)
@global_options(add_endpoint_options=False)
@click.argument(
    "path", type=click.Path(exists=True, file_okay=False), default=os.getcwd()
)
def git_info(path: os.PathLike):
    """Prints the git information for the given directory"""
    from gable.cli.helpers.repo_interactions import get_git_repo_info

    pprint.pprint(get_git_repo_info(path))


@debug.command(
    # Disable help, we re-add it in global_options()
    add_help_option=False,
)
@global_options(add_endpoint_options=False)
@click.pass_context
def env(_ctx: ClickContext):
    """Prints the environment variables used to configure Gable"""
    env_vars = ["GABLE_API_ENDPOINT", "GABLE_API_KEY"]
    for env_var in env_vars:
        logger.info(f"  {env_var}={os.environ.get(env_var, '<Not Set>')}")
    logger.info(
        "Note: these can be overridden by passing command line arguments to gable."
    )


@debug.command()
@global_options()
@click.pass_context
def pyping(ctx: ClickContext):
    """Pings the Gable API (python server) to check for connectivity"""
    try:
        response, success, status_code = ctx.obj.client.get_pyping()
    except Exception as e:
        raise click.ClickException(
            f"Unable to ping Gable API at {ctx.obj.client.endpoint}: {str(e)}"
        )
    if not success:
        raise click.ClickException(
            f"Unable to ping Gable API at {ctx.obj.client.endpoint}"
        )
    logger.info(f"Successfully pinged Gable API at {ctx.obj.client.endpoint}")
