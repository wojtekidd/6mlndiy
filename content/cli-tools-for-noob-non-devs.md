Title: CLI tools for noobs and non-devs - improve your shell experience, promptly. 
Date: 2020-03-03 22:59
Tags: cli, shell, tooling
Slug: cli-tools-for-noob-non-devs
Authors: Wojtek Cichon
Summary: I want to show you some cool CLI tools I found that will enable you to get accustomed to using your shell and enjoying it!

![Picture of shell]({static}/images/shell-by-pankaj-patel.jpg "Terminal shell")

I noticed that people learning to code and non-developers have generally a hard time approaching their operating systems’ shells. No wonder - we’ve got so accustomed to graphic user interfaces that asking your operating system to do things by writing some abstract commands feels pretty awkward to most of us.

When starting to code, or working with software developers sooner than later you’ll have to bang your head against the keyboard, press enter and see what happens. 

I want to show you some cool CLI tools I found that will enable you to get accustomed to using your shell and enjoying it!

## Shell 101

First things first.

"In computing, a **shell** is a user interface for access to an **operating system**'s services. In general, **operating system shells** use either a command-line interface (CLI) or graphical user interface (GUI), depending on a computer's role and particular operation. A **command-line interface** (**CLI**) is a text-based user interface (UI) used to view and manage computer files."
  
My first contact with Linux shell came about the year 2000. Back then, I was what people now call a script kiddie - subscribing Bugtraq, installing Red Hat on Friday nights, tweaking Enlightenment, learning HTML with C++ and thinking how I can put these two together.
  
I’ve got introduced to CLI in high school and since then I feel paranoid when I’m not able to access shell on my laptop or workstation.

## CLI tools I find useful

Here are some CLI tools that make working with shell less hell.  

### fish

[Fish](https://fishshell.com/) stands for **f**riendly **i**nteractive **sh**ell. It’s full of colors, helpful autosuggestions and works across all platforms (macOS, Linux, Windows).

It’s very friendly for users who just started working with CLI. See what happens when I put `git` and just press `[TAB]` a couple of times:

![Animated Fish gif]({static}/images/fishell.gif "Fish shell gif")

**Note:** with fish things might get a bit out of hand when you want to set up your programming environment. I had to google things and work it out when it came to managing the `PATH` variable on some occasions ([here’s a post that saved my life when it came to setting up programming version managers in fish](https://angristan.xyz/2018/07/how-to-use-nvm-rbenv-pyenv-goenv-with-fish-shell/)

Anyway, fish is “smart and user-friendly” and I would highly recommend it to all you CLI n00bs!
  
### bash-git-prompt

This [“informative and fancy bash prompt for Git users”]([https://github.com/magicmonty/bash-git-prompt) is something I wouldn’t be able to live without right now. If you’re working a lot with [Git version-control system](https://en.wikipedia.org/wiki/Git) then this is a must-have.

Thanks to this little addition to my shell I know exactly what’s my current directories’ `git status` without having to execute this command every single time I push/pull/commit/add changes to my local repo.

[Works great with fish](https://github.com/magicmonty/bash-git-prompt#install-for-the-fish-shell) 👍

### The Fuck

Yes - that’s the name of the next CLI tool which I find very helpful. Described as a [“magnificent app which corrects your previous console command”](https://github.com/nvbn/thefuck) it does exactly that.  

With this app, swearing gives you twice the relief 😉

### howdoi

I use this one less, but it’s sometimes very helpful on CLI-only systems where you can’t use a GUI web browser (remember that there are text-mode web browsers like [Lynx](https://lynx.browser.org/) that  work perfectly fine 👌🏻). [Howdoi](https://github.com/gleitz/howdoi) provides short programming-related snippets when you’re lost or you’re just looking for a quick hack.

### fkill

When using CLI you’re able to view all the processes that your computer is currently running by using a `ps` command. There are moments when you want to kill a process or two to unfreeze your machine. What [fkill](https://github.com/sindresorhus/fkill-cli) does is support you with a nice CLI interface to do that instead of making you `grep` through a list of processes and `kill` them one by one.

## Let’s be `less` afraid, shell we?

I hope these tools will make your CLI experience less cumbersome and invite you to use shell a bit more often. For more great CLI tools you can always [check out this awesome CLI apps list on GitHub](https://github.com/agarrharr/awesome-cli-apps)).

Next thing you know, you’ll be contributing to the ‘GUI vs CLI’ discourse on Twitter 😜
