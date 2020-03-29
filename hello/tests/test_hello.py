
from pytest import raises
from hello.main import HelloTest

def test_hello():
    # test hello without any subcommands or arguments
    with HelloTest() as app:
        app.run()
        assert app.exit_code == 0


def test_hello_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with HelloTest(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_command1():
    # test command1 without arguments
    argv = ['command1']
    with HelloTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'bar'
        assert output.find('Foo => bar')


    # test command1 with arguments
    argv = ['command1', '--foo', 'not-bar']
    with HelloTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'not-bar'
        assert output.find('Foo => not-bar')



def test_world():
    argv = ['test']
    with HelloTest(argv=argv) as app:
        app.run()

    argv = ['huh', 'abc', '--arg2', '123']
    with HelloTest(argv=argv) as app:
        app.run()

    argv = ['jinja-test', 'arg1', 'arg2']
    with HelloTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['item1'] == 'arg1'
        assert output.find('Item1 is ')
