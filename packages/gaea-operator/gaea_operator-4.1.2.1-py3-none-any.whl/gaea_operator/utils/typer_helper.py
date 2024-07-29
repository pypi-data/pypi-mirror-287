"""
Usage:
A dataclass/YAML/CLI config system:
- write a @dataclass with your config options
- make sure every option has a default value
- include a `config: str = ""` option in the dataclass.
- write a main function that takes a single argument of the dataclass type
- decorate your main function with @dataclass_cli
- make sure your main function has a docstring.
The config will be loaded from a YAML file specified by the --config option,
and CLI options will override the config file.
Example from running this file:
> python edit/config.py --help
                                                                                                                                                           
 Usage: config.py [OPTIONS]                                                                                                                                
                                                                                                                                                           
 test                                                                                                                                                      
                                                                                                                                                           
╭─ Options 
│ --config        TEXT
│ --hi            INTEGER  [default: 1]
│ --bye           TEXT     [default: bye]
│ --help                   Show this message and exit.
╰─
"""
import dataclasses, inspect, typing as tp
import typer


def conf_callback(ctx: typer.Context, param: typer.CallbackParam, value: str) -> str:
    """
    Callback for typer.Option that loads a config file from the first
    argument of a dataclass.
    Based on https://github.com/tiangolo/typer/issues/86#issuecomment-996374166
    """
    if param.name == "config" and value:
        typer.echo(f"Loading config file: {value}")
        import yaml
        try:
            with open(value, "r") as f:
                conf = yaml.safe_load(f)
            ctx.default_map = ctx.default_map or {}
            ctx.default_map.update(conf)
        except Exception as ex:
            raise typer.BadParameter(str(ex))
    return value


def dataclass_cli(func):
    """
    Converts a function taking a dataclass as its first argument into a
    dataclass that can be called via `typer` as a CLI.
    Additionally, the --config option will load a yaml configuration before the
    other arguments.
    Modified from:
    - https://github.com/tiangolo/typer/issues/197
    A couple related issues:
    - https://github.com/tiangolo/typer/issues/153
    - https://github.com/tiangolo/typer/issues/154
    """

    # The dataclass type is the first argument of the function.
    sig = inspect.signature(func)
    type_hints = tp.get_type_hints(func)
    param = list(sig.parameters.values())[0]
    cls = param.annotation
    if isinstance(cls, str): cls = type_hints[param.name]
    assert dataclasses.is_dataclass(cls)

    def wrapped(**kwargs):
        # Load the config file if specified.
        if kwargs.pop("config", "") != "":
            import yaml
            with open(kwargs["config"], "r") as f:
                conf = yaml.safe_load(f)
        else:
            conf = {}

        # CLI options override the config file.
        conf.update(kwargs)

        # Convert back to the original dataclass type.
        arg = cls(**conf)

        # Actually call the entry point function.
        return func(arg)

    # To construct the signature, we remove the first argument (self)
    # from the dataclass __init__ signature.
    signature = inspect.signature(cls.__init__)
    parameters = list(signature.parameters.values())
    if len(parameters) > 0 and parameters[0].name == "self":
        del parameters[0]

    # Add the --config option to the signature.
    # When called through the CLI, we need to set defaults via the YAML file.
    # Otherwise, every field will get overwritten when the YAML is loaded.
    parameters = [
        inspect.Parameter(
            "config",
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            default=typer.Option("", callback=conf_callback, is_eager=True),
        )
    ] + [p for p in parameters if p.name != "config"]

    # The new signature is compatible with the **kwargs argument.
    wrapped.__signature__ = signature.replace(parameters=parameters)

    # The docstring is used for the explainer text in the CLI.
    wrapped.__doc__ = (func.__doc__ or '') + "\n" + ""

    return wrapped
