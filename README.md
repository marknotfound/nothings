# Do Nothing Scripts

The instructions/steps are specific to my own use case, so please fork and modify to your needs :)

### Usage
```
$ git clone git@github.com:marknotfound/nothings.git
$ cd nothings && chmod u+x nothings.py
$ ./nothings.py

>> Hit Enter after each step is completed

>>>> Check email
>>>> Make follow up notes for any actionable emails
>>>> Check calendar
>>>> Make follow up notes for any actionable meetings
>>>> Check status of any open diffs
>>>> Check JIRA board and see what's in flight. Make any necessary comments/updates.
>>>> Write down standup notes
>>>> Write down and star ONE task to achieve today

>>>>>>> Good job! Have a great day :) <<<<<<<

>>>> Responsibility is not inherited, it is a choice that everyone needs to make at some point in their life.
>> Byron Pulsifer
```

### Optional Steps
1. Set up a bash alias to run the script from anywhere.
```
$ echo alias morning="/Users/mdunphy/workspace/dailies/nothings.py" >> ~/.bash_profile
```