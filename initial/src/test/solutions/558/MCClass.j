.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is b I from Label2 to Label3
Label4:
	iconst_4
	istore_1
	iload_1
	iconst_0
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iconst_0
	invokestatic io/putInt(I)V
	goto Label9
Label8:
Label10:
.var 2 is a I from Label10 to Label11
Label12:
	iconst_5
	istore_2
.var 3 is i I from Label12 to Label13
	iconst_3
	istore_3
	iconst_5
	iconst_3
	irem
	i2f
	invokestatic io/putFloatLn(F)V
	iload_1
	iload_2
	isub
	iload_3
	isub
	i2f
	invokestatic io/putFloat(F)V
Label13:
Label11:
Label9:
Label5:
Label3:
Label1:
	return
.limit stack 7
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
