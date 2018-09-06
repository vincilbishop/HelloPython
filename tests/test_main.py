
from hellopython.main import HelloPythonTest

def test_hellopython(tmp):
    with HelloPythonTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with HelloPythonTest(argv=argv) as app:
        app.run()
