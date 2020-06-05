iconst 0       ; Push int constant 0
istore 1       ; Store into local variable 1 (i=0)
goto 8         ; First time through don't increment
iinc 1 1       ; Increment local variable 1 by 1 (i++)
iload 1        ; Push local variable 1 (i)
bipush 100     ; Push int constant 100
if_icmplt 5    ; Compare and loop if less than (i < 100)
return         ; Return void when done
