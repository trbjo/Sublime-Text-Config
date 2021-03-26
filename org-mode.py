import sublime
import sublime_plugin


class OrgmodeFoldLinksCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # region_to_fold = sublime.Region()
        self.view.fold(self.view.find_by_selector("url.link.text.org"))

    def is_enabled(self):
        return self.view.match_selector(0, "text.org")

class OrgFoldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        folded = self.view.fold(self.view.find_by_selector("markup.heading.2.text.org"))
        if not folded:
            self.view.unfold(self.view.find_by_selector("markup.heading.2.text.org"))


    def is_enabled(self):
        return self.view.match_selector(0, "text.org")


class OrgmodeLinkFolder(sublime_plugin.ViewEventListener):
    @classmethod
    def is_applicable(cls, settings):
        return settings.get("syntax").endswith("Zorgmode.sublime-syntax")

    def on_load(self):
        self.view.run_command("orgmode_fold_links")

    on_post_save = on_load



class GetEntryNumberCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        caretpos = v.sel()[0].begin()
        (row,col) = v.rowcol(caretpos)
        secondcharofline = v.substr(v.text_point(row, 1))
        islistmultipledigits = str.isdigit(secondcharofline)
        if islistmultipledigits:
            currentlistnumber = v.substr(v.text_point(row, 0)) + secondcharofline
        else:
            currentlistnumber = v.substr(v.text_point(row, 0))
        try:
            v.insert(edit, caretpos, '\n' + str(self.op(int(currentlistnumber))) + '. ')
        except ValueError:
            pass

class AddListEntryCommand(GetEntryNumberCommand):
    def op(self, value):
        return value + 1
