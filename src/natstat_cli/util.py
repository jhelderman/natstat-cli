import datetime
from functools import wraps
from types import NoneType, UnionType
from typing import Union, get_args, get_origin

import click


def model_options(model):
    "Add Pydantic model to a click CLI"
    fields = model.model_fields

    def decorator(fn):
        def new_fn(**kwargs):
            req = model(**kwargs)
            for k in fields.keys():
                if k in kwargs:
                    kwargs.pop(k)
            return fn(req=req, **kwargs)

        for name, field in fields.items():
            click_type, multiple = get_type(field.annotation)
            click_str = name.replace("_", "-")
            if click_type is bool:
                opt_str = f"--{click_str}/--no-{click_str}"
            else:
                opt_str = f"--{click_str}"
            opt = click.option(
                opt_str,
                type=click_type,
                multiple=multiple,
                default=field.default,
                required=field.is_required(),
                help=field.description,
            )
            new_fn = opt(new_fn)
        new_fn = wraps(fn)(new_fn)
        return new_fn

    return decorator


def get_opt(name, field):
    opt_str = f"--{name.replace('_', '-')}"
    return click.option(
        opt_str,
        type=field.annotation,
        default=field.default,
        help=field.description,
    )


def get_type(annotation):
    if annotation is datetime.datetime:
        return click.DateTime(["%Y-%m-%d"]), False
    origin = get_origin(annotation)
    args = get_args(annotation)
    if origin is UnionType or origin is Union:
        args = list(filter(lambda x: x is not NoneType, args))
        if len(args) == 1:
            return get_type(args[0])
        else:
            return None, False
    if origin is list:
        return args[0], True
    elif origin is tuple:
        return tuple(get_type(x)[0] for x in args), False
    return annotation, False
