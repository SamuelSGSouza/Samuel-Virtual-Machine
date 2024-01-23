mov state print

mov a "Digite um Numero:"
syscall

mov state read
syscall

mov state parse_num
syscall

mov b a

mov state print
mov a "Digite o Segundo número"
syscall

mov state read
syscall

mov state parse_num
syscall

div a b
mov state print
syscall