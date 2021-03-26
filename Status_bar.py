# from sublime_plugin import ViewEventListener
# import sublime
# import re

# class HideMenu(sublime_plugin.EventListener):
#     def on_new(self, view):
#         window = view.window()
#         if window.is_menu_visible():
#             window.set_menu_visible(False)

# class CurrentPathStatusEvent(sublime_plugin.ViewEventListener):

    # def on_activated(self):
        # window = self.view.window()
        # if len (window.views()) <= 1:
            # window.set_tabs_visible(False)
        # else:
            # window.set_tabs_visible(True)

# class CurrentPathStatusEventTwo(sublime_plugin.EventListener):
    # def on_activated(self, view):
        # view.settings().set("highlight_line", True)

    # def on_deactivated(self, view):
        # view.settings().set("highlight_line", False)

    # def on_deactivated(self):
        # sublime.Settings().set("highlight_line", False)

    # def on_activated_async(self):
    #     tabs = bool
    #     for group in range(sublime.active_window().num_groups()):
    #         if len(sublime.active_window().views_in_group(group)) > 1:
    #             tabs = True
    #             break
    #         else:
    #             tabs = False
    #     sublime.active_window().set_tabs_visible(tabs)

# class Hej(ViewEventListener):
#     # global my_dict
#     # my_dict = {}
#     # global pp_path

#     # def helper_path(self):
#     #     return sublime.active_window().extract_variables()['file_name'] if self.view.file_name() else self.view.name() if self.view.name() else "New File"
#         # return self.view.name()
#         # try:
#         #     pp_path = my_dict[self.view.buffer_id()]
#         # except Exception:
#         #     pp_path = self.view.file_name().replace('/home/tb', '~') if self.view.file_name() else self.view.name() if self.view.name() else "New File"
#         #     if len(pp_path) < 61:
#         #         return pp_path
#         #     str_length = 0
#         #     included_elems = -1
#         #     words = pp_path.split('/')
#         #     while str_length < 61:
#         #         str_length += len(words[-included_elems]) + 1
#         #         included_elems += 1
#         #     included_elems = included_elems -1 if included_elems > 1 else 1
#         #     shortened_words = list(map(lambda x: x[0], words[:(len(words) - included_elems)]))
#         #     pp_path = '/'.join(shortened_words + (words[-included_elems:]))
#         #     my_dict[self.view.buffer_id()] = pp_path
#         # return pp_path

#     def on_load_async(self):
#         self.view.set_status('currentPath', self.helper_path())

#     def on_activated_async(self):
#         self.view.set_status('currentPath', self.helper_path())

#     def on_post_save(self):
#         self.view.erase_status('acon')
#         self.view.set_status('currentPath', self.helper_path())

#     def on_modified_async(self):
#         if self.view.is_dirty():
#             self.view.set_status('acon', '  ')
#         else:
#             self.view.erase_status('acon')

#     def on_pre_save_async(self):
#         sublime.set_timeout(lambda: sublime.status_message('\0'), 20)
#         sublime.set_timeout(lambda: sublime.status_message('\0'), 50)
#         sublime.set_timeout(lambda: sublime.status_message('\0'), 100)
#         sublime.set_timeout(lambda: sublime.status_message('\0'), 200)
#         # self.view.run_command('collapse_lines')

# def selections(view, default_to_all=True):
#     regions = [r for r in view.sel() if not r.empty()]
#     if not regions and default_to_all:
#         regions = [sublime.Region(0, view.size())]
#     return regions

# class CollapseLines(sublime_plugin.TextCommand):
#     def run(self, edit):
#         view = self.view
#         reobj = re.compile(r'(?:\s*)(\r?\n)(?:\s*)(?:\r?\n+)')

#         for region in selections(view):
#             str_buffer = view.substr(region)
#             trimmed = reobj.sub(r'\1\1', str_buffer)
#             if str_buffer != trimmed:
#                 view.replace(edit, region, trimmed)
