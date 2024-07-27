import click
from zhinst.comms import init_logs, LogSeverity
from zhinst.comms.compiler import compile, capnp_id


@click.group()
def main():
    pass


@main.command(
    name="compile",
    help="Compiles Cap'n Proto schema files and generates corresponding _schema.py files.",
)
@click.argument(
    "source",
    required=True,
)
@click.option(
    "--src-prefix",
    required=True,
    help="If a file specified for compilation starts with <prefix>, remove the prefix for the purpose of deciding the names of output files.",
)
@click.option(
    "--output-folder",
    "-o",
    required=True,
    help="The folder in which the _schema.py file will be written.",
)
@click.option(
    "--import-path",
    "-I",
    multiple=True,
    help="Directories to add for the search of imports.",
)
def compile_cli(source, src_prefix, output_folder, import_path):
    init_logs(LogSeverity.STATUS)
    compile(
        src=[source],
        src_prefix=src_prefix,
        output_folder=output_folder,
        import_paths=import_path,
    )


@main.command(
    name="id",
    help="Generates a new 64-bit unique ID for use in a Cap'n Proto schema.",
)
def id_cli():
    id = capnp_id()
    print(id)


if __name__ == "__main__":
    main()
