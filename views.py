# views.py

# aiohttp imports
from aiohttp import web

default_py_code = """import sys
import os

if __name__ == "__main__":
    print "Hello Python World!!"
"""

class RunPyCode:

    def __init__(self, code=None):

        self.code = code
        if not os.path.exists('running'):
            os.mkdir('running')
    
    async def get_history_bars(self, request: web.Request) -> web.json_response:


    def runpy(code = default_py_code):
        resrun = 'No result!'
        rescompil = "No compilation for Python"
    

    # def _run_py_prog(self, cmd="a.py"):
    #     cmd = [sys.executable, cmd]
    #     p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     result = p.wait()
    #     a, b = p.communicate()
    #     self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
    #     return result
    
    # def run_py_code(self, code=None):
    #     filename = "./running/a.py"
    #     if not code:
    #         code = self.code
    #     with open(filename, "w") as f:
    #         f.write(code)
    #     self._run_py_prog(filename)
    #     return self.stderr, self.stdout