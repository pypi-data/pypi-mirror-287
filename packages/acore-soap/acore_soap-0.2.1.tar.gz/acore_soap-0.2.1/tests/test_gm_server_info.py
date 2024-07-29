# -*- coding: utf-8 -*-

from acore_soap.gm.server_info import (
    SOAPResponse,
    ServerInfoResponse,
)


class TestServerInfoResponse:
    def test_parse_server_uptime(self):
        # fmt: off
        assert ServerInfoResponse.extract_server_uptime("Server uptime: 34 second(s)") == 34
        assert ServerInfoResponse.extract_server_uptime("Server uptime: 6 minute(s) 29 second(s)") == 389
        assert ServerInfoResponse.extract_server_uptime("Server uptime: 1 hour(s) 6 minute(s) 29 second(s)") == 3989
        assert ServerInfoResponse.extract_server_uptime("Server uptime: 1 day(s) 1 hour(s) 6 minute(s) 29 second(s)") == 90389
        # fmt: one

    def test_from_soap_response(self):
        soap_response = SOAPResponse(
            body="",
            message="AzerothCore rev. 278ee2a72836 2024-06-13 21:52:22 +0200 (master branch) (Unix, RelWithDebInfo, Static)\r\nConnected players: 1000. Characters in world: 700.\r\nConnection peak: 0.\r\nServer uptime: 34 second(s)\r\nUpdate time diff: 1ms. Last 500 diffs summary:\r\n- Mean: 1ms\r\n- Median: 1ms\r\n- Percentiles (95, 99, max): 2ms, 12ms, 17ms",
            succeeded=True,
        )
        res = ServerInfoResponse.from_soap_response(soap_response)
        assert res.connected_players == 1000
        assert res.characters_in_world == 700
        assert res.server_uptime == 34


if __name__ == "__main__":
    from acore_soap.tests import run_cov_test

    run_cov_test(__file__, "acore_soap.gm.server_info", preview=False)
