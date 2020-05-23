.class public ic2
.super java/lang/Object 
.method public <init>()V 
    aload_0 
    invokespecial java/lang/Object/<init>()V 
    return 
.end method 
.method public static main([Ljava/lang/String;)V
    .limit stack 10 
    .limit locals 100 
    iconst_3
    istore_1
    iconst_4
    istore_2
    iconst_5
    istore_3
    iload_1
    iload_2
    iconst_2
    imul
    iadd
    istore_3
    iload_3
    bipush 11
    if_icmpne L_7ba
    iconst_2
    istore_1
    goto L_77a
L_7ba:
    bipush 7
    istore_2
L_77a:
L_7f2:
    iload_2
    bipush 10
    if_icmpge L_4af
    iload_2
    iconst_2
    iadd
    istore_2
    goto L_7f2
L_4af:
    getstatic java/lang/System/out Ljava/io/PrintStream; 
    iload_2
    invokevirtual java/io/PrintStream/println(I)V   ; print x
    return
.end method
