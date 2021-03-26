from os import path
import socket
import os
import re
import sublime
import sublime_plugin
import subprocess
# from Default.paste_from_history import g_clipboard_history

# class CopyInMacroCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         self.view.run_command('copy')
#         g_clipboard_history.push_text(sublime.get_clipboard())

# class CutInMacroCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         self.view.run_command('cut')
#         g_clipboard_history.push_text(sublime.get_clipboard())

class SampleListener(sublime_plugin.EventListener):
    def on_query_context(self, view, key, operator, operand, match_all):
        if key in ("goto_anything:input", "command_palette:input"):
            lhs = view.element() == key
            rhs = bool(operand)

            return lhs == rhs if operand != sublime.OP_EQUAL else lhs != rhs

        return None


# if socket.gethostname() == "Intel-NUC":
#     class hej(sublime_plugin.EventListener):
#         def on_load_async(self, view):
#             subprocess.Popen(['swaymsg', '[app_id=^subl$]', 'focus']).wait()
# else:
#     class hej(sublime_plugin.EventListener):
#         def on_load_async(self, view):
#             subprocess.Popen(['swaymsg', '[app_id=^subl$]', 'focus;', '[app_id=^(subl|sublime_text)$', 'workspace="^2λ$"]', 'fullscreen', 'enable']).wait()





class HighlightLine(sublime_plugin.EventListener):

#     def on_deactivated(self, view):
#         view.settings().set("highlight_line", False)

    def on_activated_async(self, view):
            if len(sublime.active_window().views()) > 1:
                sublime.active_window().set_tabs_visible(True)

    def on_deactivated_async(self, view):
            if len(sublime.active_window().views()) == 1:
                sublime.active_window().set_tabs_visible(False)

    # def on_activated_async(self, view):
    #         if sublime.active_window().num_groups() > 1:
    #             sublime.active_window().set_tabs_visible(True)
    #         else:
    #             sublime.active_window().set_tabs_visible(False)

    def on_new_async(self, view):
        if view.name() == 'Find Results':
            view.set_read_only(True)


# class RunAlacrittyCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         subprocess.Popen(['alacritty'], cwd=path.dirname(self.window.active_view().file_name()))


class ShowDiagnosticsNicelyCommand(sublime_plugin.WindowCommand):
    def is_enabled(self, internal=False, message=None):
            return True

    def run(self):
        panelView = self.window.find_output_panel("diagnostics")
        settings = panelView.settings()
        currentScheme = self.window.active_view().settings().get("color_scheme")
        # modScheme = currentScheme[:-21] + '_widget' + currentScheme[-21:]
        modScheme = currentScheme[:-21] + currentScheme[-21:]
        # settings.set("color_scheme", modScheme)
        settings.set("word_wrap", True)
        settings.set("font_face", "SF Pro Display Regular")
        settings.set("font_size", 10)
        settings.set("highlight_line", False)
        settings.set("gutter", True)
        if panelView is not None and panelView.size() != 28:
            sublime.active_window().run_command('show_panel', {'panel': 'output.diagnostics'})
            # sublime.active_window().focus_view(panelView)



class LspSaveAndMaybeHidePanelCommand(sublime_plugin.WindowCommand):
    def run(self):
        panelView = self.window.find_output_panel("diagnostics")
        if panelView.size() == 28:
            sublime.active_window().run_command('hide_panel', {'panel': 'output.diagnostics'})
        sublime.set_timeout(lambda: sublime.active_window().run_command('lsp_save'), 1000)

class LspSaveWithTimeOutCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.set_timeout(lambda: sublime.active_window().run_command('lsp_save'), 1000)

class PasteZshCommand(sublime_plugin.WindowCommand):
    def run(self):
        subprocess.Popen(['/usr/bin/pkill', 'zsh', '--signal=USR2']).wait()
        subprocess.Popen([ 'swaymsg', '[app_id="^PopUp$"]', 'scratchpad', 'show,', 'fullscreen', 'disable,', 'move', 'position', 'center,', 'resize', 'set', 'width', '1502px', 'height', '1002px,', 'resize', 'shrink', 'up', '1000px']).wait()





# class ShowTabAndSwitchCommand(sublime_plugin.WindowCommand):
#     counter = 0

