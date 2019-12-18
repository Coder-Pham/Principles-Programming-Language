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
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	iload_1
	iload_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iload_1
	iload_2
	idiv
	invokestatic io/putInt(I)V
	goto Label15
Label14:
	iload_1
	iload_2
	isub
	invokestatic io/putInt(I)V
Label15:
	goto Label11
Label10:
	iconst_2
	istore_1
Label18:
	iload_1
	iload_2
	if_icmpgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label19
Label22:
	bipush 10
	istore_2
	iload_2
	iload_1
	imul
	invokestatic io/putIntLn(I)V
Label23:
Label20:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label18
Label19:
Label21:
Label11:
Label7:
	goto Label5
Label4:
Label24:
Label26:
	iload_1
	invokestatic io/putInt(I)V
Label27:
Label25:
Label5:
Label1:
	return
.limit stack 14
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
