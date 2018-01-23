---
layout: post
title:  "Installation of Vim-LaTeX"
date:   2016-02-19
categories: latex
---

# Environment

- Mac OS X with command line tools and Homebrew. Thus my $VIM is at `~/.vim`.
- Macvim (version 7.4.1202) installed by Homebrew
- LaTeX-Suite-aka-Vim-LaTeX (version 1.5)

Something about vim version: Please refer to the docs of Vim-LaTeX to see if the vim version meets the requirements. Vim-LaTeX also recommends using Macvim and I agree.

# Installation with Vundle

    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Edit `~/.vimrc` as the docs.

```vim
"Plugins managed by Vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'

"LaTeX Plugins
"Uncomment the following after installation of latex-suite
"Plugin 'LaTeX-Suite-aka-Vim-LaTeX'

call vundle#end()
filetype plugin indent on

"LaTeX-Suite-aka-Vim-LaTeX Configuration
let g:tex_flavor='latex' "Use vim-latex even when *.tex file is newcreated)
autocmd BufEnter *.tex set sw=2
```

Open Macvim, enter `:InstallBundle LaTeX-Suite-aka-Vim-LaTeX` and wait for downloading. Uncomment `Plugin 'LaTeX-Suite-aka-Vim-LaTeX'` in `~/.vimrc`. The installation is completed now.

A simple test. Open an arbitary `.tex` file and auto-completion works now.

# Configuration

## Compilation
The primary configuration file is `texrc`. Follow the instructions in `texrc`, first we copy it preventing it from being overwritten.

	mkdir ~/.vim/ftplugin/tex
    cp ~/.vim/bundle/LaTeX-Suite-aka-Vim-LaTeX/ftplugin/latex-suite/texrc ~/.vim/ftplugin/tex/
    vim ~/.vim/ftplugin/tex/texrc


- Line 87 & 89 `TexLet g:Tex_DefaultTargetFormat = 'pdf'`.
- Line 115 `TexLet g:Tex_CompileRule_pdf = 'xelatex -interaction=nonstopmode'`
- Line 147 `TexLet g:Tex_ViewRule_pdf = 'open -a Preview'`

`Tex_ViewRule_pdf` can also be something like `'open -a /Application/Skim.app'`. Note that at least in my mac, there is something strange arround line 147. Sometimes `if has('macunix')` takes effect and sometimes `else` takes effect. For convenience, I just set all `Tex_ViewRule_pdf` to be `'open -a Preview'`.

A simple test. Enter `\ll` and `\lv` in the command mode.

## Map and Macros
Configuration here is just for convenience. Configuration file about map can be put in `tex.vim`.
```vim
vim ~/.vim/ftplugin/tex.vim
```
```vim
" F2 save and compile
map <F2> <ESC>:w<CR>\ll

" F3 to preview
map <F3> <ESC>:w<CR>\lv

" F4 to save and close the window
map <F4> <ESC>:wq<CR>

" IMAP
augroup MyIMAPs
    au!
    au VimEnter * call IMAP('`j', '\lim_{<++> \to <++>}<++>', '')
    au VimEnter * call IMAP('`i', '\int_{<++>}^{<++>}<++>', '')
    au VimEnter * call IMAP('`o', '\sum_{<++>}^{<++>}<++>', '')
augroup END
```
When editing the file `i` can call the plugin of integration. j and o are similar. After you edit the file, `<F2>` can save and compile the file and `<F3>` can preview the pdf-file. `<F4>` is similar.

## Folding
Perhaps you can configure the global variable in `tex.vim`. However, it also does not work in my mac. I use this way.
```
vim ~/.vim/bundle/LaTeX-Suite-aka-Vim-LaTeX/ftplugin/latex-suite/folding.vim
```

Add this after `AddSyntaxFoldItem`.

```
" { { { exercise
call AddSyntaxFoldItem (
    \ '^\s*\\begin{exercise}',
    \ '^\s*\\end{exercise}',
    \ 0,
    \ 0
    \ )
" }}}
```
Here everything should be editted carefully like `exercise`.
