.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is b I from Label2 to Label3
	iconst_1
	istore_1
Label6:
	iload_1
	bipush 12
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
Label10:
	iload_1
	invokestatic io/putIntLn(I)V
	iload_1
	iconst_0
	if_icmpeq Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_0
	invokestatic io/putInt(I)V
	goto Label15
Label14:
Label16:
.var 2 is a I from Label16 to Label17
Label18:
	iconst_5
	istore_2
.var 3 is i I from Label18 to Label19
	iconst_3
	istore_3
	iconst_5
	iconst_3
	irem
	i2f
	invokestatic io/putFloatLn(F)V
	iload_2
	ineg
	iload_3
	isub
	i2f
	invokestatic io/putFloatLn(F)V
Label19:
Label17:
Label15:
Label11:
Label8:
	iload_1
	iconst_2
	imul
	istore_1
	goto Label6
Label7:
Label9:
Label3:
Label1:
	return
.limit stack 9
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
