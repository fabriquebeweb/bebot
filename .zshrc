## ENVIRONMENT

export VISUAL=nano
export EDITOR="$VISUAL"

## ANTIGEN

source $HOME/.antigen.zsh

antigen use oh-my-zsh

antigen bundle git
antigen bundle darvid/zsh-poetry
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions

antigen theme romkatv/powerlevel10k

antigen apply

[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

## ALIASES

alias home="cd ~"

alias open="nano"
alias src="exec zsh"

alias py="python"
alias py3="python3"
alias py2="python2"
alias pip="poetry"