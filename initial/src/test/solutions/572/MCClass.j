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
	iconst_3
	istore_2
.var 3 is fl F from Label0 to Label1
Label2:
	iconst_3
	i2f
	fstore_3
	iload_1
	iload_2
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
Label8:
Label12:
	fload_3
	iload_1
	i2f
	fmul
	iload_2
	i2f
	fload_3
	fdiv
	fadd
	fstore_3
	iload_1
	iload_2
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	fload_3
	iconst_1
	ineg
	i2f
	fsub
	fstore_3
	fload_3
	invokestatic io/putFloatLn(F)V
	goto Label19
Label18:
	fload_3
	invokestatic io/putFloatLn(F)V
Label19:
Label14:
	fload_3
	ldc 12.2
	fcmpl
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label13
	goto Label12
Label13:
Label15:
Label9:
	goto Label7
Label6:
Label20:
Label22:
	bipush 6
	istore_1
Label26:
	iload_2
	iload_1
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label27
Label30:
	fload_3
	ldc 2.2
	fcmpl
	ifle Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifgt Label34
	goto Label35
Label34:
	iload_2
	istore_1
Label35:
Label31:
Label28:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label26
Label27:
Label29:
Label23:
Label21:
Label7:
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
