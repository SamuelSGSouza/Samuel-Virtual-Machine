<<<<<<< HEAD
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

add a b
mov state print
=======
mov ,state,read 
syscall
mov ,state, parse_num
syscall
mov ,state,print 
>>>>>>> 85169d324febd590d98827a8a565cb0534f148b6
syscall