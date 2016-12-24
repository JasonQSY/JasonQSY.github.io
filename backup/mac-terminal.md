Title: Configuration of Terminal on Mac OS X
Date: 2016-2-9
Category: terminal 

The basic platform is Mac OS X. However, Ubuntu Server 14.04 will be covered partly.
# Base
- iTerm2 installed
- Xcode installed (maybe unnecessary)
- HomeBrew installed
- git installed (Command line tool)

# Zsh
zsh has been installed with Mac OS X and not installed in Ubuntu Server. With Ubuntu,

    apt-get install zsh
Nevertheless, verify zsh first.

    cat /etc/shells
Something like /bin/zsh (in Mac) should be displayed.
Then, we switch to zsh from bash.

    chsh -s /usr/zsh

Note that the configuration file of zsh in Mac is 
```
vim ~/.zshrc
```

# Oh-my-zsh
The instructions on the Internet is commonly not the latest. Please refer to oh-my-zsh in GitHub to find how to install oh-my-zsh. The common command uses curl.
After installation, ~/.zshrc has been editted. We need modify a bit. For beginners, random theme can be employed.
```
ZSH_THEME=random
```
However, agnoster is a popular theme and we should install powerline (a font) first (also in GitHub). A convenient method is by pip.
```
pip install powerline-status
```
Then,
```
ZSH_THEME=agnoster
```
Finally, edit the font of iTerm2. I use "12pt Meslo LG M DZ Regular for Powerline" both for "Regular Font" and "Non-ASCII Font".

#Theme of iTerm2
iTerm2 theme is modified by GUI. Take solarized dark for example. Clone the iterm2-solarized theme from GitHub and open the theme in finder. Then, open Prefenences->Profile->Colors->Load Presets->Solarized Dark

# Colorscheme of Vim
I prefer desert. Solarized also OK.
```shell
"Theme 
syntax enable
"set background=dark
"colorscheme solarized
color desert

"Indent
set autoindent
set cindent
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab "Do not replace tab with space

"Search
set incsearch

"Appearance
set number "line number
set cul "highlight current line
set ruler
```
# Further
- autojump
    - improve cd
- zsh-syntax-highlighting
    - highlight ls
- tmux
- iterm分屏等

