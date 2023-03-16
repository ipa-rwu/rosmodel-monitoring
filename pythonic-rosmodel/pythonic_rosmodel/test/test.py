from __future__ import unicode_literals

from pathlib import Path

import pythonic_rosmodel.textx_syntax as textx_syntax
from pythonic_rosmodel.metamodel_gen import primitives, ros
from textx import metamodel_from_file
from textx.export import metamodel_export

textx_syntax_folder = Path(textx_syntax.__file__).parent
model_tx_filename = Path("Ros.tx")
export_metamodel_file = Path(
    Path(__file__).parent / model_tx_filename.with_suffix('.dot'))


def main(debug=False):

    mm = metamodel_from_file(
        file_name=Path(textx_syntax_folder / model_tx_filename), classes=[ros.TopicSpec, ros.Namespace, ros.Publisher, primitives.MessagePart, ros.MessageDefinition], debug=debug)
    metamodel_export(mm, export_metamodel_file)


if __name__ == '__main__':
    main()
