# -*- coding: utf-8 -*-

import pytest
from pathlib import Path
from acore_soap.request import (
    SOAPRequest,
    SOAPResponse,
    SOAPResponseParseError,
    SOAPCommandFailedError,
    ensure_response_succeeded,
)

dir_here = Path(__file__).absolute().parent

path_fail1_wrong_command_xml = dir_here / "fail1_wrong_command.xml"
path_fail2_account_not_exists_xml = dir_here / "fail2_account_not_exists.xml"
path_success_xml = dir_here / "success.xml"
path_no_result_xml = dir_here / "no_result.xml"
path_no_faultstring_xml = dir_here / "no_faultstring.xml"


class TestSoapResponse:
    def test_parse(self):

        res = SOAPResponse.parse(path_fail1_wrong_command_xml.read_text())
        assert res.succeeded is False
        assert "Possible subcommands" in res.message

        res = SOAPResponse.parse(path_fail2_account_not_exists_xml.read_text())
        assert res.succeeded is False
        assert "Account not exist: TEST" in res.message

        res = SOAPResponse.parse(path_success_xml.read_text())
        assert res.succeeded is True
        assert "Account created: test" in res.message

        with pytest.raises(SOAPResponseParseError):
            SOAPResponse.parse("<a>hello</a>")

        res = SOAPResponse.parse(path_no_result_xml.read_text())
        assert res.succeeded is True
        assert res.message == "No result"

        res = SOAPResponse.parse(path_no_faultstring_xml.read_text())
        assert res.succeeded is False
        assert res.message == "No fault string"


def test_ensure_response_succeeded():
    soap_request = SOAPRequest(command=".server info")
    soap_response = SOAPResponse(
        body="this is body", message="this is message", succeeded=True
    )
    ensure_response_succeeded(
        request=soap_request,
        response=soap_response,
        raises=True,
    )

    soap_response = SOAPResponse(
        body="this is body", message="this is message", succeeded=False
    )
    with pytest.raises(SOAPCommandFailedError):
        ensure_response_succeeded(
            request=soap_request,
            response=soap_response,
            raises=True,
        )


if __name__ == "__main__":
    from acore_soap.tests import run_cov_test

    run_cov_test(__file__, "acore_soap.request", preview=False)
