import pytest

def pytest_html_report_title(report):
    report.title = "Report Pytest HTML"


@pytest.fixture(scope='function', autouse=True)
def hooks_function(request):
    # BEFORE TEST
    print("\nBEFORE TEST")

    yield
    # AFTER TEST
    print("\nAFTER TEST")


@pytest.fixture(scope='session', autouse=True)
def hooks_suite(request):
    # BEFORE SUITE
    print("\nBEFORE SUITE")

    yield
    # AFTER SUITE
    print("\nAFTER SUITE")
