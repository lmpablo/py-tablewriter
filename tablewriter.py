import math


class TableWriter(object):
    """
    @params
    padding : int - space at the left and right of field text
    min_width : int - minimum width of a column; used when not specified field-level
    max_width : int - maximum width of a column; used when not specified field-level
    """
    def __init__(self, padding=1, min_width=15, max_width=60):
        self.padding = padding
        self.min_width = min_width
        self.max_width = max_width
        

    """
    Supported settings:
        width : int - specified width for the column
        prefix : string - string to be prepended to the value
        postfix : string - string to be appended to the value
        align : string - center-, left-, or right-aligned
    """
    def write_table(self, table, title, headers, settings=None):
        hsizes = self.calculate_widths(headers, settings)
        is_header_caps = settings.get('$uppercase_headers', False)

        table_str = ""
 
        title = self.get_title_str(title, headers, hsizes)
        header = self.get_headers_str(headers, hsizes, is_header_caps)

        table_str += title
        table_str += header

        for row in table:
            row_str = self.get_row_str(row, headers, hsizes, settings)
            table_str += row_str
            table_str += "\n"

        table_str += self.get_hr(headers, hsizes)
        table_str += "\n"

        print table_str


    def calculate_widths(self, headers, settings):
        header_sizes = []
        for header in headers:
            if settings is not None and settings.get(header, None):
                width = settings[header].get('width', None)
                if width:
                    header_sizes.append(width)
                    continue
            combined = self.padding * 2 + len(header)
            hlength = max(combined, self.min_width)
            hlength = min(hlength, self.max_width)
            header_sizes.append(hlength)

        return header_sizes

    def get_hr(self, headers, header_sizes):
        n_bars = len(headers) + 1
        return "+" + ("-" * (sum(header_sizes) + n_bars - 2)) + "+"


    def get_pre_space(self, header, header_size):
        hlen = len(header)
        hmid = hlen / 2.0
        return int(math.ceil((header_size / 2) - hmid))


    def get_title_str(self, title, headers, header_sizes):
        print_str = ""
        topline = self.get_hr(headers, header_sizes)
        tlen = len(title)

        mid = (len(topline) - 2) / 2.0
        nspaces = int(math.ceil(mid - tlen / 2.0))
        nspaces_post = len(topline) - 2 - tlen - nspaces

        print_str += topline
        print_str += "\n"
        print_str += "|" + ((" " * nspaces) + title + (" " * nspaces_post)) + "|"
        print_str += "\n"

        return print_str


    def get_headers_str(self, headers, header_sizes, uppercase=False):
        new_headers = []
        topline = self.get_hr(headers, header_sizes)
        idx = 0
        for header in headers:
            if uppercase:
                header = header.upper()
            pre_space = self.get_pre_space(header, header_sizes[idx])
            post_space = header_sizes[idx] - len(header) - pre_space
            header = (" " * pre_space) + header + (" " * post_space)
            new_headers.append(header)
            idx += 1

        print_str = topline
        print_str += "\n"
        print_str += "|" + "|".join(new_headers) + "|"
        print_str += "\n"
        print_str += topline
        print_str += "\n"

        return print_str

    def get_row_str(self, row, headers, header_sizes, settings):
        row_values = []
        idx = 0
        for h in headers:
            hval = str(row.get(h, '-'))
            vlen = len(hval)
            hsize = header_sizes[idx]
            hsettings = settings.get(h, None)

            align = 'center'
            prefix = ''
            postfix = ''

            if hsettings:
                align = hsettings.get('align', 'center')
                prefix = hsettings.get('prefix', '')
                postfix = hsettings.get('postfix', '')

            if prefix or postfix:
                hval = prefix + hval + postfix
                vlen = len(hval)

            if align == 'center':
                pre_space = int(math.ceil((hsize / 2.0) - (vlen / 2.0)))
            elif align == 'left':
                pre_space = self.padding
            elif align == 'right':
                pre_space = hsize - vlen - self.padding
            
            post_space = hsize - pre_space - vlen
            row_data = (" " * pre_space) + hval + (" " * post_space)

            if len(row_data) > hsize:
                row_data = row_data[0:hsize - 4] + "... "

            row_values.append(row_data)


            idx += 1

        return "|" + "|".join(row_values) + "|"
