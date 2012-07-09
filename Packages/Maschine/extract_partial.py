import sublime, sublime_plugin
import functools
import os.path
import codecs

class ExtractPartialCommand(sublime_plugin.TextCommand):
  """Extract selection into partial."""
  def run(self, edit):

    partial_directory = os.path.dirname(self.view.file_name())
    selection = self.view.sel()

    partial_content = ""
    for region in selection:
      partial_content += self.view.substr(region)

    self.view.window().show_input_panel(
      "Extract to partial:",
      "",
      functools.partial(self.on_done, partial_directory, partial_content),
      None,
      None)

  def on_done(self, partial_directory, partial_content, partial_name):
    partial_path = partial_directory + "/_" + partial_name + ".html.erb"

    partial_file = codecs.open(partial_path, "w", "utf-8")
    partial_file.write(partial_content)
    partial_file.close()

    view = self.view.window().open_file(partial_path)