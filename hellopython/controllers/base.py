from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
import time
from yaspin import yaspin
from cement import shell

VERSION_BANNER = """
Hello Python! %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Hello Python!'

        # text displayed at the bottom of --help output
        epilog = 'Usage: hellopython command1 --foo bar'

        # controller level arguments. ex: 'hellopython --version'
        arguments = [
            ### add a version banner
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='example sub command1',

        # sub-command level arguments. ex: 'hellopython command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
              'action': 'store',
              'dest': 'foo'}),
        ],
    )
    def command1(self):
        """Example sub-command."""

        data = {
            'foo': 'bar',
        }

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo

        self.app.render(data, 'command1.jinja2')

    @ex(
        help='example sub command2',

        # sub-command level arguments. ex: 'hellopython command2 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
              'action': 'store',
              'dest': 'foo'}),
        ],
    )
    def command2(self):

        """Example sub-command."""

        data = {
            'foo': 'bar2',
        }

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo

        self.app.render(data, 'command2.jinja2')

    @ex(
        help='example sub command3',

        # sub-command level arguments. ex: 'hellopython command3 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
              'action': 'store',
              'dest': 'foo'}),
        ],
    )
    @yaspin(text="Loading...")
    def command3(self):

        """Example third sub-command."""

        time.sleep(3)  # time consuming code

        data = {
            'foo': 'bar3',
        }

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo

        self.app.render(data, 'command3.jinja2')

    @ex(
        help='example sub command4',

        # sub-command level arguments. ex: 'hellopython command4 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
              'action': 'store',
              'dest': 'foo'}),
        ],
    )
    @yaspin(text="Loading...")
    def command4(self):

        """Example third sub-command."""

        time.sleep(1)  # time consuming code

        ### execute command with output to console
        out, err, code = shell.cmd('git status')

        data = {
            'foo': 'bar3',
            'out': out
        }

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo



        self.app.render(data, 'command4.jinja2')

