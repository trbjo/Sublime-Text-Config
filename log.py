import sublime
import sublime_plugin

class SetDotnetSyntaxHotwalletCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.set_timeout(lambda: self.window.active_view().set_syntax_file("Packages/User/Dotnet.sublime-syntax"), 100)
        sublime.set_timeout(lambda: self.window.active_view().set_name("HotWallet"), 100)

class SetDotnetSyntaxDepositCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.set_timeout(lambda: self.window.active_view().set_syntax_file("Packages/User/Dotnet.sublime-syntax"), 100)
        sublime.set_timeout(lambda: self.window.active_view().set_name("Deposit"), 100)

class SetDotnetSyntaxDefaultCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.set_timeout(lambda: self.window.active_view().set_syntax_file("Packages/User/Dotnet.sublime-syntax"), 100)
        sublime.set_timeout(lambda: self.window.active_view().set_name("Bank"), 100)

