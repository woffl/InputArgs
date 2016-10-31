import sublime
import sublime_plugin


class History:
    hist = []
    index = None

    def insert(self, user_input):
        if not self.hist or (user_input != self.last()):
            self.hist.append(user_input)
            self.index = None

    def roll(self, backwards=False):
        if self.index is None:
            self.index = -1 if backwards else 0
        else:
            self.index += -1 if backwards else 1

        if self.index == len(self.hist) or self.index < -len(self.hist):
                self.index = -1 if backwards else 0

    def last(self):
        return self.hist[-1] if self.hist else None

    def get(self, index=None):
        if not index:
            index = self.index
        return self.hist[index] if self.hist else None

    def reset_index(self):
        self.index = None

if 'history1' not in globals():
    history1 = History()


class InputArgsHistory(sublime_plugin.TextCommand):
    def run(self, edit, backwards=False):
        history1.roll(backwards)
        self.view.erase(edit, sublime.Region(0, self.view.size()))
        self.view.insert(edit, 0, history1.get())


class InputArgsHistoryListener(sublime_plugin.EventListener):
    # restore History index
    def on_deactivated(self, view):
        history1.reset_index()