#     def is_enabled(self, internal=False, message=None):
#             return True

#     def hidecounter(self):
#         self.counter-=1
#         if self.counter == 0:
#             sublime.active_window().set_tabs_visible(False)

#     def run(self):
#         self.counter+=1
#         sublime.active_window().set_tabs_visible(True)
#         sublime.active_window().run_command(self.command)
#         sublime.set_timeout(lambda: self.hidecounter(), 3000)

# class ShowTabAndNextCommand(ShowTabAndSwitchCommand):
#     command = 'next_view'
#     def op(self):
#         self.run()

# class ShowTabAndPrevCommand(ShowTabAndSwitchCommand):
#     command = 'prev_view'
#     def op(self):
#         self.run()

# class FocusNeighboringGroupAndShowTabCommand(ShowTabAndSwitchCommand):
#     command = 'focus_neighboring_group'
#     def op(self):
#         self.run()




class OpenOrganizingCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.active_window().open_file('/home/tb/Doc/Skrivebibliotek/noter-dansk.org')
        sublime.active_window().run_command('move_to_group', {"group": 1})
        # sublime.set_timeout(lambda: sublime.active_window().run_command('set_layout', {"cells": [[0, 0, 1, 1], [1, 0, 2, 1 ]]    , "cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0]}), 1100)

      
        # todo = sublime.active_window().find_open_file('/home/tb/Doc/Skrivebibliotek/noter-dansk.org')
        # def hej():
        #     while self.window.active_view().is_loading():
        #         sublime.set_timeout(lambda: hej, 200)

        # if todo is None:
        #    sublime.active_window().open_file('/home/tb/Doc/Skrivebibliotek/noter-dansk.org')
        # else:
        #    hej()
        #    sublime.active_window().focus_view(todo)










class DanishCommand(sublime_plugin.WindowCommand):
    def is_enabled(self, internal=False, message=None):
        if self.window.active_view().file_name()[-3:] == 'org':
            return True
        else:
            return False
    def run(self):
        sublime.active_window().run_command('set_user_setting', {"file": "Preferences.sublime-settings", "setting": "dictionary", "value": "Dictionaries/da_DK.dic"})
        sublime.active_window().run_command('set_user_setting', {"file": "Preferences.sublime-settings", "setting": "english", "value": False})

class EnglishCommand(sublime_plugin.WindowCommand):
    def is_enabled(self, internal=False, message=None):
        if self.window.active_view().file_name()[-3:] == 'org':
            return True
        else:
            return False
    def run(self):
        sublime.active_window().run_command('set_user_setting', {"file": "Preferences.sublime-settings", "setting": "dictionary", "value": "Packages/Language - English/en_GB.dic"})
        sublime.active_window().run_command('set_user_setting', {"file": "Preferences.sublime-settings", "setting": "english", "value": True})

class GermanCommand(sublime_plugin.WindowCommand):
    def is_enabled(self, internal=False, message=None):
        if self.window.active_view().file_name()[-3:] == 'org':
            return True
        else:
            return False
    def run(self):
        sublime.active_window().run_command('set_user_setting', {"file": "Preferences.sublime-settings", "setting": "dictionary", "value": "Dictionaries/de_CH.dic"})
        sublime.active_window().run_command('set_user_setting', {"file": "Preferences.sublime-settings", "setting": "english", "value": False})


class SublimeProjectCommand(sublime_plugin.WindowCommand):
    def run(self):
        subprocess.Popen(['FindSublimeProject.sh'])

class OrgModeExportAsPdfCommand(sublime_plugin.WindowCommand):
    def is_enabled(self, internal=False, message=None):
        if self.window.active_view().file_name()[-3:] == 'org':
            return True
        else:
            return False

    def run(self):
        sublime.active_window().run_command('save')
        file='/home/tb/Export/' + path.basename(self.window.active_view().file_name())[:-3] + 'pdf'
        if not path.exists(file):
            subprocess.Popen(['emacs', self.window.active_view().file_name(), '--batch', '-l', '/home/tb/.emacs.d/init.el', '-f', 'org-latex-export-to-pdf', '--kill']).wait()
        else:
            subprocess.Popen(['emacs', self.window.active_view().file_name(), '--batch', '-l', '/home/tb/.emacs.d/init.el', '-f', 'org-latex-export-to-pdf', '--kill'])

        subprocess.Popen(['xdg-open', file])
        sublime.set_timeout(lambda: subprocess.Popen(['rm', '/home/tb/Export/' + path.basename(self.window.active_view().file_name())[:-3] + 'tex']), 6000)



