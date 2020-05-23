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
    iconst_3
    fcmpg
    ifge L_899
    bipush 7
    istore_1
    goto L_fbb
L_899:
    iconst_3
    istore_1
L_fbb:

L_a5a:
    iload_1
    iconst_5
    if_icmpge L_a5a
    iinc 1,1
    istore_1
