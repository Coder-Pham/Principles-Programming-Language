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
	iconst_0
	istore_1
Label8:
	iload_1
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	iconst_5
	istore_2
Label14:
	iload_2
	bipush 50
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label15
Label18:
	iload_2
	iload_1
	isub
	i2f
	invokestatic io/putFloatLn(F)V
	iload_2
	istore_1
	iload_1
	bipush 30
	if_icmple Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label22
	goto Label23
Label22:
	goto Label17
Label23:
Label19:
Label16:
	iload_2
	bipush 10
	iadd
	istore_2
	goto Label14
Label15:
Label17:
Label10:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label9:
Label11:
Label5:
Label24:
	iconst_0
	istore_2
Label28:
	iload_2
	bipush 12
	if_icmpge Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label29
Label32:
.var 3 is c I from Label32 to Label33
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
Label33:
Label30:
	iload_2
	iconst_2
	imul
	istore_2
	goto Label28
Label29:
Label31:
Label25:
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
