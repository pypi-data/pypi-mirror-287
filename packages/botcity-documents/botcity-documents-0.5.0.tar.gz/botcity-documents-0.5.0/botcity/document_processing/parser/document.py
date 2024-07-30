from typing import Any, Callable, List, Optional, TypeVar, Union

from ..geometry import Point, Polygon
from .entry import Entry
from .matcher import DataTypeMatcher

F = TypeVar('F', bound=Callable[..., Any])


TOKENS_MAP = {
    " ": False,
    # ":": True,
    # "/": True,
    # "-": True
}


def multisplit(text):
    def split_token(part_text, token, keep):
        # print(f"Split {part_text} with '{token}'.")
        if token not in part_text:
            return [part_text]
        parts = part_text.split(token)
        if not keep:
            return parts
        ret = []
        for i, p in enumerate(parts):
            ret.append(p)
            if i < len(parts)-1:
                ret.append(token)
        return ret

    def process_token(items, token, keep):
        # print(f"Process Token for {items} with '{token}'.")
        t_ret = []
        for itm in items:
            t_ret.extend(split_token(itm, token, keep))
        return t_ret

    items = [text]
    for token, keep in TOKENS_MAP.items():
        items = process_token(items, token, keep)

    return [itm for itm in items if itm]


class DocumentParser:
    def __init__(self) -> None:
        self._entries = []

    def clear(self):
        """Clear the list of entries.
        """
        self._entries.clear()

    def print(self):
        """Print the list of entries.
        """
        for e in self.get_entries():
            print(f"->{e.text} ({e.p1.x}, {e.p1.y} - {e.p4.x}, {e.p4.y})")

    def add_entry(self, entry: Entry):
        """Add an entry into the parser list.

        Args:
            entry (Entry): The entry to be added.
        """
        entry.index = len(self._entries)
        self._entries.append(entry)

    def get_entries(self) -> List[Entry]:
        """The parser entries.

        Returns:
            List[Entry]: The parser entries.
        """
        return self._entries

    def set_entries(self, entries: List[Entry], sort: bool = True):
        """Sets the list of entries.

        Args:
            entries (List[Entry]): List of entries.
            sort (bool, optional): Sort the entries. Defaults to True.
        """
        self.clear()
        for entry in entries:
            self.add_entry(entry)
        if sort:
            self._sort_entries()

    def _sort_entries(self):
        # TODO: Research a way to fix the find algorithms to take
        # into consideration the non-sequential aspect of items
        # self._entries.sort(key=lambda e: (e.p1.y, e.p1.x))
        self._entries.sort(key=lambda e: (e.p1.y, e.p1.x))
        for idx, e in enumerate(self._entries):
            e.index = idx

    def load_entries(self, entries: List, sort: bool = True):
        """Load entries into the parser.

        Args:
            entries (List): List of Entry objects or
                List of List containing the required information.
            sort (bool, optional): Sort the entries. Defaults to True.
        """
        if isinstance(entries[0], Entry):
            self.set_entries(entries, sort)
        else:
            # Parse the list of list items and create entry
            ens = []
            for entry_data in entries:
                text = entry_data[0]
                p1x = int(entry_data[1])
                p1y = int(entry_data[2])
                p2x = int(entry_data[3])
                p2y = int(entry_data[4])
                p3x = int(entry_data[5])
                p3y = int(entry_data[6])
                p4x = int(entry_data[7])
                p4y = int(entry_data[8])
                try:
                    page = int(entry_data[9])
                except IndexError:
                    page = 1

                en = Entry()
                en.text = text
                en.page = page
                en.p1 = Point(p1x, p1y)
                en.p2 = Point(p2x, p2y)
                en.p3 = Point(p3x, p3y)
                en.p4 = Point(p4x, p4y)
                ens.append(en)
            self.set_entries(ens, sort)

    def get_full_text(self) -> str:
        """Returns the full document text.

        Returns:
            str: The document text.
        """
        return " ".join([entry.text for entry in self.get_entries()])

    def combined_entries(self, *args) -> Entry:
        """Combine a list of entries into a new merged entry.

        Returns:
            Entry: The new merged entry.
        """
        if isinstance(args[0], int):
            start, end = args
            # Python does not include the end so we need to +1
            entries = self.get_entries()[start: end+1]
        elif isinstance(args[0], list):
            entries = args[0]

        text = ""
        x1 = x2 = y1 = y2 = -1

        for e in entries:
            text += e.text
            if x1 == -1 or e.p1.x < x1:
                x1 = e.p1.x
            if x2 == -1 or e.p2.x > x2:
                x2 = e.p2.x
            if y1 == -1 or e.p1.y < y1:
                y1 = e.p1.y
            if y2 == -1 or e.p4.y > y2:
                y2 = e.p4.y

        entry = Entry()
        entry.index = entries[-1].index
        entry.text = text
        entry.p1 = Point(x1, y1)
        entry.p2 = Point(x2, y1)
        entry.p3 = Point(x2, y2)
        entry.p4 = Point(x1, y2)

        return entry

    def _index_from_entry(self, entry):
        if isinstance(entry, Entry):
            index = min(entry.index+1, len(self.get_entries()))
        elif isinstance(entry, int):
            index = entry
        return index

    def get_n_entry(self, text: Optional[str] = "", entry: Optional[Union[int, Entry]] = 0,
                    count: Optional[int] = 1) -> Entry:
        """Get the nth entry corresponding to the parameters.

        Args:
            text (Optional[str], optional): The entry text. Defaults to "".
            entry (Optional[Union[int, Entry]], optional): Reference Entry or index to use as start
                point for the search. Defaults to 0.
            count (Optional[int], optional): Index of search to return. 1 means first entry,
                2 means second entry, etc. Defaults to 1.

        Returns:
            Entry: The corresponding entry.
        """
        if not text:
            return self._entries[0] if self._entries else None

        start_index = self._index_from_entry(entry)
        texts = multisplit(text)

        # print("texts: ", texts)

        n_count = 0
        current = 0
        first = None

        i = start_index-1
        while i < len(self.get_entries())-1:
            i += 1
            entry = self.get_entries()[i]
            if entry.text == texts[current]:
                # print("Match: ", entry)
                n_count += 1
                if n_count == count and not first:
                    first = entry
                if count > 1:
                    if n_count >= count:
                        current += 1
                else:
                    current += 1
                if current == len(texts):
                    return self.combined_entries(first.index, first.index+len(texts)-1)
            else:
                i -= current
                current = 0
                first = None
                if count == 1:
                    n_count = 0
        return None

    def get_first_entry(self, text: Optional[str] = "", entry: Optional[Union[int, Entry]] = 0) -> Entry:
        """Get the first entry which meets the text criteria.

        Args:
            text (Optional[str], optional): The entry text. Defaults to "".
            entry (Optional[Union[int, Entry]], optional): Reference Entry or index to use as start
                point for the search. Defaults to 0.

        Returns:
            Entry: The corresponding entry.
        """
        return self.get_n_entry(text=text, entry=entry, count=1)

    def get_second_entry(self, text: Optional[str] = "", entry: Optional[Union[int, Entry]] = 0) -> Entry:
        """get the second entry which meets the text criteria.

        Args:
            text (Optional[str], optional): The entry text. Defaults to "".
            entry (Optional[Union[int, Entry]], optional): Reference Entry or index to use as start
                point for the search. Defaults to 0.

        Returns:
            Entry: The corresponding entry.
        """
        return self.get_n_entry(text=text, entry=entry, count=2)

    def get_last_entry(self) -> Entry:
        """Get the last entry on the parser's entry list.

        Returns:
            Entry: The last entry.
        """
        return self.get_entries()[-1]

    def get_first_entry_contains(self, text: Optional[str] = "", entry: Optional[Union[int, Entry]] = 0) -> Entry:
        """Get the first entry which contains the text criteria.

        Args:
            text (Optional[str], optional): The entry partial text. Defaults to "".
            entry (Optional[Union[int, Entry]], optional): Reference Entry or index to use as start
                point for the search. Defaults to 0.

        Returns:
            Entry: The corresponding entry.
        """
        start_index = self._index_from_entry(entry)

        i = start_index-1
        while i < len(self.get_entries())-1:
            i += 1
            entry = self.get_entries()[i]
            if text in entry.text:
                return entry
        return None

    def _read_area_using_line_height(self, polygon: Polygon, line_height: int) -> str:
        ret = ""

        curr_y = -1
        for entry in self.get_entries():
            if polygon.contains(Polygon([entry.p1, entry.p2, entry.p3, entry.p4])):
                pre = ""
                if curr_y != -1 and entry.p1.y > (curr_y + line_height):
                    pre = "\n"  # TODO: Check if use os.linesep
                    curr_y = entry.p1.y
                else:
                    pre = " "
                if curr_y == -1:
                    curr_y = entry.p1.y

                ret += pre + entry.text
        return ret

    def _read_area_polygon(self, polygon: Polygon) -> str:
        ret = ""
        separator = " "
        # last_entry = None

        for entry in self.get_entries():
            if polygon.contains(Polygon([entry.p1, entry.p2, entry.p3, entry.p4])):
                ret += separator + entry.text
                # last_entry = entry
        return ret

    def _read_area(self, p1: Point, p2: Point, p3: Point, p4: Point,
                   line_height: Optional[int] = None, debug: Optional[bool] = False, data_type=None) -> str:
        if debug:
            msg = f"######### trying to read ({p1.x}, {p1.y}), ({p2.x}, {p2.y}),({p3.x}, {p3.y}),({p4.x}, {p4.y})"
            print(msg)

        polygon = Polygon([p1, p2, p3, p4])
        if line_height is None:
            ret = self._read_area_polygon(polygon)
        else:
            ret = self._read_area_using_line_height(polygon, line_height)

        if data_type is not None:
            return DataTypeMatcher.match(ret.strip(), data_type)
        else:
            return ret.strip()

    def read(self, entry: Entry,
             margin_left: float, margin_right: float,
             margin_top: float, margin_bottom: float,
             line_height: Optional[int] = None, data_type=None,
             right_reference: Optional[Entry] = None,
             bottom_reference: Optional[Entry] = None) -> str:
        """Read an area and return its content.

        Args:
            entry (Entry): The anchor entry.
            margin_left (float): Proportion from the anchor's left corner.
            margin_right (float): Proportion from the anchor's right corner.
            margin_top (float): Proportion from the anchor's top.
            margin_bottom (float): Proportion from the anchor's bottom.
            line_height (Optional[int], optional): Line height for compensation. Defaults to None.
            data_type ([type], optional): Expected data type for use with OCR to correct for possible
                reading artifacts. Defaults to None.
            right_reference (Optional[Entry], optional): Reference Entry to use as right
                anchor. Defaults to None.
            bottom_reference (Optional[Entry], optional): Reference Entry to use as bottom
                anchor. Defaults to None.

        Returns:
            str: The text content from the area.
        """
        x1 = int(entry.p1.x + (entry.width*margin_left))
        y1 = int(entry.p1.y + (entry.height*margin_right))

        x2 = int(x1 + (entry.width*margin_top))
        y2 = int(y1 + (entry.height*margin_bottom))

        if right_reference is not None:
            x2 = right_reference.p1.x

        if bottom_reference is not None:
            y2 = bottom_reference.p1.y

        return self._read_area(
            Point(x1, y1), Point(x2, y1), Point(x2, y2), Point(x1, y2),
            line_height=line_height, data_type=data_type
        )
