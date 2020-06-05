.class public mycode 
.super java/lang/Object 
.method public <init>()V 
    aload_0 
    invokespecial java/lang/Object/<init>()V 
    return 
.end method 
.method public static main([Ljava/lang/String;)V 
    .limit stack 5 
    .limit locals 100 
    iconst_5
    istore_1
    iload_1
    iload_1
    iconst_2
    imul
    iadd
    istore_2
    getstatic java/lang/System/out Ljava/io/PrintStream; 
    iload_2
    invokevirtual java/io/PrintStream/println(I)V   ; print x
    return
.end method
