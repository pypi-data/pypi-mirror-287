import argparse
import json
import logging
import sys
from dataclasses import asdict
from dataclasses import dataclass
from importlib.metadata import version
from io import TextIOWrapper

from typing_extensions import Literal
from typing_extensions import Sequence

from . import database
from .logger import LOGGER
from .services.preprocessor.process import Process
from .services.translator.translator import Translator
from .services.translator.translator import TranslatorBuilder
from .types import Convert


def argumentParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="kancolatex",
        description="a tool generate latex from AirDefense Calculator",
    )

    parser.add_argument(
        "-m",
        "--mode",
        metavar="mode",
        type=str,
        choices=["default", "export", "translate"],
        default="default",
        help="operation Mode, option: [default, export, translate]",
    )

    parser.add_argument(
        "-n",
        "--noro",
        metavar="fleet.json",
        type=argparse.FileType("r"),
        help="path to the fleet json.",
    )

    parser.add_argument(
        "-t",
        "--template",
        metavar="template.tex",
        type=argparse.FileType("r"),
        help="path to the template latex file.",
    )

    parser.add_argument(
        "-o",
        "--output",
        metavar="output.tex",
        type=argparse.FileType("w"),
        help="path to the output latex file. If not specific the result will be display to stdout.",
    )

    parser.add_argument(
        "--update",
        action="store_true",
        help="update ship, equipment and fit bonus.",
    )

    parser.add_argument(
        "--reset",
        action="store_true",
        help="reset the database. Old record will be missing.",
    )

    parser.add_argument("--debug", action="store_true", help="enable debug message")

    parser.add_argument(
        "-tse",
        "--translation-ships-en",
        metavar="translation_ships_en.json",
        type=argparse.FileType("r"),
        help="path to the json of english translation for ships",
    )

    parser.add_argument(
        "-tee",
        "--translation-equipments-en",
        metavar="translation_equipment_en.json",
        type=argparse.FileType("r"),
        help="path to the json of english translation for equipments",
    )

    parser.add_argument("--version", action="store_true", help="current version")

    parser.add_argument(
        "--name-type",
        metavar="translate_type",
        type=str,
        choices=["ship", "equipment"],
        help="target type want to translate, option: [ship, equipment]",
    )

    parser.add_argument(
        "--target",
        metavar="translate_target",
        type=str,
        help="target want to translate",
    )

    return parser


@dataclass(slots=True)
class Args:
    mode: Literal["default", "export", "translate"]
    noro: TextIOWrapper | None
    template: TextIOWrapper | None
    output: TextIOWrapper | None
    update: bool
    reset: bool
    debug: bool
    translation_ships_en: TextIOWrapper | None
    translation_equipments_en: TextIOWrapper | None
    version: bool
    name_type: Literal["ship", "equipment"] | None
    target: str | None


_SUCCESS = 0
_ERROR = 1


class _Helper:
    @classmethod
    def mode_Default(cls, args: Args):
        if args.noro and args.template:

            fleetInfo = cls._createFleetInfo(args.noro)

            _translator = cls._createTranslator(
                args.translation_ships_en, args.translation_equipments_en
            )

            p = Process(fleetInfo, args.template, _translator)
            result = p.process()
            if args.output and not p.errorCount:
                args.output.write(result.getvalue())
            elif not p.errorCount:
                return print(result.getvalue())

        elif args.noro and args.template is None:
            LOGGER.info("Please provide a template.")
            sys.exit(_ERROR)
        elif args.noro is None and args.template:
            LOGGER.info("Please provide a deck builder json.")
            sys.exit(_ERROR)

    @classmethod
    def mode_Export(cls, args: Args):
        if args.noro is None:
            LOGGER.info("Please provide a deck builder json.")
            sys.exit(_ERROR)

        fleetInfo = cls._createFleetInfo(args.noro)

        import pydantic

        class _J(json.JSONEncoder):
            def default(self, o: object):
                if isinstance(o, pydantic.BaseModel):
                    return o.model_dump()

                return super().default(o)

        return json.dumps(asdict(fleetInfo), cls=_J, ensure_ascii=False)

    @classmethod
    def mode_Translate(cls, args: Args):
        if args.target is None:
            LOGGER.info("Please provide a target to translate.")
            sys.exit(_ERROR)

        _translator = cls._createTranslator(
            args.translation_ships_en, args.translation_equipments_en
        )

        _translateResult: str = ""
        if args.name_type == "ship":
            _translateResult = _translator.translate_ship(args.target)
        elif args.name_type == "equipment":
            _translateResult = _translator.translate_equipment(args.target)

        print(_translateResult)

    @classmethod
    def _createFleetInfo(cls, _f: TextIOWrapper):
        fleetInfo = Convert.loadDeckBuilderToFleetInfo(_f.read())

        if fleetInfo is None:
            LOGGER.fatal("fleetInfo is None")
            sys.exit(_ERROR)

        return fleetInfo

    @classmethod
    def _createTranslator(cls, _s: TextIOWrapper | None, _e: TextIOWrapper | None):
        return Translator(
            builder=TranslatorBuilder(
                (json.loads(_s.read()) if _s is not None else dict()),
                (json.loads(_e.read()) if _e is not None else dict()),
            )
        )


def main(argv: Sequence[str] | None = None):

    parser = argumentParser()
    _parsedResult = parser.parse_args(argv)
    args = Args(**vars(_parsedResult))

    if args.debug:
        LOGGER.setLevel(logging.DEBUG)
        setattr(_parsedResult, "debug", False)
    setattr(_parsedResult, "mode", "")

    LOGGER.debug(f"{args = }")

    if all(not v for v in vars(_parsedResult).values()):
        parser.print_help()

    if args.version:
        print(version("kancolatex"))
        sys.exit(_SUCCESS)

    if args.reset:
        try:
            database.dbReset()
        except Exception as e:
            LOGGER.fatal(e)
            sys.exit(_ERROR)

    if args.update:
        try:
            database.dbUpdate()
        except Exception as e:
            LOGGER.fatal(e)
            sys.exit(_ERROR)

    if args.mode == "default":
        _Helper.mode_Default(args)
    elif args.mode == "export":
        _Helper.mode_Export(args)
    elif args.mode == "translate":
        _Helper.mode_Translate(args)

    sys.exit(_SUCCESS)
