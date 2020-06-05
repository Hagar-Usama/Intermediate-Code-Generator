.class public code2 
.super java/lang/Object 
.method public <init>()V 
    aload_0 
    invokespecial java/lang/Object/<init>()V 
    return 
.end method 
.method public static main([Ljava/lang/String;)V 
    .limit stack 5 
    .limit locals 100 
    iconst_5	; const 5
    istore_1	; y = 5
    iconst_2	; const 2
    istore_2	; z = 2
    iconst_2	; const 2
    iload_1	; y
    imul	; y*2 = 10
    iload_2	; z
    iadd	; y + 10 = 15
    istore_3	; x = 15
    getstatic java/lang/System/out Ljava/io/PrintStream; 
    iload_3
    invokevirtual java/io/PrintStream/println(I)V   ; print x
    getstatic java/lang/System/out Ljava/io/PrintStream; 
    iload_2
    invokevirtual java/io/PrintStream/println(I)V   ; print z
    getstatic java/lang/System/out Ljava/io/PrintStream; 
    iload_1
    invokevirtual java/io/PrintStream/println(I)V   ; print y
    return
.end method
