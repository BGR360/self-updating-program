from app.version import __version__

class SelfUpdatingApp():
    def print_version(self):
        print('self-updating-app v{}'.format(__version__))

    def run(self):
        self.print_version()
        print('Hello world!')
