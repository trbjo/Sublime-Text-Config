import sublime
import sublime_plugin
# import re


class ToggleTodoCommand(sublime_plugin.WindowCommand):
    todo='/home/tb/org/todo.org'
    def run(self):
        if self.window.active_view().file_name() == self.todo:
            self.window.run_command('save')
            self.window.run_command('close')
        else:
            self.window.open_file(self.todo + ':999', sublime.ENCODED_POSITION)



