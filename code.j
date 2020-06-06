.class public code
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
    if_icmpne L_edf
    iconst_2
    istore_1
    goto L_094
L_edf:
    bipush 7
    istore_2
L_094:
    iload_2
    bipush 10
    if_icmpge L_d18
    iload_2
    iconst_2
    iadd
    istore_2
    goto L_094
L_d18:
     return
.end method