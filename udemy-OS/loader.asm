[BITS 16]
[ORG 0x7e00]

start:
    mov ah,0x13     ; ah == function code, 13 means print string
    mov al, 1       ; al == write mode, 1 means cursor placed at end of string
    mov bx,0xa      ; prints in green
    ; bh holds page number, bl holds character attributes
    xor dx,dx
    ; dh represents rows, dl represents columns - this sets cursor to top left
    mov bp,Message  ; address of message to bp register
    mov cx,MessageLen   ; cx holds # characters to print
    int 0x10        ; print service

End:
    hlt
    jmp End

Message:    db  "Loader starts"
MessageLen: equ $-Message