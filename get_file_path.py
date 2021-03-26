from os import path
from sublime_plugin import TextCommand

class CopyFilenameCommand(TextCommand):
    def run(self, edit):
        f = open("/tmp/sublfile", "w")
        f.write(path.dirname(self.view.file_name()))
        f.close()
        # sublime.set_clipboard(path.dirname(self.view.file_name()))
        # sublime.status_message("Copied file name: %s" % self.view.file_name())

    def is_enabled(self):
        return True
        # return len(self.view.file_name()) > 0
