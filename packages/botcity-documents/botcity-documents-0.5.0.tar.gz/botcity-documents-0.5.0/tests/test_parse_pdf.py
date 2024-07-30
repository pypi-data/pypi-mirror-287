import os

cur_dir = os.path.abspath(os.path.dirname(__file__))


def test_parse_pdf():
    # Import the packages
    from botcity.document_processing import PDFReader

    # Read the file and instantiate the reader
    parser = PDFReader().read_file(os.path.join(cur_dir, "statement.pdf"))

    _account_no = parser.get_first_entry("Account No:")
    value = parser.read(_account_no, 1.218045, -3.285714, 1.37594, 5.142857)
    assert value == "1023456789-0"

    _statement_date = parser.get_first_entry("Statement Date:")
    value = parser.read(_statement_date, 1.16, -2.142857, 1.057143, 3.714286)
    assert value == "03/08/2016"

    _due_date = parser.get_first_entry("Due Date:")
    value = parser.read(_due_date, 1.234234, -2.428571, 1.693694, 5.285714)
    assert value == "03/29/2016"

    _service_for = parser.get_first_entry("Service For:")
    value = parser.read(_service_for, -0.079137, 1.857143, 1.143885, 4.428571)
    assert value == "Jane Smith"

    _service_for = parser.get_first_entry("Service For:")
    value = parser.read(_service_for, -0.086331, 6.857143, 1.877698, 7)
    assert "1234 Main Street" in value

    _amount_due = parser.get_first_entry("Current Electric Charges")
    value = parser.read(_amount_due, 2.551724, -2, 1.262069, 4.666667)
    assert value == "$115.28"
