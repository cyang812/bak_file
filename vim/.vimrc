call plug#begin()

Plug 'junegunn/fzf.vim'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'chriskempson/base16-vim'

call plug#end()
