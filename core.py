import gdb.printing


class ByteStringPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        res = '<empty>'
        stringDataPtr = self.val['m_pData']['m_pObj']['_M_t']['_M_t']['_M_head_impl']
        if not stringDataPtr:
            return res

        stringLen = stringDataPtr['m_nDataLength']
        if stringLen == 0:
            return res

        stringContent = stringDataPtr['m_String'].reinterpret_cast(gdb.lookup_type('unsigned char').pointer())
        try:
            res = stringContent.string('', 'strict', stringLen)
        except:
            res = ''.join('<%d>' % stringContent[i] for i in range(stringLen))

        return res


def build_pretty_printer():
    pp = gdb.printing.RegexpCollectionPrettyPrinter("pdfium")
    pp.add_printer('ByteString', '^fxcrt::ByteString$', ByteStringPrinter)
    return pp


printer = build_pretty_printer()
