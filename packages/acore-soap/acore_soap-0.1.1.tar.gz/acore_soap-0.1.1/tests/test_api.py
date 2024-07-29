# -*- coding: utf-8 -*-

from acore_soap import api


def test():
    _ = api
    _ = api.SOAPResponseParseError
    _ = api.SOAPCommandFailedError
    _ = api.SOAPRequest
    _ = api.SOAPResponse
    _ = api.gm.GMCommandRequest
    _ = api.gm.GMCommandResponse
    _ = api.gm.ServerInfoRequest
    _ = api.gm.ServerInfoResponse
    _ = api.gm.CreateAccountRequest
    _ = api.gm.CreateAccountResponse
    _ = api.gm.ChangeAccountPasswordRequest
    _ = api.gm.ChangeAccountPasswordResponse
    _ = api.gm.SetAccountPasswordRequest
    _ = api.gm.SetAccountPasswordResponse
    _ = api.gm.SetAccountGmlevelRequest
    _ = api.gm.SetAccountGmlevelResponse
    _ = api.gm.AddItemRequest
    _ = api.gm.AddItemResponse


if __name__ == "__main__":
    from acore_soap.tests import run_cov_test

    run_cov_test(__file__, "acore_soap.api", preview=False)
