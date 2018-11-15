from cement import Controller, ex
from cement.utils.version import get_version_banner
from cement import shell
from cement import App, init_defaults

from ..core.version import get_version
import time

from yaspin import yaspin

from colorama import init, Fore, Back, Style
import emoji

from pymongo import MongoClient
from pythonwifi.iwlibs import Wireless
from PIL import Image

init()
# See: https://docs.builtoncement.com/extensions/daemon
DEFAULTS = init_defaults('hellopython', 'daemon')
DEFAULTS['daemon']['user'] = 'myuser'
DEFAULTS['daemon']['group'] = 'staff'
DEFAULTS['daemon']['dir'] = '/var/lib/hellopython/'
DEFAULTS['daemon']['pid_file'] = '/var/run/hellopython/myapp.pid'
DEFAULTS['daemon']['umask'] = 0


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

        config_defaults = DEFAULTS

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
        """Example fourth sub-command."""

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

    @ex(
        help='example sub command5',

        # sub-command level arguments. ex: 'hellopython command5 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
              'action': 'store',
              'dest': 'foo'}),
        ],
    )
    def command5(self):

        """Example fifth sub-command."""

        ### execute command with output to console
        out, err, code = shell.cmd('git status')

        data = {
            'foo': 'bar3',
            'out': out
        }

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo

        print(Fore.RED + 'some red text')
        print(Back.WHITE + 'and with a white background' + Style.RESET_ALL)
        print(Style.RESET_ALL + 'back to normal now')


    @ex(
        help='example sub command6',

        # sub-command level arguments. ex: 'hellopython command6 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
              'action': 'store',
              'dest': 'foo'}),
        ],
    )
    def command6(self):

        """Example sixth sub-command."""

        ### execute command with output to console
        out, err, code = shell.cmd('git status')

        data = {
            'foo': 'bar3',
            'out': out
        }

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo

        print(emoji.emojize('Python is :thumbs_up:'))
        print(emoji.emojize('Time for a :beer:', use_aliases=True))

    @ex(
        help='example mongodb subcommand',

        # sub-command level arguments. ex: 'hellopython command6 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
              'action': 'store',
              'dest': 'foo'}),
        ],
    )
    def command7(self):

        """Example hello mongo sub-command."""
        client = MongoClient('localhost', 27017)

        db = client['pymongo_test']
        posts = db.posts
        post_data = {
            'title': 'Python and MongoDB',
            'content': 'PyMongo is fun, you guys',
            'author': 'Scott'
        }
        result = posts.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id))

        print(emoji.emojize('Mongo DB :thumbs_up:'))

    @ex(
        help='example wifi subcommand',

        # sub-command level arguments. ex: 'hellopython command6 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-f', '--foo'],
             {'help': 'notorious foo option',
              'action': 'store',
              'dest': 'foo'}),
        ],
    )
    def command8(self):

        """Example hello wifi sub-command."""
        wifi = Wireless('eth0')
        print('SSID: {0}'.format(wifi.getEssid()))

        print(emoji.emojize('Python WiFi :thumbs_up:'))

ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            xrange(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath):
    image = None
    image = Image.open(image_filepath)


    image_ascii = convert_image_to_ascii(image)
    print image_ascii

if __name__=='__main__':
    import sys

    image_file_path = sys.argv[1]
    handle_image_conversion(image_file_path)