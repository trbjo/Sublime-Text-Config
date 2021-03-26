import subprocess
import sublime
import sublime_plugin


class SendMailCommand(sublime_plugin.TextCommand):
    def run(self, edit):
            def on_done(input_string):
                # self.view.run_command("move_to", {"to": "bof"})
                # self.view.run_command("insert", {"characters": input_string})
                process = subprocess.Popen(['msmtp', 'troels@bjoernskov.org'], stdin=subprocess.PIPE)
                # process.communicate(self.view.substr(sublime.Region(0, self.view.size())))
                process.communicate(self.view.substr(sublime.Region(0, self.view.size())).encode(encoding='UTF-8',errors='strict'))

            def on_change(input_string):
                print("Input changed: %s" % input_string)

            def on_cancel():
                print("User cancelled the input")

            window = self.view.window()
            window.show_input_panel("Text to Insert:", "Hello, World!",
                                     on_done, on_change, on_cancel)
