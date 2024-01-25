mov state print

mov a "Digite um Numero:"
syscall

mov state read
syscall

mov state parse_num
syscall

mov b a
push b

mov state print
mov a "Digite o Segundo número"
syscall

mov state read
syscall

mov state parse_num
syscall

push a

pop a
pop b

add a b
mov state print
syscall

push a
syscall

pop a
mov state print
syscall