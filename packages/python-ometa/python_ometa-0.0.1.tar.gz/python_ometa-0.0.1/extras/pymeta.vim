" Vim syntax file
" Language:         PyMeta
" Maintainer:       Cory Dodt
" Last Change:      $Date: 2009/10/04 14:42:09 $
" Version:          $Id: ometa.vim,v 1.1 2009/10/04 14:42:09 cdodt Exp $    

" Quit when a syntax file was already loaded
if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif

hi link ometaExec NONE
hi link ometaFilter NONE
hi link subExpression NONE
hi link ometaTerminal NONE
hi link ometaIdentifier NONE
hi link ometaSeparator NONE
hi link ometaReturns NONE
hi link ometaOptional NONE
hi link ometaMultiple NONE
hi link ometaNot NONE
hi link ometaVariable NONE
hi link ometaChoice NONE
hi link ometaOp NONE
hi link cddComment NONE
hi link ometaChrLiteral NONE

syn region ometaVariable start=/:/ end=/[^A-Za-z0-9_]/

syn match ometaIdentifier /[A-Za-z0-9_]/
syn match ometaOp         /\(::=\||\|=>\|[|?*+~]\)/
syn match ometaOpNohl     /[()]/ " don't highlight parens - gets annoying

syn region subExpression  start=/(/ end=/)/ contained
syn region ometaTerminal start=/</ end=/>/
syn region ometaExec     start=/!(/ end=/)/ contains=subExpression
syn region ometaFilter   start=/?(/ end=/)/ contains=subExpression
syn region cddComment     start=/COMMENT::=!("""/ end=/""")/
syn region ometaChrLiteral start=/'/ end=/'/

hi link ometaExec       Special
hi link ometaFilter     Special
hi link subExpression    Special
hi link ometaTerminal   Constant
" hi link ometaIdentifier Identifier
hi link ometaOp         Operator
hi link ometaVariable   Identifier
hi link cddComment       Comment
hi link ometaChrLiteral String
