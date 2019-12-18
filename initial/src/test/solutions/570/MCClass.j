.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
	iconst_2
	istore_1
	iload_1
	iconst_2
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
Label6:
	iconst_2
	istore_2
	iload_1
	iload_2
	if_icmpeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	return
Label11:
	iconst_2
	istore_1
Label14:
	iload_1
	iload_2
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label15
Label18:
	bipush 10
	istore_2
	iload_2
	iload_1
	imul
	invokestatic io/putIntLn(I)V
Label19:
Label16:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label14
Label15:
Label17:
	iload_1
	iload_2
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label22
	iload_1
	iload_2
	idiv
	invokestatic io/putInt(I)V
	goto Label23
Label22:
	iload_1
	iload_2
	isub
	invokestatic io/putInt(I)V
Label23:
Label7:
	goto Label5
Label4:
Label24:
	return
	iload_1
	invokestatic io/putInt(I)V
Label25:
Label5:
Label1:
	return
.limit stack 15
.limit locals 3
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
