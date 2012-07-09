import sublime, sublime_plugin
import os, time

class RestartRackCommand(sublime_plugin.TextCommand):
  """Touch tmp/restart.txt file in the Rack project to restart application."""
  def run(self, edit):
    for folder in self.view.window().folders():
      fname = os.path.join(str(folder), "tmp", "restart.txt")
      if os.path.exists(os.path.dirname(fname)):
        with file(fname, "a"):
          os.utime(fname, None)
          sublime.status_message("Restarted Rack application.")
      else:
        sublime.status_message("Rack restart failed.")