class OrgModeExportAsHtmlAndOpenCommand(sublime_plugin.WindowCommand):
    def is_enabled(self, internal=False, message=None):
        if self.window.active_view().file_name()[-3:] == 'org':
            return True
        else:
            return False

    def run(self):
        sublime.active_window().run_command('save')
        subprocess.Popen(['emacs', self.window.active_view().file_name(), '--batch', '-l', '/home/tb/.emacs.d/init.el', '-f', 'org-html-export-to-html', '--kill']).wait()
        subprocess.Popen(['xdg-open', '/home/tb/Export/' + path.basename(self.window.active_view().file_name())[:-3] + 'html'])

class OrgModeExportAsRevealJsAndOpenCommand(sublime_plugin.WindowCommand):
    def is_enabled(self, internal=False, message=None):
        file = self.window.active_view().file_name()
        if file is not None and file[-3:] == 'org':
            return True
        else:
            return False

    def run(self):
        sublime.active_window().run_command('save')
        subprocess.Popen(['emacs', self.window.active_view().file_name(), '--batch', '-l', '/home/tb/.emacs.d/init.el', '-f', 'org-reveal-export-to-html', '--kill'])
        subprocess.Popen(['firefox-nightly', '/home/tb/Export/' + path.basename(self.window.active_view().file_name())[:-3] + 'html'])

# class FocusNextCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         subprocess.Popen(['swaymsg', 'focus', 'next']).wait()

# class RunDosToUnixCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         subprocess.Popen(['dos2unix', '--remove-bom', self.window.active_view().file_name() ])

# class RemoveChmodCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         subprocess.Popen(['chmod', '-x', self.window.active_view().file_name() ])

# class SetChmodCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         subprocess.Popen(['chmod', '+x', self.window.active_view().file_name() ])


class BuildWithSassCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.active_window().run_command('save')
        subprocess.Popen(['sass', 'scss/custom.scss:src/css/stylesheet.css'], cwd='/home/tb/Doc/Git/Pilatus.Bank/Pilatus.Bank.WS/ClientApp')

class BuildWithLatexCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.active_window().run_command('save')
        tex_file_name_with_path=self.window.active_view().file_name()
        pdf_file_name_with_path='/home/tb/.latex_exports/' + path.basename(tex_file_name_with_path)[:-3] + 'pdf'
        subprocess.Popen(['pdflatex', '-quiet', '-output-directory', '/home/tb/.latex_exports', tex_file_name_with_path], cwd=path.dirname(tex_file_name_with_path))
        subprocess.Popen(['mv', pdf_file_name_with_path, '/home/tb/Export/'])


class OpenTodoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        view.window().open_file('/home/tb/Doc/Skrivebibliotek/noter-dansk.org')


class FindInFilesGotoCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        if view.name() == "Find Results":
            line_no = self.get_line_no()
            file_name = self.get_file()
            if line_no is not None and file_name is not None:
                caretpos = view.sel()[0].begin()
                (row,col) = view.rowcol(caretpos)
                file_loc = "%s:%s:%s" % (file_name, line_no, col -6)
                view.window().open_file(file_loc, sublime.ENCODED_POSITION)
            elif file_name is not None:
                view.window().open_file(file_name)

    def get_line_no(self):
        view = self.view
        if len(view.sel()) == 1:
            line_text = view.substr(view.line(view.sel()[0]))
            match = re.match(r"\s*(\d+).+", line_text)
            if match:
                return match.group(1)
        return None

    def get_file(self):
        view = self.view
        if len(view.sel()) == 1:
            line = view.line(view.sel()[0])
            while line.begin() > 0:
                line_text = view.substr(line)
                match = re.match(r"(.+):$", line_text)
                if match:
                    if path.exists(match.group(1)):
                        return match.group(1)
                line = view.line(line.begin() - 1)
        return None
