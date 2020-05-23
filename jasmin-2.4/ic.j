.class public iccode
.super java/lang/Object 
.method public <init>()V 
    aload_0 
    invokespecial java/lang/Object/<init>()V 
    return 
.end method 
.method public static main([Ljava/lang/String;)V 
    .limit stack 10 
    .limit locals 100 
    iconst_5
    istore_1
    iload_1
    i2f
    iload_1
    i2f
    ldc 2.5f
    fmul
    fadd
    fstore_2
    fload_2
    ldc 3.0f  ; instead of iconst_3
    fcmpg
    ifge L_899
    bipush 7
    istore_1
    goto L_fbb
L_899:
    iconst_3
    istore_1
L_fbb:
    iload_1
    iconst_5
    if_icmpge L_fbb
    iconst_1
    iload_1
    iadd
    istore_1
    getstatic java/lang/System/out Ljava/io/PrintStream; 
    iload_2
    invokevirtual java/io/PrintStream/println(I)V   ; print x
    return
.end method
