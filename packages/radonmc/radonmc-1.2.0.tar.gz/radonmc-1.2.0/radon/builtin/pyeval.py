from ..error import raise_error
from ..tokenizer import GroupToken
from ..transpiler import FunctionDeclaration, TranspilerContext, add_lib


def lib_eval(_ctx: TranspilerContext, token: GroupToken):
    try:
        eval(token.value[7:-1])
    except Exception as e:
        raise_error("Eval error", str(e), token)


def lib_exec(_ctx: TranspilerContext, token: GroupToken):
    try:
        exec(token.value[7:-1])
    except Exception as e:
        raise_error("Eval error", str(e), token)


add_lib(FunctionDeclaration(
    type="python-raw",
    name="pyeval",
    returns="void",
    function=lib_eval,
))

add_lib(FunctionDeclaration(
    type="python-raw",
    name="pyexec",
    returns="void",
    function=lib_eval,
))
