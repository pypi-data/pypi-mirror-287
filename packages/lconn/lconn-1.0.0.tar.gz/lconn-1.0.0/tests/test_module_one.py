import unittest
from your_package_name import LCon, Hoster, SetupError, HostingError, InvalidArg
import asyncio

class TestYourPackage(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.get_event_loop()

    def test_lcon_setup(self):
        async def run_test():
            lcon = await LCon()
            await lcon["setup"]({"host": "127.0.0.1", "port": 4001, "protocol": "http", "location": "data"})
            status = await lcon["get"]("all")
            self.assertEqual(status["status"], False)
            await lcon["reset"]()
        self.loop.run_until_complete(run_test())

    def test_hoster(self):
        async def run_test():
            stop_server = await Hoster(port=4001, location="data")
            await stop_server()
        self.loop.run_until_complete(run_test())

if __name__ == "__main__":
    unittest.main()