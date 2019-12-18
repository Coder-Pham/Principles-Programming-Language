.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static check I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 12
	putstatic MCClass/check I
.var 1 is a I from Label0 to Label1
Label4:
Label8:
Label12:
	iconst_2
	istore_1
Label18:
	iload_1
	iconst_2
	imul
	iconst_1
	isub
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label20:
	iload_1
	iconst_5
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label19
	goto Label18
Label19:
Label21:
	goto Label15
Label14:
	iload_1
	bipush 100
	if_icmpeq Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label13
	goto Label12
Label13:
Label15:
	invokestatic io/putLn()V
	iconst_2
	istore_1
Label24:
	iload_1
	iconst_2
	imul
	iconst_1
	isub
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label26:
	iload_1
	iconst_5
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label25
	goto Label24
Label25:
Label27:
	getstatic MCClass/check I
	iconst_1
	iadd
	putstatic MCClass/check I
Label9:
Label6:
	getstatic MCClass/check I
	bipush 15
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 15
.limit locals 2
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
