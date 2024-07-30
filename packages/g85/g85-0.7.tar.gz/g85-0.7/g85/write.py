from typing import TextIO, cast
from collections.abc import Sequence
import logging
import math
from dataclasses import fields
from xml.etree import ElementTree

from .main import Map, Device


logger = logging.getLogger(__name__)


class G85Error(Exception):
    pass


# Hack to directly pass through <![CDATA[...]]>
def _escape_cdata(text: str) -> str:
    if text.startswith('<![CDATA[') and text.endswith(']]>'):
        return text
    return _original_escape_cdata(text)


_original_escape_cdata = ElementTree._escape_cdata      # type: ignore
ElementTree._escape_cdata = _escape_cdata               # type: ignore
####


def write(maps: Sequence[Map], stream: TextIO) -> None:
    el_root = ElementTree.Element('Maps')

    for wmap in maps:
        write_wmap(wmap, el_root)

    tree = ElementTree.ElementTree(element=el_root)
    ElementTree.indent(tree)
    tree.write(stream)


def write_wmap(wmap: Map, el_root: ElementTree.Element) -> None:
    el_map = ElementTree.SubElement(el_root, 'Map')

    write_devices(wmap.devices, el_map)

    map_fields = [ff.name for ff in fields(wmap)]
    for field in map_fields:
        if field[0].isupper() or field == 'xmlns':
            val = getattr(wmap, field)
            if val is None:
                continue
            el_map.set(field, val)
    for key, value in wmap.misc.items():
        if key[0].isupper() and key in map_fields:
            continue
        el_map.set(key, value)


def write_devices(devices: Sequence[Device], el_map: ElementTree.Element) -> None:
    for device in devices:
        el_device = ElementTree.SubElement(el_map, 'Device')

        # ReferenceDevice
        if device.reference_xy is not None:
            el_ref = ElementTree.SubElement(el_device, 'ReferenceDevice')
            el_ref.set('ReferenceDeviceX', str(device.reference_xy[0]))
            el_ref.set('ReferenceDeviceY', str(device.reference_xy[1]))

        # Row data prep
        if device.map is None:
            raise G85Error(f'No _data for device pformat({device})')

        is_decimal = device.BinType == 'Decimal'
        row_texts, bin_length = prepare_data(device.map, decimal=is_decimal)

        # Bins
        if not device.bin_pass:
            logger.warning('No bins were provided!')

        bin_counts = device.bin_counts()

        for bin_code, passed in device.bin_pass.items():
            el_bin = ElementTree.SubElement(el_device, 'Bin')
            if is_decimal:
                el_bin.set('BinCode', str(bin_code).zfill(bin_length))
            else:
                el_bin.set('BinCode', str(bin_code))
            el_bin.set('BinQuality', 'Pass' if passed else 'Fail')
            el_bin.set('BinCount', str(bin_counts[bin_code]))

        el_data = ElementTree.SubElement(el_device, 'Data')
        for row_text in row_texts:
            el_row = ElementTree.SubElement(el_data, 'Row')
            el_row.text = f'<![CDATA[{row_text}]]>'

        # Device attribs
        dev_fields = [ff.name for ff in fields(device)]
        for field in dev_fields:
            if field[0].isupper():
                val = getattr(device, field)
                if val is None:
                    continue

                if field in ('WaferSize', 'DeviceSizeX', 'DeviceSizeY', 'Orientation'):
                    val = f'{val:g}'
                elif field in ('OriginLocation',):
                    val = f'{val:d}'
                elif field == 'CreateDate':
                    val = val.strftime('%Y%m%d%H%M%S%f')[:-3]
                elif field == 'NullBin' and device.BinType == 'Decimal':
                    val = f'{val:d}'

                el_device.set(field, val)

        for key, value in device.misc.items():
            if key[0].isupper() and key in dev_fields:
                continue
            el_device.set(key, value)

        for key, value in device.data_misc.items():
            el_data.set(key, value)

        if device.supplier_data:
            el_suppdata = ElementTree.SubElement(el_device, 'SupplierData')
            for key, value in device.data_misc.items():
                el_suppdata.set(key, value)


def prepare_data(data: list[list[str]] | list[list[int]], decimal: bool) -> tuple[list[str], int]:
    is_char = isinstance(data[0][0], str)

    row_texts = []
    if is_char:
        data = cast(list[list[str]], data)
        char_len = len(data[0][0])
        for srow in data:
            if char_len == 1:
                row_text = ''.join(srow)
            else:
                row_text = ' '.join(srow) + ' '
            row_texts.append(row_text)
        return row_texts, char_len
    else:       # noqa: RET505
        data = cast(list[list[int]], data)
        max_value = max(max(rr) for rr in data)
        max_digits = math.ceil(math.log10(max_value))
        for irow in data:
            row_text = ' '.join(str(vv).zfill(max_digits) for vv in irow) + ' '
            row_texts.append(row_text)
        return row_texts, max_digits
