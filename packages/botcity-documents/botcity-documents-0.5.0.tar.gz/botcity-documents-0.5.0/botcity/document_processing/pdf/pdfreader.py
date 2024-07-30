import os
import pathlib

import jpype
import jpype.imports

from ..geometry import Point
from ..parser import DocumentParser, Entry


def use_jvm():
    base_path = os.path.abspath(os.path.dirname(__file__))
    if not jpype.isJVMStarted():
        lib_dir = pathlib.Path(base_path)
        file_list = list(lib_dir.glob('*.jar'))
        for fl in file_list:
            jpype.addClassPath(fl)
        jpype.startJVM(
            jpype.getDefaultJVMPath(),
            '-Djava.awt.headless=true',
            '-Dorg.slf4j.simpleLogger.defaultLogLevel=off',
            '-Dorg.apache.commons.logging.Log=org.apache.commons.logging.impl.NoOpLog',
            convertStrings=False
        )


class PDFReader:
    def __init__(self) -> None:
        self._page_width = None
        self._page_height = None

    @property
    def page_width(self) -> float:
        """PDF Page width.
        """
        return self._page_width if self._page_width is None else 0.0

    @property
    def page_height(self) -> float:
        """PDF Page height.
        """
        return self._page_height if self._page_height is None else 0.0

    def read_file(self, file: str) -> DocumentParser:
        """Read the given PDF file and returns a new instance of the DocumentParser.

        Args:
            file (str): PDF file path.

        Returns:
            DocumentParser: The document parser to be used.
        """
        from dev.botcity.botcity_document_processing.pdf import PdfReader
        from java.io import File

        filepath = os.path.abspath(os.path.expanduser(os.path.expandvars(file)))

        reader = PdfReader()
        f = File(filepath)
        error = False
        try:
            parser = reader.readFile(f)
            j_entries = parser.getEntries()

            entries = []
            for j_en in j_entries:
                entry = Entry()
                entry.text = str(j_en.getText())
                entry.page = int(j_en.getPage())
                entry.p1 = Point(float(j_en.p1.x), float(j_en.p1.y))
                entry.p2 = Point(float(j_en.p2.x), float(j_en.p2.y))
                entry.p3 = Point(float(j_en.p3.x), float(j_en.p3.y))
                entry.p4 = Point(float(j_en.p4.x), float(j_en.p4.y))
                entries.append(entry)

            self._page_height = float(reader.getPageHeight())
            self._page_width = float(reader.getPageWidth())
            parser = DocumentParser()
            parser.load_entries(entries)
            return parser
        except jpype.JException:
            # We must ignore the exception here to hide the Java message.
            error = True
        if error:
            raise ValueError(f"Error while reading the file '{
                             file}'. The file is either invalid or damaged. Please check.")


use_jvm()
