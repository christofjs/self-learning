[BITS 16]
[ORG 0x7c00]

start:
    xor ax,ax
    mov ds,ax
    mov es,ax
    mov ss,ax
    mov sp,0x7c00

TestDiskExtension:
    ; dl holds drive id when BIOS transfers control to boot code
    mov [DriveId],dl    ; square brackets to access location
    mov ah,0x41
    mov bx,0x55aa
    int 0x13
    jc NotSupport
    cmp bx,0xaa55       ; if not, extension service not supported
    jne NotSupport

LoadLoader:
    mov si,ReadPacket
    mov word[si],0x10       ; size
    mov word[si+2],5        ; # sectors
    mov word[si+4],0x7e00   ; offset
    mov word[si+6],0        ; segment
    mov dword[si+8],1       ; address lo
    mov dword[si+0xc],0     ; address hi
    mov dl,[DriveId]
    mov ah,0x42
    int 0x13
    jc  ReadError

    mov dl,[DriveId]
    jmp 0x7e00

ReadError:
NotSupport:
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
    hlt             ; place processor in halt state
    jmp End         ; in case of interrupt

DriveId:        db 0
Message:        db  "We have an error in the boot process"
MessageLen:     equ $-Message
ReadPacket:     times 16 db 0

times (0x1be-($-$$)) db 0   ; repeats command number of times - parens is how many times db is repeated
    ; $$ represents beginning of current section (start of code in this case)
    ; $-$$ == start of code to end of message
    ; 0x1be == partition entries
    ; 0x1be-($-$$) == start of code to end of message is a block, then fills all zeroes from there to 0x1be
    ; sets us up to begin filling partition

    db 80h      ; boot indicator (bootable partition)
    db 0,2,0    ; start CHS (cylinder, head, sector)
                    ; first byte -- head
                    ; second -- bits 0-5:sector
                    ;           bits 6-7:cylinder
                    ; third -- lower 8 bits of cylinder value
                    ; fourth -- partition type
                    ; next three bytes -- ending CHS value
                ; cylinder 0 is first cylinder
                ; sector 1 is first sector
    db 0f0h
    db 0ffh,0ffh,0ffh
    dd 1
    dd (20*16*63-1)

    times (16*3) db 0

    ; signature
    db 0x55
    db 0xaa