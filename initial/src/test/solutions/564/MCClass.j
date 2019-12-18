.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label2:
Label4:
Label6:
	iconst_0
	istore_1
Label10:
	iload_1
	bipush 10
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label11
	iconst_5
	istore_2
Label16:
	iload_2
	bipush 50
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label17
Label20:
	iload_2
	iload_1
	isub
	i2f
	invokestatic io/putFloatLn(F)V
	iload_2
	istore_1
	iload_1
	bipush 30
	if_icmple Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label24
	goto Label25
Label24:
	goto Label19
Label25:
Label21:
Label18:
	iload_2
	bipush 10
	iadd
	istore_2
	goto Label16
Label17:
Label19:
Label12:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label10
Label11:
Label13:
Label7:
Label5:
Label26:
	iconst_0
	istore_2
Label30:
	iload_2
	bipush 12
	if_icmpge Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifle Label31
Label34:
.var 3 is c I from Label34 to Label35
	bipush 10
	istore_3
	iload_3
	iload_2
	iadd
	iconst_2
	idiv
	istore_1
	iload_1
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label35:
Label32:
	iload_2
	iconst_2
	imul
	istore_2
	goto Label30
Label31:
Label33:
Label27:
Label3:
Label1:
	return
.limit stack 18
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
