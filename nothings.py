#!/usr/local/bin/python
from quotes import QuoteGenerator

class MorningRoutine(object):
  instructions = [
    "Check email",
    "Make follow up notes for any actionable emails",
    "Check calendar",
    "Make follow up notes for any actionable meetings",
    "Check status of any open diffs",
    "Check JIRA board and see what's in flight. Make any necessary comments/updates.",
    "Write down standup notes",
    "Write down and star ONE task to achieve today"
  ]

  def run(self):
    print("\n>> Hit Enter after each step is completed\n")
    for step in self.instructions:
      raw_input(">>>> {}".format(step))


if __name__ == "__main__":
  MorningRoutine().run()
  print("\n>>>>>>> Good job! Have a great day :) <<<<<<<")
  quote = QuoteGenerator().get_random_quote()
  print("\n>>>> {}".format(quote['quote']))
  print(">> {}".format(quote['author'] if quote['author'] != '' else 'Unknown'))